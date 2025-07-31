import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Example: using dummy features
X = pd.DataFrame({
    'income': np.random.rand(100),
    'credit_utilization': np.random.rand(100),
    'missed_payments': np.random.randint(0, 3, 100),
    'debt_to_income': np.random.rand(100)
})
y = (X['missed_payments'] > 1).astype(int)  # Synthetic target

# Train model
model = LogisticRegression()
model.fit(X, y)

# Plot coefficients
coef = model.coef_[0]
features = X.columns

plt.figure(figsize=(6, 4))
bars = plt.bar(features, coef, color='#66B3FF')
plt.axhline(0, color='gray', linestyle='--')
plt.title('Feature Influence on Delinquency (Logistic Regression)')
plt.ylabel('Coefficient')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Logistic_Regression_Coefficients.png")
plt.show()
