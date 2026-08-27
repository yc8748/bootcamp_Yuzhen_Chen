
from flask import Flask, request, jsonify
import joblib

# loaded ONCE, at startup - not inside a route
model = joblib.load('model/model.pkl')
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict_post():
    data = request.get_json(silent=True) or {}
    features = data.get('features')
    # TODO 1: return jsonify({'error': ...}), 400 if features is missing
    #         or does not have exactly 2 values
    if features is None:
        return jsonify({'error': 'Missing "features" key in JSON body'}), 400
    if not isinstance(features, list) or len(features) != 2:
        return jsonify({'error': 'Features must be a list of exactly 2 numbers'}), 400
    try:
        features = [float(x) for x in features]
    except (ValueError, TypeError):
        return jsonify({'error': 'Features must be numbers'}), 400
    # TODO 2: otherwise predict and return jsonify({'prediction': <the number>})
    #         remember model.predict takes a LIST of rows: model.predict([features])
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})


@app.route('/predict/<f1>/<f2>', methods=['GET'])
def predict_get(f1, f2):
    # TODO 3: f1 and f2 arrive as STRINGS. Convert them to float, and return
    #         jsonify({'error': ...}), 400 if either one is not a number.
    #         Then predict with the same `model` above and return the same JSON
    #         shape as /predict does.
    try:
        f1_float = float(f1)
        f2_float = float(f2)
    except ValueError:
        return jsonify({'error': 'Path parameters must be numbers'}), 400
    
    prediction = model.predict([[f1_float, f2_float]])[0]
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(port=5000)
