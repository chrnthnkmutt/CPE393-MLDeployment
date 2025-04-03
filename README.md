# mldeployment-cpe393

## Project Description

This project demonstrates the deployment of a machine learning model using Flask and Docker. The model is trained to predict housing prices based on various features. The API provides endpoints for making predictions, checking the health of the service, and more.

## Setup Steps

1. Train the model by running `train.py`. This will save `housing_model.pkl` in the `app` folder.
2. Navigate to the project directory in the terminal:
   ```sh
   cd ml-docker-deploy
   ```
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
     -d '{"features": [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]}'
```

#### Response
```json
{
  "predictions": [0, 2],
  "confidences": [0.97, 0.85]
}
```

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
