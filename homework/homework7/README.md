#  Stage 7

## Outlier Functions Improvement
### check_data()
I add a function which can check data, it will raise ValueError if it checks NaN, Inf, and empty series. And the function is applied at top of other outlier functions.

### Parameters Check
Outlier functions have parameters. I check the positivity of `k` in `detect_outliers_iqr()` and `threshold` in `detect_outliers_zscore()` and I check that `lower` is below `upper` in `winsorize_series()`. It will raise ValueError if problem exits.

## Reflection
### Method
I choose `zscore` for outlier, because the box plot shows that some points, which might be normal, are droped. For `winsorize`, it will change bad points to the boundary level instead of dropping them, which is not a good idea for me, because it also introduces unusual grouped points. And for the `threshold`, 0.3 is good because the data is produced by normal distribution.
### Assumptions
The data is roughly normal.
### Observed Impact
For summary stats, it makes the data more like normal distribution. For simple regression, it's fun that removing makes the R^2 worse. It is because when producing data, the unnormal event happens to `daily_return` at first, the we make `daily_return_2 = 0.6 * daily_return`, which is actually not practical. And, `iqr` performs here worse than `zscore` because it moves more points.
### Risks
If the data is roughly normal, for example, it has heavy tails, the outlier will mask many good points as bad ones. And it will lead to mistake.