# Stage 13 Homework - Prediction API

TODO: two sentences on what the model does.

## Running it

    python app.py

The server starts on http://127.0.0.1:5000 and loads model/model.pkl at startup.

## POST /predict

    curl -X POST http://127.0.0.1:5000/predict \
         -H "Content-Type: application/json" \
         -d "{\"features\": [0.1, 0.2]}"

Response: 200 {"prediction":23.58961171297328}

## GET /predict/<f1>/<f2>

    curl http://127.0.0.1:5000/predict/0.1/0.2

Response: 200 {"prediction":23.58961171297328}

## Bad input
400 {"error":"Path parameters must be numbers"}
