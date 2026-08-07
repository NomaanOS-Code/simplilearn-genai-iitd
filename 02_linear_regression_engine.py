import math

print("="*60)
print("  NomaanOS - Pure Python Linear Regression & Stat Engine")
print("="*60)

# Sample Dataset: Study Hours (X) vs Test Score (Y)
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [25, 35, 40, 55, 60, 68, 72, 85, 88, 95]

# 1. Means Calculation
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

# 2. Slope (m) and Intercept (c)
numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y))
denominator = sum((x - mean_x) ** 2 for x in X)

m = numerator / denominator
c = mean_y - (m * mean_x)

print(f"\n[+] Linear Model Equation: Y = {m:.2f}*X + {c:.2f}")

# 3. Model Predictions & R-squared Score Calculation
predictions = [m * x + c for x in X]
ss_res = sum((y - y_hat) ** 2 for y, y_hat in zip(Y, predictions))
ss_tot = sum((y - mean_y) ** 2 for y in Y)
r_squared = 1 - (ss_res / ss_tot)

print(f"[+] Model Accuracy (R² Score): {r_squared:.4f} ({r_squared*100:.2f}%)")

# 4. ASCII Visual Plot Render
print("\n[+] Visual Regression Plot (Actual vs Model):")
print("-" * 55)
for x, y, y_hat in zip(X, Y, predictions):
    actual_bar = "#" * int(y // 5)
    pred_bar = "*" * int(y_hat // 5)
    print(f"X={x:2d} | Actual: {actual_bar:<18} ({y})")
    print(f"     | Model : {pred_bar:<18} ({y_hat:.1f})")
print("-" * 55)

# 5. Inference / Test Prediction
new_x = 12
pred_y = m * new_x + c
print(f"\n[🚀 Test Prediction] Study Hours = {new_x} hrs -> Predicted Score = {pred_y:.1f}%")
