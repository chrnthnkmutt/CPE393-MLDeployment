# mldeployment-cpe393

Created By Charunthon Limseelo (65070503410).

Advisior: Prof. Aye Hninn Khine (The Course Instructor of CPE393 Special Topics III: Machine Learning Operations)

## Project Description

This project demonstrates the deployment of a machine learning model using Flask and Docker. The model is trained to predict housing prices based on various features. The API provides endpoints for making predictions, checking the health of the service, and more.

## Setup Steps

1. Train the model by running `train.py`. This will save `linear_model.pkl` in the `app` folder.
2. Navigate to the project directory in the terminal:
3. Build the Docker image:
   ```sh
   docker build -t ml-model .
   ```
4. Run the Docker container:
   ```sh
   docker run -p 9000:9000 ml-model
   ```

## Sample API Requests and Responses

### Predict Endpoint

#### Request
```sh
curl -X POST http://localhost:9000/predict \
   -H "Content-Type: application/json" \
   -d '{ "features": [ [5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3] ] }'
```

#### Example Response
```json
{
  "confidences":[1.0,1.0],
  "predictions":[0,2]
}
```

> Note: Confidences and Predictions values are swapped in the response. The first value in the `predictions` array corresponds to the first value in the `confidences` array, and so on.

### Health Check Endpoint

#### Request
```sh
curl -X GET http://localhost:9000/health
```

#### Response
```json
{
  "status": "ok"
}
```
