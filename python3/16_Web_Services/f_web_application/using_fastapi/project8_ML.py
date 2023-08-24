"""
Purpose: FastAPI app for ML
"""

import fastapi
from fastapi.responses import JSONResponse
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

app = fastapi.FastAPI()


@app.post("/predict")
def predict_flower(data: dict):
    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    ]
    prediction = model.predict([features])
    return JSONResponse({"prediction": str(prediction[0])})


"""
# CMD: python -m uvicorn project5_ML:app --reload

testing

curl -X POST -H "Content-Type: application/json" -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}' http://localhost:8000/predict

"""
