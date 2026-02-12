# 💳 Credit Card Fraud Detection

An end-to-end machine learning project for detecting fraudulent credit card transactions on highly imbalanced data.

## 📌 Overview
This project focuses on identifying fraudulent transactions using supervised machine learning. The dataset contains 284,000+ transactions, with fraud cases representing less than 0.2% of total data.

## 🚀 Key Highlights
- Handled severe class imbalance
- Used stratified train-test split
- Applied feature scaling (StandardScaler)
- Built Logistic Regression model with class-weight balancing
- Evaluated using Precision, Recall, F1-score, and ROC-AUC

## 🛠 Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## 📊 Dataset
Kaggle Credit Card Fraud Detection Dataset  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## 📈 Model Performance

- ROC-AUC Score: ~0.97
- Improved Recall for Fraud Detection using class-weight balancing
- Successfully handled extreme class imbalance 

### Key Insight
In fraud detection, minimizing false negatives (missed frauds) is more important than overall accuracy.

