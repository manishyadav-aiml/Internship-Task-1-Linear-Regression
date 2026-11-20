# AI & ML Task 1: Build & Evaluate a Linear Regression Model (House Price Predictor)

A complete Machine Learning workflow using the **California Housing Dataset** to predict house prices using Linear Regression.

This project covers data loading, exploratory data analysis (EDA), preprocessing, model training, evaluation, visualization, model comparison, and report generation.

---

## Deliverables Checklist

| No. | Deliverable | File |
|---|---|---|
| 1 | Jupyter Notebook with code, outputs, visualizations, and explanations | `task1_ml_linear_regression.ipynb` |
| 2 | PDF Report (2–4 pages) | `Task1_Linear_Regression_Report.pdf` |
| 3 | Trained Linear Regression Model | `models/linear_regression_model.pkl` |
| 4 | Improved Model | `models/improved_model.pkl` |
| 5 | Prediction Web Application | `app.py` |
| 6 | Command-Line Prediction Script | `predict.py` |

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Joblib

---

## Project Structure

```text
Task-1-Linear-Regression/
│
├── task1_ml_linear_regression.ipynb
├── Task1_Linear_Regression_Report.pdf
├── README.md
├── requirements.txt
├── housing_utils.py
├── generate_report.py
├── predict.py
├── app.py
├── results.json
│
├── data/
│   └── california_housing.csv
│
├── figures/
│   ├── target_distribution.png
│   ├── feature_distributions.png
│   ├── correlation_heatmap.png
│   ├── income_vs_price.png
│   ├── geographic_prices.png
│   ├── diagnostics.png
│   ├── coefficients.png
│   └── model_comparison.png
│
└── models/
    ├── linear_regression_model.pkl
    └── improved_model.pkl
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Task-1-Linear-Regression
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Launch Jupyter Notebook

```bash
python -m notebook task1_ml_linear_regression.ipynb
```

Open the notebook and select:

**Kernel → Restart Kernel and Run All Cells**

Save the notebook with all outputs after execution.

The first execution requires an internet connection to download the California Housing dataset. A local CSV copy is saved in the `data/` directory.

---

## Model Workflow

### 1. Data Loading and Exploration

- Load the California Housing dataset.
- Inspect dataset dimensions and structure.
- Analyze numerical features.
- Check missing values and data quality.

### 2. Exploratory Data Analysis (EDA)

- Target variable distribution.
- Feature distributions.
- Outlier analysis.
- Correlation heatmap.
- Income versus house price analysis.
- Geographic price distribution.

### 3. Data Preprocessing

- Train-test split (80:20).
- Feature scaling using StandardScaler.
- Pipeline implementation.
- Prevention of data leakage.

### 4. Model Training

- Linear Regression.
- Feature engineering experiments.
- Ridge Regression.
- Non-linear reference model.

### 5. Model Evaluation

Evaluate model performance using:

- Mean Absolute Error (MAE).
- Root Mean Squared Error (RMSE).
- R-squared (R²).
- Five-fold cross-validation.

### 6. Model Diagnostics

- Actual versus predicted values.
- Residual analysis.
- Feature coefficients.
- Model comparison.

### 7. Model Saving and Reporting

- Save trained models using Joblib.
- Reload and test saved models.
- Generate visualizations.
- Generate the final PDF report.

---

## Prediction

### Command-Line Prediction

Run:

```bash
python predict.py --MedInc 5.0 --Latitude 37.8 --Longitude -122.3
```

### Streamlit Web Application

Run:

```bash
streamlit run app.py
```

The application provides an interface for making house price predictions using the trained model.

---

## Generated Outputs

After successfully executing the notebook, the following files are generated:

| File | Description |
|---|---|
| `Task1_Linear_Regression_Report.pdf` | Final project report |
| `results.json` | Model evaluation results |
| `model_comparison.png` | Model comparison visualization |
| `linear_regression_model.pkl` | Saved Linear Regression model |
| `improved_model.pkl` | Saved improved model |
| `figures/` | EDA and model evaluation visualizations |
| `data/` | Downloaded dataset |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Dataset download fails | Check your internet connection and retry. |
| `ModuleNotFoundError: housing_utils` | Run the notebook and scripts from the project directory. |
| Prediction model is missing | Execute all notebook cells before running prediction scripts. |
| PDF report is not generated | Execute the final notebook cell or run `python generate_report.py`. |
| Missing Python dependencies | Run `python -m pip install -r requirements.txt`. |

---

## Limitations

- The dataset is based on 1990 California census block-group averages.
- The target variable is capped at $500,000.
- Predictions represent historical patterns and may not reflect current housing market conditions.
- Model performance depends on the quality and limitations of the dataset.

**Note:** This project is developed for educational and Machine Learning practice purposes. It is not intended to be used as a professional property valuation tool.

---

## Author

**Manish Kumar Yadav**

GitHub: [manishyadav-aiml](https://github.com/manishyadav-aiml)