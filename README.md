# 📧 Email Spam Classifier

An Email Spam Classifier built using machine learning to distinguish between spam and legitimate (ham) emails. This project showcases a typical text classification pipeline including data preprocessing, feature extraction, model training, evaluation, and deployment.

🚀 **Live :** [https://email-spam-predictor.onrender.com](https://email-spam-predictor.onrender.com)

## 🚀 Features

- Preprocesses raw email data (cleaning, tokenization, stopword removal)
- Converts text into numerical features using TF-IDF
- Trains multiple ML models (Naive Bayes, SVM, Logistic Regression, etc.)
- Evaluates model performance using metrics like accuracy, precision.
- Provides a simple interface for classifying custom input emails

## 🧠 Technologies Used

- Python 🐍
- scikit-learn
- pandas, NumPy
- NLTK / spaCy (for text processing)
- Matplotlib / Seaborn (for visualization)
- Flask (for optional UI deployment)
- Render (for deployment)

## 📊 Dataset

The project uses the [Spam Email Dataset](https://www.kaggle.com/datasets/abdmental01/email-spam-dedection) 

- 5,157 mails tagged as spam or ham
- Plain text format

