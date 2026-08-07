import math

print("="*60)
print("  NomaanOS - Pure Python KNN Classification Engine")
print("="*60)

# Training Dataset: (Packet Rate/sec, Payload Size KB, Class Label)
dataset = [
    (10, 5, "Normal"),
    (15, 12, "Normal"),
    (12, 8, "Normal"),
    (20, 15, "Normal"),
    (85, 90, "Threat"),
    (90, 80, "Threat"),
    (78, 95, "Threat"),
    (95, 100, "Threat")
]

# 1. Euclidean Distance Function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 2. KNN Classifier Algorithm
def predict_knn(train_data, test_point, k=3):
    distances = []
    for item in train_data:
        features = (item[0], item[1])
        dist = euclidean_distance(features, test_point)
        distances.append((dist, item[2]))
    
    # Sort distances in ascending order
    distances.sort(key=lambda x: x[0])
    
    # Select Top K Nearest Neighbors
    neighbors = distances[:k]
    
    # Majority Voting
    votes = {}
    for dist, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
        
    prediction = max(votes, key=votes.get)
    return prediction, neighbors

# 3. Test Traffic Ingestion & Classification
test_sample = (82, 88)  # High packet rate & payload
k_val = 3
prediction, k_neighbors = predict_knn(dataset, test_sample, k=k_val)

print(f"\n[+] Incoming Traffic Sample: Packet Rate = {test_sample[0]} pkts/s | Payload = {test_sample[1]} KB")
print(f"[+] K-Value Set: {k_val}")

print("\n[+] Top K Nearest Neighbors (Distance Calculations):")
print("-" * 55)
for dist, label in k_neighbors:
    print(f" -> Euclidean Distance: {dist:<6.2f} | Category: {label}")
print("-" * 55)

print(f"\n[🚀 Classification Result]: Traffic Identified As -> [{prediction.upper()}]")
