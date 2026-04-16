# DAY 11: ENSEMBLE LEARNING

## Objective
The objective of this experiment is to improve model accuracy and stability by using Ensemble Learning. Specifically, a Random Forest Regressor is implemented and compared with a Linear Regression model to analyze performance improvement.

## Methodology
- The California Housing dataset was used for this experiment. 
- The data was divided into training and testing sets. A Random Forest Regressor was trained using multiple decision trees, where each tree learns from a different subset of the data.
- The model performance was evaluated using the R² (R-squared) score. 
- Additionally, Feature Importance was analyzed to identify which features have the most impact on predictions.

## Model Comparison
- Linear Regression R² Score: 0.58
- Random Forest R² Score: 0.7727

The Random Forest model achieved a higher R² score compared to Linear Regression, indicating better predictive performance. 
While Linear Regression explains about 58% of the variance in the data, Random Forest explains approximately 77.27%, making it more accurate and reliable for this dataset. 
This significant improvement is because Random Forest can capture complex and non-linear relationships in the data, whereas Linear Regression assumes a simple linear relationship between features and the target variable.

## Feature Importance Analysis
The Feature Importance plot showed that Median Income (MedInc) is the most important feature influencing house prices. Other important features include Average Occupancy, Latitude, and Longitude. Features like House Age have comparatively lower importance. This indicates that economic and location-based factors play a more significant role in predicting housing prices.

## Conclusion
The Random Forest model provides better accuracy and stability compared to Linear Regression. The experiment also shows that there is a trade-off between model performance and training time. Increasing the number of trees beyond a certain limit leads to diminishing returns.

Therefore, choosing an optimal number of trees is important to achieve a balance between accuracy and efficiency.