import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Create synthetic binary classification data
X, y = make_classification(n_samples=100, n_features=1, n_redundant=0, 
                           n_informative=1, random_state=0, class_sep=1.5)

# Fit logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Predict probability
X_test = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
y_prob = model.predict_proba(X_test)[:, 1]

# Plot
plt.figure(figsize=(6, 4))
plt.scatter(X, y, c='black', label='Customer Data')
plt.plot(X_test, y_prob, color='blue', linewidth=2, label='Logistic Regression Curve')
plt.title('Probability of Delinquency vs. Predictor')
plt.xlabel('Feature (e.g., Credit Utilization)')
plt.ylabel('Predicted Probability of Delinquency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Logistic_Regression_Probability_Curve.png")
plt.show()
