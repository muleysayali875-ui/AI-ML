# DAY 6: THE BINARY DECISION

## Objective
To build a binary classification model using Logistic Regression to predict whether a student will Pass (1) or Fail (0) based on input features.

## Tasks Performed
    1. Logistic Regression Model
        - Created a dataset with features:
            Hours of Sleep
            Coffee Consumption
        - Defined:
            Features (X)
            Target (y)
        - Split data into training and testing sets
        - Trained the model using Logistic Regression
        - Generated predictions on test data

    2. Confusion Matrix
        - Computed confusion matrix to evaluate model performance
        - Visualized it using a heatmap
        - Analyzed:
            True Positives (TP)
            True Negatives (TN)
            False Positives (FP)
            False Negatives (FN)

    3. Classification Report
        - Generated classification metrics:
            Precision
            Recall
            F1-score
            Accuracy
        - Used these metrics to evaluate model reliability

    4. Feature Importance
        - Extracted model coefficients
        - Determined impact of each feature:
            Sleep positively influences passing
            Higher coffee consumption negatively influences passing

    5. Manual Prediction
        - Tested model with custom input:
            Hours_Sleep = 3, Coffee_Cups = 7
        - Model predicted: Fail (0)

    Experiment (Jupyter Notebook)
        - Performed manual prediction using the trained model
        - Reflected on classification errors
        Conclusion: False Negative is more dangerous in critical applications like cancer detection, as it may lead to missed diagnosis and delayed treatment.

## Key Learning Outcomes
    - Understood difference between regression and classification
    - Learned working of Logistic Regression and probability-based prediction
    - Gained knowledge of evaluation metrics beyond accuracy
    - Understood importance of Confusion Matrix in model evaluation

## Conclusion
Successfully implemented a Logistic Regression model and evaluated its performance using classification metrics. The model was able to distinguish between Pass and Fail scenarios and was validated using both test data and manual input.