import math

print("="*60)
print("  NomaanOS - Pure Python Single Neuron Perceptron Engine")
print("="*60)

# Sigmoid Activation Function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Training Data: [Feature 1 (Anomalous Port), Feature 2 (Large Payload)] -> Target Threat (0 or 1)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 1]  # Decision Gate Threshold

# Initialize Weights & Bias
w1, w2 = 0.1, 0.1
b = 0.0
lr = 0.5  # Learning Rate

print("\n[+] Training Neural Network (1 Perceptron Neuron)...")
print("-" * 55)

epochs = 1000
for epoch in range(1, epochs + 1):
    total_error = 0
    for i in range(len(X)):
        x1, x2 = X[i]
        target = Y[i]
        
        # Forward Pass
        z = w1 * x1 + w2 * x2 + b
        prediction = sigmoid(z)
        
        # Error calculation
        error = target - prediction
        total_error += abs(error)
        
        # Backpropagation / Weight Adjustment
        w1 += lr * error * x1
        w2 += lr * error * x2
        b += lr * error

    if epoch in [1, 10, 100, 500, 1000]:
        print(f" -> Epoch {epoch:4d} | Weights: [{w1:.3f}, {w2:.3f}] | Bias: {b:.3f} | Error: {total_error:.4f}")

print("-" * 55)
print("\n[+] Final Trained Predictions:")
for x1, x2 in X:
    z = w1 * x1 + w2 * x2 + b
    pred = sigmoid(z)
    binary_class = 1 if pred >= 0.5 else 0
    print(f" Inputs: [{x1}, {x2}] -> Output Prob: {pred:.4f} -> Class: {binary_class}")

print("\n[🚀 Model Training Complete]: Single Neuron Perceptron Operational!")
