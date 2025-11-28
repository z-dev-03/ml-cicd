import pickle, sys, numpy as np
from sklearn.linear_model import LinearRegression

# Train model
X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression().fit(X, y)

# Validate
pred = model.predict([[4]])[0]
print(f"Prediction: {pred:.1f}")

if abs(pred - 8.0) < 0.1:
    pickle.dump(model, open('model.pkl', 'wb'))
    print("PASS - Model saved")
    sys.exit(0)
else:
    print("FAIL")
    sys.exit(1)

#Test Auto 1