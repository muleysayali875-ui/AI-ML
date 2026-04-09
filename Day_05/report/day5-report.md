# DAY 5: THE FIRST PREDICTION

## Objectives
Today's task was to understand how a machine learning model learns the relationship between input features and target values, and to evaluate its performance using appropriate metrics.

## Methodology

A dataset representing study hours and corresponding exam scores was used for model training and evaluation. The workflow followed these steps:

1. Data Splitting
    - The dataset was divided into training (80%) and testing (20%) sets using train_test_split. This ensured that the model was evaluated on unseen data, promoting generalization rather than memorization.

2. Model Implementation
    - A Linear Regression model was implemented using the sklearn.linear_model library. The model was trained using the training dataset through the fit() method, enabling it to learn the relationship between hours studied and exam scores.    

3. Prediction
    - The trained model was used to generate predictions on the test dataset. Additionally, a prediction was made for a new input value (11 hours) to verify the model’s ability to handle unseen data.

4. Model Evaluation
    - The model’s performance was assessed using:
        - Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values.
        - R-squared (R²) Score: Indicates how well the model fits the data, with values closer to 1 representing better performance.

5. Visualization
    - A graphical representation was created using Matplotlib, where the actual data points and the regression line were plotted to visually assess the model’s fit.

## Results and Observations
The regression line closely aligned with the data points, indicating that the model successfully captured the underlying linear relationship. The evaluation metrics reflected strong performance, with a low error value and a high R² score, confirming the model’s effectiveness.

## Conclusion
The task successfully demonstrated the complete workflow of building a basic machine learning model, from data splitting to training, prediction, and evaluation. The Linear Regression model effectively learned the relationship between study hours and exam scores and produced reliable predictions.