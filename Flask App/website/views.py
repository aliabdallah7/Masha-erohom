from flask import Flask, Blueprint, render_template, request, make_response, send_from_directory, redirect, url_for
from flask_login import login_required, current_user
from .models import File
from werkzeug.utils import secure_filename
from datetime import datetime
from . import db
from Marbert.BertClassifier import get_sentiment
import pandas as pd
import os
import json
views = Blueprint('views', __name__)
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        file = request.files['file']
        classifications = []
        if file and allowed_file(file.filename):
            Rfile = pd.read_csv(file)
            if 'text' in Rfile.columns:
                for text in Rfile['text']:
                    output = get_sentiment(text)
                    classifications.append(output)

                Rfile['prediction'] = classifications
                filename = secure_filename(file.filename)
                new_filename = f'{filename.split(".")[0]}_predicted_{str(datetime.now()).replace(":", "-")}.csv' 
                save_location = os.path.join('predictedData', new_filename)
                Rfile.to_csv(save_location, index=False)
                new_file=File(file_name=new_filename,user_id=current_user.id)
                db.session.add(new_file)
                db.session.commit()
                
                return redirect(url_for('views.chart', filename=new_filename))
            else:
                return "The uploaded file does not contain a 'text' column."
        else:
            return "The uploaded file is not a CSV file."
    else:
        return render_template("home.html", user=current_user)

@login_required
@views.route('/download/<filename>',methods=['GET'])
def download(filename):
    return send_from_directory('predictedData', filename, as_attachment=True)

@login_required
@views.route('/chart/<filename>', methods=['GET'])
def chart(filename):
    file_path = os.path.join('predictedData', filename)
    df = pd.read_csv(file_path)

    joy_count = (df['prediction'] == 'joy').sum()
    anger_count = (df['prediction'] == 'anger').sum()
    sadness_count = (df['prediction'] == 'sadness').sum()
    love_count = (df['prediction'] == 'love').sum()
    sympathy_count = (df['prediction'] == 'sympathy').sum()
    surprise_count = (df['prediction'] == 'surprise').sum()
    fear_count = (df['prediction'] == 'fear').sum()
    none_count = (df['prediction'] == 'none').sum()

    categories = ['joy', 'anger', 'sadness', 'love', 'sympathy', 'surprise', 'fear', 'none']
    counts = [joy_count, anger_count, sadness_count, love_count, sympathy_count, surprise_count, fear_count, none_count]
    counts = [int(count) for count in counts]
    categories_json = json.dumps(categories)
    counts_json = json.dumps(counts)
    return render_template('Chart.html', categories=categories_json, counts=counts_json, user=current_user, filename=filename)
@views.route('/History')
def History():
        user_files = File.query.filter_by(user_id=current_user.id).all()
        return render_template('history.html', user_files=user_files, user=current_user)

    
    