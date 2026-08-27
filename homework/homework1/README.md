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
