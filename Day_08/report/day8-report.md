# DAY 8: THE END-TO-END PIPELINE

## Objective
The objective of this task was to build a complete machine learning pipeline using the California Housing dataset. This included data loading, preprocessing, model training, evaluation, and performance visualization.

## Steps Performed

    1. Data Loading
        - The California Housing dataset was successfully fetched and converted into a Pandas DataFrame for easier manipulation and analysis.

    2. Data Preprocessing
        - The dataset was divided into features (X) and target (y).
        - The data was split into training (80%) and testing (20%) sets using train_test_split.
        - StandardScaler was applied to normalize the feature values, ensuring all features are on a similar scale.

    3. Model Training
        - A Linear Regression model was trained using the scaled training data to learn the relationship between features and house prices.

    4. Prediction and Evaluation
        - Predictions were made on the test dataset.
        - Model performance was evaluated using:
            Mean Absolute Error (MAE): Measures the average prediction error in dollar terms.
            R-Squared Score (R²): Indicates how well the model explains the variance in the data.

    5. Residual Analysis
        - A residual plot was generated to visualize the difference between actual and predicted values. This helped in understanding the model’s performance and checking for patterns in errors.

## Key Observations
- Feature scaling improved the model’s performance by standardizing data.
- The Linear Regression model provided a reasonable prediction but may not capture complex patterns.
- Residual analysis is important to detect non-linear relationships in the dataset.

## Conclusion
The task successfully demonstrated the complete machine learning workflow, from data loading to evaluation. It highlighted the importance of preprocessing, model evaluation, and visualization in building effective machine learning models.

## Learning Outcome
- Understood how to build an end-to-end ML pipeline.
- Learned the importance of feature scaling.
- Gained knowledge of evaluation metrics like MAE and R².
- Understood how residual plots help in diagnosing model performance.