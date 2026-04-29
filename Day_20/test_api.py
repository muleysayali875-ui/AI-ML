import requests

# Sample California housing feature payload
sample_data = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.02381,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}

# Send POST request to Flask API
response = requests.post(
    'http://127.0.0.1:5000/predict',
    json=sample_data
)

# Print prediction result
print("Prediction Response:")
print(response.json())