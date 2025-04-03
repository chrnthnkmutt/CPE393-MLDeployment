from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Input validation
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key"}), 400

    features = data["features"]
    if not isinstance(features, list) or not all(isinstance(i, list) and len(i) == 4 and all(isinstance(j, (int, float)) for j in i) for i in features):
        return jsonify({"error": "Invalid input format. 'features' must be a list of lists with 4 float values each."}), 400

    input_features = np.array(features)
    predictions = model.predict(input_features)
    confidences = model.predict_proba(input_features).max(axis=1)

    return jsonify({"predictions": predictions.tolist(), "confidences": confidences.tolist()})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
