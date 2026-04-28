# DAY 19: DIMENSIONALITY REDUCTION (PCA)

## Objective:
Implemented Principal Component Analysis (PCA) to reduce high-dimensional data, analyze retained variance, visualize compressed datasets, and benchmark performance improvements in machine learning model training.

## Key Tasks Completed:
    1. PCA Dimensionality Reduction
        - Loaded the Digits dataset containing 64 features.
        - Reduced the dataset from 64 dimensions to 2 principal components.
        - Visualized the compressed data using a 2D scatter plot.

    2. Explained Variance Analysis
        - Calculated the Explained Variance Ratio.
        - Measured how much original information was retained after dimensionality reduction.
        - Determined the number of components required to preserve 95% of total variance.

    3. Scree Plot Generation
        - Generated cumulative variance graph.
        - Identified optimal PCA component count for production-level compression.

    4. Performance Benchmarking
        - Trained Logistic Regression on original 64-dimensional data.
        - Trained Logistic Regression on PCA-reduced data retaining 95% variance.
        - Compared training times to evaluate speed improvements.

## Key Learnings:
- PCA reduces computational complexity while preserving important patterns.
- Lower dimensions improve model speed and scalability.
- PCA is highly useful for preprocessing before clustering or classification.
- Dimensionality reduction enhances end-user experience by enabling faster recommendations and analytics.

## Conclusion:
Day 19 demonstrated how PCA improves machine learning efficiency by compressing large feature spaces, optimizing model performance, and supporting scalable real-world applications.
