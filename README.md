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



