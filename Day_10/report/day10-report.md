# DAY 10: COMPLEX RELATIONSHIPS

## Objectives
The objective of this task was to understand how to model non-linear relationships in data and compare different approaches such as Polynomial Regression and Decision Tree Regression. Additionally, the task focused on understanding overfitting and how model complexity affects performance.

## Polynomial Regression (Curved Model)
- In this section, Polynomial Features were used to extend a simple linear model by including higher-degree terms such as (X^2).
- This transformation allowed the Linear Regression model to fit a curved pattern instead of a straight line.
- As a result, the model was able to capture the underlying trend in the data more effectively, producing a smooth curve that represents the general relationship between the input and output variables.

## Decision Tree Regression (Step-like Model)
- A Decision Tree Regressor was implemented to model the same dataset. 
- Unlike Polynomial Regression, the Decision Tree does not generate a continuous curve. Instead, it divides the data into smaller regions and assigns constant values within each region.
- This results in a step-like prediction pattern. While this approach can fit data more flexibly, it can also lead to overly complex models if not properly controlled.

## Overfitting Analysis (Depth Experiment)
To study overfitting, multiple Decision Tree models were trained with different values of max_depth:
    - Depth = 2: The model was too simple and failed to capture the underlying pattern (underfitting).
    - Depth = 5: The model achieved a reasonable balance between simplicity and accuracy.
    - Depth = 20: The model became highly complex and started fitting noise in the data, resulting in a jagged and irregular prediction pattern (overfitting).
This experiment demonstrated that increasing model complexity can reduce training error but may harm the model’s ability to generalize to new data.

## Model Comparison
A comparison was made between Polynomial Regression and Decision Tree Regression using a combined plot.
    - Polynomial Regression produced a smooth and continuous curve, capturing the overall trend of the data.
    - Decision Tree Regression produced a step-like curve, approximating the data through discrete splits.
This comparison highlighted the difference in how these models learn patterns from the same dataset.

## R² Score Evaluation
R² scores were used to evaluate model performance:
    - Polynomial Regression achieved an R² score of 0.853, indicating a good balance between fitting the data and generalizing well.
    - Decision Tree (depth = 2) achieved 0.813, showing underfitting due to low complexity.
    - Decision Tree (depth = 5) achieved 0.929, providing a better fit with moderate complexity.
    - Decision Tree (depth = 20) achieved 1.000, indicating a perfect fit on training data but clear overfitting.
These results demonstrate that while deeper trees can achieve higher R² scores, they may not generalize well. Therefore, a higher R² score does not always indicate a better model when overfitting is present.

## Conclusion
This task emphasized the importance of selecting appropriate models for non-linear data and controlling model complexity. Polynomial Regression is effective for capturing smooth patterns, while Decision Trees offer flexibility but require careful tuning to prevent overfitting.
Understanding the balance between model accuracy and generalization is essential for building robust and reliable machine learning models.