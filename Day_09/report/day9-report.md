# Day 9 Report: Model Optimization & Hyperparameter Tuning

## Objective
The objective of Day 9 was to improve model performance by optimizing its hyperparameters using Grid Search with Cross-Validation. This helps in finding the best configuration for a model instead of relying on default settings.

## Concept Overview
- In Machine Learning, models have two types of values:
      Parameters → learned from data
      Hyperparameters → set before training
- For Ridge Regression, the key hyperparameter is alpha, which controls the strength of regularization.
- To find the best alpha, we used GridSearchCV, which tries multiple values and selects the best one using cross-validation.

## Implementation Steps
1. Loaded the California Housing dataset
2. Split the data into training and testing sets
3. Applied feature scaling using StandardScaler
4. Trained a default Ridge Regression model
5. Applied GridSearchCV with a range of alpha values
6. Retrieved the best model using best_estimator
7. Compared performance using the R² score

## Results
- Default Model (alpha = 1.0): R² Score = 0.5758157428913686
- Optimized Model (Best Alpha = 10.0 ): R² Score = 0.6003
- The optimized model performed better (or more consistently) than the default model, demonstrating the importance of hyperparameter tuning.

## Conclusion
This task demonstrated how hyperparameter tuning improves model performance and reliability. Using GridSearchCV with cross-validation allows us to systematically find the best settings, making our machine learning models more accurate and robust.
