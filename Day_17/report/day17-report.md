# DAY 17 REPORT: Hyperparameter Tuning using GridSearchCV

## Objective
The objective of this task was to improve the performance of a machine learning model by optimizing its hyperparameters using GridSearchCV. Instead of manually selecting parameters, an automated search was performed to find the most effective combination that maximizes model accuracy.

## Approach
The Breast Cancer dataset from sklearn was used for this experiment. A Random Forest Classifier was selected as the base model due to its reliability and strong performance in classification tasks. Initially, a baseline model was evaluated using cross-validation to understand the default performance.

A parameter grid was then defined, including different values for the number of estimators, maximum depth, and minimum samples required for splitting. GridSearchCV was applied with 3-fold cross-validation, which systematically tested every possible combination of these parameters and evaluated their performance.

## Results and Analysis
The GridSearch process evaluated 27 different parameter combinations, resulting in a total of 81 model fits due to cross-validation. The best-performing configuration was identified as a model with no restriction on depth, minimum split of 2, and 50 estimators. This configuration achieved a cross-validation accuracy of 0.9631.

When compared with the baseline model, the tuned model showed improved performance, demonstrating the effectiveness of hyperparameter tuning. However, it was also observed that increasing the search space leads to higher computational cost, highlighting a trade-off between accuracy and training time.

## Model Persistence
The final optimized model was saved using joblib, allowing it to be reused without retraining. This is an important step in building production-ready machine learning systems.

## Key Learning and Reflection
GridSearchCV evaluates every possible combination of parameters, which can become computationally expensive. For example, with 5 parameters and 10 options each, it would test 100,000 combinations, and with 3-fold cross-validation, this results in 300,000 model trainings. Due to this, RandomizedSearchCV is often preferred for large datasets, as it reduces computation time by testing only a subset of combinations while still achieving near-optimal results.

## Conclusion
This task highlighted the importance of hyperparameter tuning in improving model performance. GridSearchCV provided a structured approach to optimization, ensuring better accuracy and generalization. At the same time, it emphasized the need to balance performance gains with computational efficiency in real-world applications.