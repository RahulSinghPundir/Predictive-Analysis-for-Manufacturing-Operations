# Predictive Analysis for Manufacturing Operations

This project implements model for predicting machine downtime or production defects using a manufacturing dataset. It also includes a Streamlit-based user interface for inputting data and viewing predictions. The goal is to assist decision-making in manufacturing by leveraging machine learning models.

---

## Features

1. **Endpoints**:
   - **Prediction Endpoint**: Makes predictions for machine downtime or failure based on input parameters.

2. **Streamlit UI**:
   - Allows users to input data directly into an editable DataFrame.
   - Displays predictions along with confidence scores.

3. **Machine Learning**:
   - Trained on manufacturing-related data with features such as `Hydraulic_Pressure(bar)`, `Spindle_Speed(RPM)`, `Torque(Nm)`, and `Cutting(kN)`.
   - Predicts whether downtime will occur (`1` for failure, `0` for success).
   - Saves the best model for inference.

---


## Streamlit UI

The Streamlit app allows users to:

1. Input manufacturing parameters into an editable DataFrame.
2. Trigger predictions for all rows in the DataFrame.
3. View results for each input row, including:
   - Downtime status ("Success" or "Failure").
   - Confidence score.

### How to Run the Streamlit App

Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Example Workflow

1. Open the Streamlit app.
2. Input machine parameters into the DataFrame.
3. Click "Predict" to get predictions for each input row.
4. View the downtime prediction and confidence score for each input.

---

## Machine Learning Details

- **Model Used**: Logistic Regression or Decision Tree (best model chosen based on performance).
- **Features**:
  - `Hydraulic_Pressure(bar)`
  - `Spindle_Speed(RPM)`
  - `Torque(Nm)`
  - `Cutting(kN)`
- **Target**: `Downtime_Machine_Failure` (1 for failure, 0 for success).

---

## Notes

- Test the endpoints using tools like Postman or cURL.
- Modify `BASE_URL` in `app.py` to match the API's host and port if necessary.

