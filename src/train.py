"""
Training module for Credit Card Fraud Detection project.
Handles model initialization and training.
"""

from sklearn.linear_model import LogisticRegression


def train_model(X_train, y_train):
    model = LogisticRegression(
        max_iter=1000,
        class_weight='balanced',
        random_state=42
    )
    
    model.fit(X_train, y_train)
    return model
