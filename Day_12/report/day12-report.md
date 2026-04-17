# DAY 12: BINARY CLASSIFICATION

## Objective
The objective of this task was to understand Binary Classification and implement a Logistic Regression model to classify tumors as Malignant or Benign using probability-based predictions.

## Tasks Performed
- Loaded the Breast Cancer dataset using sklearn.datasets
- Split the dataset into training and testing sets
- Applied feature scaling using StandardScaler
- Trained a Logistic Regression model on scaled data
- Made predictions using the trained model
- Evaluated model performance using accuracy score
- Visualized results using a Confusion Matrix heatmap
- Used predict_proba() to analyze class probabilities

## Results
- Achieved a model accuracy of over 90%, indicating strong performance.
- Successfully visualized model predictions using a Confusion Matrix to analyze correct and incorrect classifications.
- Observed how class probabilities influence the final prediction, providing insight into the model’s confidence levels.

## Key Concepts Learned
- Logistic Regression is used for classification, not regression
- The Sigmoid function converts outputs into probabilities (0 to 1)
- Difference between:
    - Class Prediction → Final output (0 or 1)
    - Class Probability → Confidence of prediction
- Importance of feature scaling in Logistic Regression
- Confusion Matrix helps analyze model errors beyond accuracy

## Conclusion
Logistic Regression is an effective baseline model for binary classification tasks. It not only predicts the class but also provides probability estimates, helping in better understanding and decision-making, especially in critical applications like medical diagnosis.