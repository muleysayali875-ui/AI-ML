# Day 20: End-to-End Pipelines and Model Deployment

## Objective:
To transform a machine learning model from a research script into a production-ready service by building an integrated sklearn Pipeline, serializing it, and deploying it through a Flask REST API for real-time predictions.

## Implementation:
- Loaded and split the California Housing dataset
- Built an sklearn Pipeline combining:
    - StandardScaler for preprocessing
    - RandomForestRegressor for prediction
- Trained the pipeline on training data
- Serialized the complete pipeline using Joblib into production_model.pkl
- Developed a Flask API with a /predict endpoint
- Accepted JSON input and returned predictions in real time
- Created a separate test_api.py script using requests library to verify API functionality

## Outcome:
- Successfully deployed a production-ready ML model
- Enabled real-time system integration for backend services
- Verified API predictions through POST request testing
- Improved deployment reliability by combining scaler and model into one unified Pipeline

## Key Learning:
Using a single Pipeline object ensures consistent preprocessing, reduces deployment complexity, prevents integration errors, and allows seamless collaboration with Backend, Data Analyst, and DevOps teams.

## Conclusion:
This task helped convert a machine learning model into a production-ready service by using a Pipeline and Flask API. It improved reliability, simplified deployment, and enabled smooth integration with other engineering teams for real-time use.