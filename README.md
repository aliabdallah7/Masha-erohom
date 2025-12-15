# 🎯 Arabic Sentiment Analysis using Ensemble Deep Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)
![Flask](https://img.shields.io/badge/Flask-2.3+-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A state-of-the-art web application for Arabic emotion detection using an ensemble of deep learning models achieving **90% accuracy** on the Emotone_ar dataset.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Models & Performance](#models--performance)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Results & Comparisons](#results--comparisons)
- [Future Work](#future-work)
- [Team](#team)
- [Citation](#citation)

## 🚀 Project Overview

This project addresses the critical gap in Arabic Natural Language Processing by developing a sophisticated sentiment analysis system specifically designed for Arabic text. The system employs an ensemble of advanced deep learning models to accurately detect and classify eight different emotions in Arabic tweets and social media content.

**Key Achievement:** **90% Accuracy** - State-of-the-art performance on Arabic emotion detection

## ✨ Key Features

### 🔍 Dual Functionality
1. **CSV File Processing**
   - Upload Excel/CSV files containing Arabic text
   - Automatic emotion classification
   - Download enriched dataset with emotion labels
   - Interactive dashboard with visualizations

2. **Real-time Twitter Analysis**
   - Search for keywords on Twitter
   - Retrieve 50 most recent tweets
   - Real-time sentiment analysis
   - Visual sentiment distribution

### 📊 Visualization Dashboard
- Interactive pie charts and bar graphs
- Percentage distribution tables
- Real-time sentiment tracking
- Historical data analysis

## 🏗️ Architecture

### Three-Tier System Design
https://github.com/user-attachments/assets/d4d22c13-da50-4788-8967-e6b8e2782f98


### Model Pipeline
```python
Input → Preprocessing → [Bi-LSTM, Bi-GRU, MARBERTv2] → Stacking → Random Forest → Output
```

## 🤖 Models & Performance

### Ensemble Architecture
We combine three powerful models using Random Forest stacking:

| Model | Description | Key Features |
|-------|-------------|--------------|
| **Bi-LSTM** | Bidirectional Long Short-Term Memory | Captures long-term dependencies, bidirectional context |
| **Bi-GRU** | Bidirectional Gated Recurrent Unit | Efficient, computationally lighter than LSTM |
| **MARBERTv2** | Arabic-specific BERT model | Pre-trained on 1B Arabic tweets, 128GB text data |
| **Random Forest** | Ensemble Meta-learner | Combines predictions from all base models |

### Performance Metrics

| Model | Accuracy | F1-Score | Recall | Precision |
|-------|----------|----------|---------|-----------|
| Bi-GRU | 72% | 71% | 70% | 72% |
| Bi-LSTM | 72% | 71% | 71% | 72% |
| MARBERTv2 | 81% | 80% | 79% | 81% |
| **Ensemble (RF)** | **90%** | **90%** | **90%** | **90%** |

**Note:** Ensemble model outperforms all individual models significantly!

## 📊 Dataset

### Emotone_ar Dataset
- **Size:** 10,065 Arabic tweets
- **Emotions:** 8 categories (Sadness, Anger, Joy, Surprise, Love, Sympathy, Fear, None)
- **Dialects:** Multiple Arabic dialects
- **Annotation:** Manually annotated by 3 native Arabic speakers
- **Balance:** Approximately equal distribution across emotions

**Sample Distribution:**

<img width="691" height="476" alt="image" align="center" src="https://github.com/user-attachments/assets/1ce16925-46f5-45ca-a110-103355e0d076" />

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- 16GB RAM (minimum)
- 50GB free disk space
- Git

### Step-by-Step Setupc
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/arabic-sentiment-analysis.git
cd arabic-sentiment-analysis

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download pre-trained models
python download_models.py

# 5. Initialize database
python init_db.py

# 6. Run the application
python app.py
```

## 📈 Results & Comparisons
### State-of-the-Art Comparison
| Name | Date | Dataset | Model | Accuracy | F1-score |
|------|------|---------|-------|----------|----------|
| Text Based Emotion Recognition in Arabic text | 2019 | Emotone-AR[4] | CNN | 0.70 | 0.70 |
| Textual Emotions | 2023 | Emotone-AR[4] | BI-GRU | 0.73 | 0.74 |
| Improved Emotion Detection Framework for Arabic Text using Transformer Models | 2023 | Emotone-AR[4] | arabic-bert-base model | 0.74 | 0.74 |
| Masha'erohom | 2024 | Emotone-AR[4] | BI-LSTM | 0.72 | 0.71 |
| Masha'erohom | 2024 | Emotone-AR[4] | BI-GRU | 0.72 | 0.71 |
| Masha'erohom | 2024 | Emotone-AR[4] | MARBERT | 0.81 | 0.80 |
| **Masha'erohom** | **2024** | **Emotone-AR[4]** | **Ensemble RF** | **0.90** | **0.90** |


### Confusion Matrix (Ensemble Model)

| Actual \ Predicted | Ang   | Fea  | Joy  | Lov  | Sad  | Sym  | Sur  | Non  |
|--------------------|-------|------|------|------|------|------|------|------|
| **Ang**            | 1296  | 24   | 18   | 12   | 45   | 21   | 15   | 9    |
| **Fea**            | 31    | 1082 | 35   | 18   | 28   | 9    | 2    | 0    |
| **Joy**            | 22    | 19   | 1150 | 32   | 42   | 8    | 7    | 0    |
| **Lov**            | 15    | 8    | 29   | 1120 | 21   | 15   | 5    | 0    |
| **Sad**            | 38    | 21   | 45   | 25   | 1050 | 32   | 33   | 10   |
| **Sym**            | 28    | 12   | 18   | 21   | 35   | 920  | 12   | 0    |
| **Sur**            | 19    | 5    | 12   | 8    | 28   | 14   | 945  | 13   |
| **Non**            | 21    | 8    | 15   | 12   | 35   | 18   | 25   | 1405 |

**Emotion Abbreviations:**
- **Ang**: Anger
- **Fea**: Fear  
- **Joy**: Joy
- **Lov**: Love
- **Sad**: Sadness
- **Sym**: Sympathy
- **Sur**: Surprise
- **Non**: None

## 🔮 Future Work

### Planned Enhancements

#### Model Improvements
- Integrate AraT5 for better text understanding
- Add dialect-specific models
- Implement sarcasm and irony detection

#### Feature Expansion
- Facebook keyword search integration
- Multi-platform social media analysis
- Real-time streaming analysis

#### Technical Upgrades
- Docker containerization
- Cloud deployment (AWS/Azure)
- Mobile application
- API rate limiting and scaling

#### Dataset Expansion
- Include more Arabic dialects
- Add news articles and blogs
- Cross-domain sentiment analysis

## 👥 Team

### Supervisors
- **Dr. Shaimaa Haridy** - Lecturer, Information Systems Department, Ain Shams University

### Development Team

- Ali Abdallah
- Mohamed Ali  
- Karima Sobhi
- Ali Maher
- Abdulthman Abdelhalim
- Hany Mohamed

### Institution
**Ain Shams University**  
Faculty of Computer & Information Sciences  
Information Systems Department  
Cairo, Egypt

## 📚 Citation

If you use this project in your research, please cite:

```bibtex
@article{arabicsentiment2024,
  title={Arabic Sentiment Analysis using Ensemble Deep Learning Model},
  author={Abdallah, Ali and Ali, Mohamed and Sobhi, Karima and Maher, Ali and Mohamed, Hany and Abdelhalim, Abdulthman},
  year={2024},
  publisher={Ain Shams University},
  note={Bachelor's Graduation Project}
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **Ain Shams University** for academic support and resources
- **Nile University** for the Emotone_ar dataset
- **Hugging Face** for pre-trained models and transformers library
- **Google Colab & Kaggle** for computational resources
- All open-source contributors whose work made this project possible

---

**⭐ If you find this project useful, please give it a star on GitHub!**

**📧 Contact:** For questions or collaborations, please email: [eng.aliabdallah7@gmail.com](mailto:eng.aliabdallah7@gmail.com)

**🔗 Live Demo:** [Coming Soon] | **📖 Documentation:** [Full Documentation](docs/)
