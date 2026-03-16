from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("loan_model.pkl")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([{
        "monthly_income": data["monthly_income"],
        "loan_amount": data["loan_amount"],
        "debt_to_income_ratio": data["debt_to_income_ratio"],
        "previous_defaults": data["previous_defaults"],
        "account_balance": data["account_balance"]
    }])

    probability = model.predict_proba(df)[0][1]

    if probability >= 0.6:
        decision = "APPROVE"
    elif probability >= 0.5:
        decision = "REVIEW"
    else:
        decision = "REJECT"

    return jsonify({
        "repayment_probability": probability,
        "decision": decision
    })

if __name__ == "__main__":
    app.run(debug=True)