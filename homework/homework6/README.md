#  Cleaning Strategy
## Raw data structure and Constraint
Because the threshold in drop_missing is set to 0.5, which actually drops nothing, the strategy has to do fill to all float64 columns, or it will leave the data with many NaN. It's not practical in fact because the column 'extra_data' only has two values.
## Functions
### fill_missing_median()
Use the median value to fill all the missing data, whose datatype is float64.

### drop_missing()
It is used to drop data which still has many empty values, and it can produced "clean" data.

### normalize_data()
It is used to transform data to a given range [0,1].