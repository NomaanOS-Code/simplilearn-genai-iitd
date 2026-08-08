import math

print("="*60)
print("  NomaanOS - Pure Python K-Means Clustering Engine")
print("="*60)

# Unlabeled Dataset: System Activity Metrics (CPU Usage %, Memory Usage MB)
dataset = [
    [12, 120], [15, 140], [18, 130],  # Cluster A: Low System Load (Idle/Normal)
    [85, 820], [90, 890], [78, 810],  # Cluster B: High Resource Spike (Anomaly/Crypto Miner)
    [45, 450], [50, 480], [52, 430]   # Cluster C: Medium Workload (Standard Tasks)
]

# 1. Euclidean Distance Calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 2. K-Means Algorithm Implementation
def kmeans(data, k=3, max_iters=10):
    # Initial Centroids (Pick first K points)
    centroids = [data[i][:] for i in range(k)]
    
    for iteration in range(max_iters):
        clusters = [[] for _ in range(k)]
        
        # Assign points to nearest centroid
        for point in data:
            distances = [distance(point, c) for c in centroids]
            nearest_idx = distances.index(min(distances))
            clusters[nearest_idx].append(point)
            
        # Recalculate Centroids (Mean of assigned points)
        new_centroids = []
        for cluster in clusters:
            if not cluster:
                continue
            mean_x = sum(p[0] for p in cluster) / len(cluster)
            mean_y = sum(p[1] for p in cluster) / len(cluster)
            new_centroids.append([mean_x, mean_y])
            
        centroids = new_centroids
        
    return centroids, clusters

# 3. Cluster Computation
K = 3
final_centroids, final_clusters = kmeans(dataset, k=K)

print(f"\n[+] Total Data Points Ingested: {len(dataset)}")
print(f"[+] K-Clusters Configured: {K}")

print("\n[+] Computed Cluster Groupings & Centroids:")
print("-" * 55)
for idx, (centroid, cluster) in enumerate(zip(final_centroids, final_clusters), start=1):
    print(f" -> Cluster #{idx} Centroid (Avg CPU %, Mem MB): [{centroid[0]:.1f}, {centroid[1]:.1f}]")
    print(f"    Assigned Nodes ({len(cluster)}): {cluster}")
print("-" * 55)

print("\n[🚀 Anomaly Detection Rule]: Cluster with highest resource coordinates flagged for audit.")
