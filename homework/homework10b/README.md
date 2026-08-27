#  Stage 10b

Results shown in notebook are produced when the `.ipynb` file is placed like `./homework10b/stage10b_modeling-time-series-and-classification_submission`

The data used in homework is my data, and its size is very small which might make predications not good.

The homework uses classification to make predications.
## Interpretation in homework
- What worked?

The classification pipeline was successfully implemented using lagged return, rolling mean return, and rolling volatility as features. A time-aware train/test split was used to preserve the temporal order of the observations. The Logistic Regression model correctly identified all of the upward observations in the test set, resulting in a recall of 1.00 for class 1.
- Where might assumptions fail?

Although the model achieved an accuracy of 0.53, it failed to identify any downward observations. This indicates that the model predicted the upward class for all test observations rather than effectively distinguishing between upward and downward movements. Therefore, the accuracy alone does not indicate strong predictive performance. The relatively small test set of 19 observations also makes the evaluation sensitive to individual predictions.

- How would you extend features or model?

The feature set could be extended by adding more lagged returns, longer-window rolling statistics, momentum indicators, and trading volume features. Other classification models, such as Decision Trees or other tree-based models, could be compared with Logistic Regression. A larger dataset and time-series cross-validation could also provide a more reliable evaluation of the model's predictive performance.