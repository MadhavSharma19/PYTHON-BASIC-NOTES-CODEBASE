from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
 
# Find optimal K (Elbow Method)
inertias = []
K_range = range(2, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)
plt.plot(K_range, inertias, marker='o')
plt.xlabel('K'); plt.ylabel('Inertia')
plt.title('Elbow Method'); plt.show()
 
# Train K-Means with chosen K
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)
print(f"Silhouette Score: {silhouette_score(X, clusters):.4f}")
 
# Visualize clusters (2D)
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=clusters, cmap='viridis', alpha=0.5)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, c='red')
plt.title('K-Means Clustering'); plt.show()
