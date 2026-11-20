# AI & ML Task 1: Build & Evaluate a Linear Regression Model (House Price Predictor)

Introduces the full ML workflow on the **California Housing** dataset: data loading, exploration, preprocessing, training, evaluation (MAE, RMSE, R²) and reporting.

## Deliverables checklist
| Item | File | Created by |
|---|---|---|
| 1. Jupyter notebook (code, plots, comments) | `task1_ml_linear_regression.ipynb` | included |
| 2. Short PDF report, 2-4 pages (EDA, model, metrics, improvement ideas) | `Task1_Linear_Regression_Report.pdf` | running the notebook (last section) |
| 3. *Optional:* saved model pickle | `models/linear_regression_model.pkl` (+ `improved_model.pkl`) | running the notebook |
| 3. *Optional:* small UI script to predict on new inputs | `app.py` (Streamlit) and `predict.py` (command line) | included |

## How to run (about 2 minutes)
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook task1_ml_linear_regression.ipynb       # Kernel -> Restart & Run All
```
The first run needs internet once to download the dataset (a CSV copy is saved in `data/`). Save the notebook **with outputs** before submitting.

After the notebook has run:
```bash
python predict.py --MedInc 5.0 --Latitude 37.8 --Longitude -122.3     # command-line prediction
streamlit run app.py                                                  # small web UI
```

## What the notebook covers
Setup, load data, data overview, EDA (target distribution, feature distributions, outliers, correlations, income vs price, geography), train/test split (80/20, `random_state=42`), a `StandardScaler` + `LinearRegression` pipeline (no data leakage), MAE / RMSE / R² on train and test plus 5-fold cross-validation, diagnostics (actual vs predicted, residuals, coefficients), improvement experiments (feature engineering, Ridge, a non-linear reference), saving and reloading the model, and the PDF report.

## Files
```
task1_ml_linear_regression.ipynb   main notebook
housing_utils.py                   feature engineering + metrics (needed to load the saved models)
generate_report.py                 builds the PDF from results.json and figures/
predict.py                         command-line predictor
app.py                             Streamlit UI
requirements.txt
```
Created when you run the notebook: `figures/`, `models/`, `data/`, `results.json`, `Task1_Linear_Regression_Report.pdf`.

## Troubleshooting
| Problem | Fix |
|---|---|
| Dataset download fails | connect to the internet once; afterwards `data/california_housing.csv` is used |
| `ModuleNotFoundError: housing_utils` | run Jupyter and the scripts from this folder |
| `predict.py` says the model is missing | run the notebook first |
| PDF not created | make sure the last notebook cell ran, or run `python generate_report.py` afterwards |

## Limitations
1990 census block-group averages and a price capped at $500,000. This is a learning project, not a valuation tool.
