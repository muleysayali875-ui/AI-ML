# DAY 16: MODEL VALIDATION & K-FOLD

## Objective
The objective of this task was to move beyond a single train-test split and evaluate model performance using K-Fold Cross-Validation. The goal was to measure the model’s stability, detect overfitting or underfitting, and understand the importance of shuffling in creating reliable models.

## Implementation
1. K-Fold Cross-Validation
A Random Forest Classifier was applied to the handwritten digits dataset using 5-Fold Cross-Validation.
- Scores for each fold:
- 0.9333, 0.8944, 0.9415, 0.9666, 0.9220
- Mean Accuracy: 0.9316 (93.16%)
- Standard Deviation: 0.0237

## Model Evaluation
- Training Accuracy: 1.0000 (100%)
- Validation Accuracy: 0.9316 (93.16%)
Analysis:
The model shows slight overfitting, as the training accuracy is perfect while validation accuracy is slightly lower. However, the validation performance is still strong, indicating that the model generalizes well.

## Shuffle vs No Shuffle Experiment (10-Fold)
1. Without Shuffle
    - Mean Accuracy: 0.9532
    - Standard Deviation: 0.0245
2. With Shuffle
    - Mean Accuracy: 0.9733
    - Standard Deviation: 0.0074
Observation:
Shuffling significantly reduced the standard deviation and improved accuracy, making the model more stable and reliable.

## Key Concepts Learned
- K-Fold Cross-Validation provides a more reliable estimate than a single train-test split.
- Mean accuracy reflects overall performance, while standard deviation measures stability.
- A low standard deviation indicates consistent model performance.
- Overfitting occurs when training accuracy is much higher than validation accuracy.
- Shuffling ensures better data distribution across folds, reducing bias and improving generalization.

## Conclusion
The model achieved high accuracy with low variance, indicating strong and stable performance. Although slight overfitting was observed, the model still generalizes well. The shuffle experiment demonstrated that proper data distribution is critical for building reliable machine learning systems.