#  Stage 8
Results shown in notebook are produced when the `.ipynb` file is placed like `./homework8/homework08_exploratory-data-analysis_submission`
## Insights & Assumptions 
- TODO: Top 3 insights
- TODO: Assumptions & risks
- TODO: Next steps before modeling (cleaning & features)
### Top 3 insights
- `transactions` is actually stable, if we don't consider the two abnormal data, which means people have needs all the time.
- Although date might be continuous, null value in data could make rolling window a mess.
- `kurtosis` of `transactions` is extremely high, which is caused by the two abnormal data, and if they are real, it's might because of discount day. 
### Assumptions & risks
We assume that data should be normal and continuous, but the risks are that there are problems.
### Next steps before modeling
Fill the null value of `spend` and `income`, then fix the abnormal data in `transactions`.