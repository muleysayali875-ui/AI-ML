# DAY 15: K-MEANS CLUSTERING

## Objective
The objective of this task was to explore unsupervised learning by implementing the K-Means clustering algorithm to identify hidden patterns in unlabeled data. Unlike supervised learning, clustering helps group similar data points based on their characteristics without predefined labels.

## Methodology
1. Data Preparation
- A synthetic dataset was generated using make_blobs, representing user behavior patterns. The dataset contained multiple clusters to simulate real-world segmentation.

2. Feature Scaling
- Before applying K-Means, the dataset was standardized using StandardScaler. This step ensures that all features contribute equally to distance calculations, which is crucial because K-Means relies on distance metrics.

3. Elbow Method for Optimal K
- To determine the optimal number of clusters (K), the Elbow Method was used.
- The Within-Cluster Sum of Squares (WCSS) was calculated for K values from 1 to 10.
A graph was plotted between K and WCSS.
The “elbow point,” where the decrease in WCSS slows down, indicated the optimal number of clusters.
- Observation: The elbow was observed at K = 5, which was selected as the optimal number of clusters.

4. Applying K-Means Clustering
- The K-Means algorithm was applied with:
    - n_clusters = 5
    - init = 'k-means++'
The model assigned each data point to a cluster and calculated cluster centroids.

5. Visualization of Clusters
A scatter plot was created to visualize:
    - Different clusters using distinct colors
    - Cluster centroids marked clearly
This visualization represents how users are grouped based on similarity.

6. Stability Test
The K-Means model was run multiple times using different initialization methods:
    - init = 'random'
    - init = 'k-means++'
Observation:
- The random initialization produced slightly varying cluster centers across runs.
- The k-means++ initialization produced more stable and consistent results.

## Key Concepts Learned
- Unsupervised learning identifies hidden patterns in data without using labeled outputs.
- K-Means clustering groups similar data points based on distance.
- The Elbow Method helps determine the optimal number of clusters (K).
- Feature scaling is essential to ensure all features contribute equally to clustering.
- K-Means minimizes the distance between data points and their respective cluster centroids.
- The k-means++ method improves clustering by selecting better initial centroids.
- Random initialization can lead to inconsistent clustering results.
- Clustering is useful for user segmentation and personalized recommendations.

## Conclusion
This task demonstrated how clustering can be used to uncover hidden user segments without labeled data. By applying the Elbow Method and K-Means algorithm, meaningful groupings were identified and visualized. The experiment also highlighted the importance of proper initialization and feature scaling in achieving stable and accurate clustering results.

