import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Emotional-Tone-Dataset.csv")

# Count occurrences of each label
label_counts = df['LABEL'].value_counts()

# Plotting
plt.figure(figsize=(8, 6))
label_counts.plot(kind='bar', color='skyblue')
plt.title('Label Distribution')
plt.xlabel('Labels')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

#################################################

# Handling missing values
df['TWEET'] = df['TWEET'].fillna('')  # Replace missing values with an empty string

# Text cleaning: remove special characters, numbers, and convert to lowercase
df['cleaned_text'] = df['TWEET'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower())))

# Remove stop words
stop_words = set(stopwords.words('arabic'))
df['cleaned_text'] = df['cleaned_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Stemming using SnowballStemmer for Arabic
stemmer = SnowballStemmer("arabic")
df['cleaned_text'] = df['cleaned_text'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))

# Split the dataset into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(
    df['cleaned_text'],
    df['LABEL'],  # Update this to the correct column name
    test_size=0.2,
    random_state=42
)

# Tokenization using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(train_data)
X_test_tfidf = tfidf_vectorizer.transform(test_data)