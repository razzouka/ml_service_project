import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
y = np.array([0, 1, 1, 0])

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

with open("dummy_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Real model saved to dummy_model.pkl!")
print(f"Model classes: {model.classes_}")
print(f"Model coef: {model.coef_}")