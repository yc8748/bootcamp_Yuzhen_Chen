
# Stock Price Analysis & Feature Engineering Pipeline

## Framing Worksheet 

### Problem Statement
The project aims to analyze historical stock price data for AAPL to understand market behavior, identify patterns, and engineer features that can support future predictive modeling. The focus is on assessing whether current market conditions present favorable risk-return characteristics for continued capital deployment over the next 12 months.

### Stakeholder & User
- **Decision owner:** Product Manager (PM)
- **Tool/operator:** Quantitative Team
- **End User:** Investment Committee / Portfolio Managers

### Useful Answer
- **Descriptive / Predictive / Causal:** Descriptive (understanding historical patterns) and Predictive (forecasting price trends and volatility)
- **Metric or artifact:** Price trends, volatility profiles, correlation matrices, feature importance, model performance metrics (R², MAE), Sharpe Ratio, Maximum Drawdown

### Assumptions & Constraints
- **Assumptions:**
  - Historical price data (Yahoo Finance) is reliable and accurately reflects market activity
  - Stock returns follow an approximately normal distribution (Z-score method assumption)
  - Daily trading volumes reflect genuine market participation
  - Rolling averages (7-day, 30-day) effectively indicate market sentiment
  - Linear relationship exists between opening and closing prices (regression analysis)
  
- **Constraints:**
  - Data limited to 12 months (251 trading days)
  - No access to fundamental data (earnings, P/E ratios, etc.)
  - No transaction cost or liquidity constraints modeled
  - Single-stock analysis (AAPL only) limits generalizability

### Known Unknowns / Risks
- **Future market volatility is unknown** - Past performance does not guarantee future results
- **Assumed transaction costs diverge from reality** - No bid-ask spread or slippage modeled
- **External shocks** - Macroeconomic events, regulatory changes, or company-specific news could disrupt established trends
- **Normality assumption may fail** - During volatile periods, price distributions can deviate significantly from normal
- **Z-score sensitivity** - Method may miss subtle but meaningful anomalies within 3σ range
- **Data limitations** - Price-only analysis misses sentiment, fundamental, and alternative data signals

### Lifecycle Mapping
| Goal | Stage | Deliverable |
| :--- | :--- | :--- |
| Define success criteria & scope | Stages 1: Problem Framing & Scoping | README + Stakeholder Memo |
| Create environment | Stages 2-3: Tooling Setup | Environment specification, `.env.example`, dependency file, and project scaffold |
| Acquire & store data | Stages 4-5: Data Acquisition & Storage | Raw CSV files in `data/raw/` |
| Clean & preprocess data | Stage 6: Data Preprocessing | Cleaned & normalized datasets in `data/processed/` |
| Detect & assess outliers | Stage 7: Outlier Detection | Outlier flags, sensitivity analysis, regression comparisons |
| Explore & understand data | Stage 8: EDA | Distribution plots, correlation matrices, time series visualizations |
| Engineer predictive features | Stage 9: Feature Engineering | Feature-rich dataset for modeling |
| Model & evaluate | Stage 10: Model Regression | Predictive models, performance metrics, recommendations |

---

## Data Pipeline (Stages 4, 5 & 6): Acquisition, Storage & Preprocessing

### 1. Data Acquisition
The pipeline pulls historical daily OHLCV (Open, High, Low, Close, Volume) data for Apple (AAPL) using the `yfinance` library.
- **Source:** Yahoo Finance
- **Period:** 12 months
- **Interval:** Daily
- **Fallback Logic:** The script checks for an existing CSV file in the `data/raw` directory before making a new API call.

**Validation Results:**
```python
{
    'missing': [],                    # No missing columns
    'shape': (251, 6),                # 251 trading days
    'na_total': 0,                    # No missing values
    'price_above_0': True             # All prices positive
}
```

### 2. Data Storage
- **Raw Data:** Stored in `data/raw/` with a timestamped filename (e.g., `api_source-yfinace_symbol-AAPL_20260827.csv`).
- **Processed Data:** Saved in `data/processed/` after cleaning and normalization (`cleaned_data_YYYYMMDD.csv`, `normalized_data_YYYYMMDD.csv`).
- **Feature Data:** Saved in `data/processed/` (`featured_data_YYYYMMDD.csv`).

### 3. Data Preprocessing
Raw data is processed to ensure quality and consistency.
- **Cleaning:** Missing values are imputed using the median strategy via `fill_missing_median()`, and columns with high missing rates are dropped using `drop_missing()`.
- **Normalization:** Numeric columns (close, high, low, open, volume) are scaled to a [0, 1] range using `normalize_data()` to prepare for machine learning models.

---

## Stage 7: Outlier Detection & Sensitivity Analysis
Outliers are identified and analyzed to understand their impact on model performance.

### 1. Methodology
- **Z-Score Method:** Applied to the `open` price column with a threshold of 3.0, assuming a roughly normal distribution.
- **IQR Method:** Applied as a secondary check using the interquartile range (k=1.5).
- **Winsorization:** Applied to cap extreme values at the 5th and 95th percentiles.

### 2. Visual Checks
- **Boxplot & Histogram:** Visual inspection of the `open` price distribution showed no extreme outliers.
- **Regression Sensitivity:** A linear regression (`open` → `close`) was performed on both the original and filtered datasets.

### 3. Observed Impact
| Metric | Original (All Data) | Filtered (No Outliers) |
| :--- | :--- | :--- |
| **Slope** | 0.9998 | 0.9998 |
| **Intercept** | 0.353 | 0.353 |
| **R²** | 0.978 | 0.978 |
| **MAE** | 2.75 | 2.75 |

- **Detection:** No outliers were detected using either method (0%), indicating stable data with no extreme deviations beyond 3σ.
- **Model Performance:** The regression R² remained at ~0.99 across both datasets, demonstrating the model's robustness.

### 4. Risks & Assumptions
- **Assumption:** Stock returns follow an approximate normal distribution, which may fail during periods of high volatility.
- **Risk:** The Z-score method can miss subtle but meaningful anomalies that fall within the 3σ range.
- **Risk:** Individual stock behavior can deviate significantly from normal distribution during market crises.

---

## Stage 8: Exploratory Data Analysis (EDA)

### 1. Data Overview
- **Data Shape:** 251 rows and 6 columns
- **Date Range:** 2025-08-27 to 2026-08-26
- **Total Days in Range:** 365 days
- **Trading Days:** 251 days
- **Missing Days:** 114 days (weekends and holidays)

### 2. Descriptive Statistics
| Feature | Count | Mean | Std | Min | 25% | 50% | 75% | Max | Skew | Kurtosis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Close** | 251 | 275.27 | 25.20 | 225.96 | 257.30 | 270.40 | 294.96 | 339.79 | 0.52 | -0.45 |
| **High** | 251 | 278.00 | 25.48 | 229.60 | 258.77 | 273.13 | 299.82 | 344.27 | 0.50 | -0.48 |
| **Low** | 251 | 272.32 | 24.72 | 225.12 | 254.36 | 267.49 | 292.50 | 337.06 | 0.50 | -0.47 |
| **Open** | 251 | 274.98 | 24.92 | 226.05 | 257.00 | 270.16 | 294.43 | 339.74 | 0.50 | -0.47 |
| **Volume** | 251 | 49.7M | 22.7M | 17.9M | 38.7M | 45.2M | 52.7M | 261.8M | 4.53 | 33.14 |

### 3. Distribution & Correlation
- **Distributions:** Price features (close, high, low, open) show near-normal distributions with slight positive skew. `Volume` is heavily right-skewed with high kurtosis, indicating occasional extreme trading days.
- **Correlation Matrix:** Price features are highly correlated with each other (e.g., `close` vs. `low` at 0.996, `close` vs. `open` at 0.989), while `volume` shows virtually no correlation with price movements (all correlations < 0.05).

### 4. Time Series Insights
- **Trend:** A strong overall uptrend from ~$240 to ~$315 (31% gain) over the period.
- **Two Major Pullbacks:** Corrections occurred around March 2026 (drop to ~$250) and September 2026, suggesting cyclical behavior with periodic buying opportunities during dips.
- **Momentum Acceleration:** The sharpest price increase occurred from May to July 2026 ($290→$320), with widening gap between price and rolling averages signaling increasing buyer interest.
- **Moving Averages:** Price consistently traded above both 7-day and 30-day rolling averages, indicating sustained bullish momentum.

### 5. Trading Volume Analysis
- **Average Volume:** ~49.7M shares per day
- **Volume Spikes:** Maximum volume of 261.8M shares (5.3x average)
- **Volume vs. Price:** No significant correlation (0.03), suggesting price moves are not primarily volume-driven.

### 6. Key Insights
1. **Strong overall uptrend** - Price rose from ~$240 to ~$315 (31% gain) with sustained bullish momentum above rolling averages.
2. **Cyclical pullbacks** - Two major corrections suggest buying opportunities during dips.
3. **Momentum acceleration** - Sharpest increase from May to July 2026 signals increasing investor interest.

### 7. Assumptions & Risks
| Assumption | Risk |
| :--- | :--- |
| Historical trends will persist | Trend reversal possible; past performance doesn't guarantee future results |
| Moving averages reliably indicate sentiment | Lagging indicators may give false signals during high volatility |
| Market remains efficient and rational | External shocks (macroeconomic, regulatory, company news) could disrupt trends |
| Price-only analysis is sufficient | Missing volume, fundamental, and sentiment signals |

### 8. Next Steps Before Modeling
- **Feature Engineering:** Lag features (1-day, 5-day, 20-day), rolling statistics, seasonality indicators
- **Volume Analysis:** Price-volume correlations, volume-weighted average price (VWAP)
- **Model Selection:** Linear regression baseline, tree-based models, time series forecasting (ARIMA, LSTM)

---

## Stage 9: Feature Engineering

### Engineered Features
Three new features were created to capture market behavior and improve predictive capability:

| Feature | Formula | Rationale |
| :--- | :--- | :--- |
| **Volatility** | `(high - low) / open` | Captures intraday price fluctuation range. Higher values indicate market uncertainty or significant events; lower values suggest stable trading. Essential for risk assessment. |
| **Momentum** | `(close / close_prev) - 1` | Measures short-term price trend strength. Positive values indicate upward momentum and buying pressure; negative values suggest downward trends. Helps identify trend direction and potential reversals. |
| **Turnover Value** | `close * volume` | Combines price and volume to measure total trading value. High values indicate strong market participation and conviction in price movements; low values suggest weak interest and potentially unreliable price trends. |

### Descriptive Statistics of Engineered Features
| Feature | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Volatility** | 251 | 0.018 | 0.007 | 0.004 | 0.012 | 0.017 | 0.022 | 0.055 |
| **Momentum** | 250 | 0.001 | 0.016 | -0.092 | -0.006 | 0.002 | 0.010 | 0.057 |
| **Turnover Value** | 251 | 1.36e+10 | 6.27e+09 | 4.30e+09 | 9.86e+09 | 1.25e+10 | 1.51e+10 | 5.23e+10 |

### Feature Engineering Rationale
1. **Volatility:** Captures market uncertainty. Higher volatility correlates with higher risk and potential returns.
2. **Momentum:** Identifies trend strength. Positive momentum suggests continued upward movement; negative momentum indicates potential sell-offs.
3. **Turnover Value:** Measures market participation. High turnover with strong price movement confirms trend validity.

---

## Stage 10: Model Regression

### Modeling Approach

A baseline linear regression model was developed to predict AAPL daily momentum (return) using lagged market features. To avoid look-ahead bias, all predictors were shifted by one trading day, and the data was split chronologically rather than randomly.

- **Target:** Daily momentum / return
- **Features:**
  - `volatility_lag1`
  - `turnover_value_lag1`
  - `close_lag1`
- **Training Set:** 200 observations
- **Test Set:** 51 observations
- **Model:** Linear Regression
- **Split:** 80% training / 20% testing, with temporal order preserved

### Model Performance

| Metric | Test Set Result |
| :--- | ---: |
| **R²** | -0.0404 |
| **RMSE** | 0.0207 |
| **MAE** | 0.0147 |

The model produced an **R² of -0.0404**, indicating that the selected features and linear specification did not explain the variation in future AAPL returns better than a simple mean-based baseline. The RMSE of **0.0207** and MAE of **0.0147** indicate that the model's typical prediction error was relatively small in absolute return terms, but the low R² suggests limited explanatory and predictive power.

### What Worked?

The modeling pipeline successfully transformed the Stage 9 engineered features into a predictive regression framework. The use of lagged variables and a chronological train/test split ensured that future information was not used to predict past observations. The model also provides an interpretable baseline that can be used for comparison with more advanced approaches.

### Where Might Assumptions Fail?

The main limitation is the model's weak predictive performance, reflected by the negative R² of **-0.0404**. The model assumes that a stable linear relationship exists between lagged volatility, turnover value, closing price, and future returns, which may not hold in financial markets.

The dataset contains only **251 trading days**, with 200 observations used for training and 51 for testing. This relatively small sample limits the reliability and generalizability of the results. In addition, the model does not incorporate fundamental information, market-wide variables, investor sentiment, or macroeconomic factors. As a result, important drivers of AAPL returns may be omitted.

### How Would You Extend Features or Model?

Future iterations could extend the feature set with:

- **Additional lag features:** 1-day, 5-day, and 20-day returns and prices
- **Rolling statistics:** Moving averages and rolling volatility over multiple windows
- **Momentum indicators:** RSI and other technical indicators
- **Volume features:** Volume moving averages and volume-price relationships
- **Market variables:** S&P 500 returns, interest rates, and broader market volatility

---

## Repository Structure
```
project/
├── data/
│   ├── raw/                        # Raw API data
│   │   └── api_source-yfinace_symbol-AAPL_YYYYMMDD.csv
│   └── processed/                  # Cleaned and feature-engineered data
│       ├── cleaned_data_YYYYMMDD.csv
│       ├── normalized_data_YYYYMMDD.csv
│       └── featured_data_YYYYMMDD.csv
├── src/
│   ├── cleaning.py                 # Data cleaning functions
│   └── eda.py                      # EDA utility functions
├── notebooks/
│   └── pipeline.ipynb              # Main analysis notebook
├── docs/
│   └── README.md                   # Project documentation
├── .env                            # Environment variables (not tracked)
├── .env.example                    # Template for .env
└── requirements.txt                # Project dependencies
```

## Dependencies
- **Data Manipulation:** pandas, numpy
- **Data Visualization:** matplotlib, seaborn
- **Data Acquisition:** yfinance
- **Machine Learning:** scikit-learn
- **Statistical Analysis:** scipy
- **Environment Management:** python-dotenv

## Running the Pipeline
1. **Setup:** Copy `.env.example` to `.env` and configure your paths.
2. **Acquire Data:** Run the pipeline to pull data from Yahoo Finance.
3. **Process Data:** Clean, normalize, and detect outliers.
4. **Analyze:** Generate EDA visualizations and feature engineering.
5. **Model:** (Future) Apply predictive models to the engineered dataset.
