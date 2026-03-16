# Loan Approval Predictor

This is a simple web-based loan approval predictor built with **Python (Flask)** and **scikit-learn**.  
It predicts whether a loan should be approved, reviewed, or rejected based on user inputs.

## Features

- Takes key inputs: monthly income, loan amount, debt-to-income ratio, previous defaults, account balance.
- Calculates repayment probability and gives decision: APPROVE / REVIEW / REJECT.
- Simple front-end with HTML form.
- Uses a pre-trained Random Forest model (`loan_model.pkl`).

## How to Run Locally

1. Clone the repository:

```bash
git clone <your-repo-url>
cd loan_project
