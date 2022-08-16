# A pandas DataFrame (baseball_df) has been loaded into your session.
# For convenience, a dictionary describing each column within baseball_df has been printed into your console. You can reference these descriptions throughout the exercise.

# You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season ('RS') and 
# total runs allowed in a season ('RA') with the following function:

# def predict_win_perc(RS, RA):
#     prediction = RS ** 2 / (RS ** 2 + RA ** 2)
#     return np.round(prediction, 2)
# Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.

# Instructions 
# Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function.
# Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.

# Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. Save the predicted win percentage as win_perc_preds_apply.
# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc().
# Save these predictions as win_perc_preds_np.
# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

# Team League  Year   RS   RA   W    G  Playoffs    WP  WP_preds
# 0  ARI     NL  2012  734  688  81  162         0  0.50      0.53
# 1  ATL     NL  2012  700  600  94  162         1  0.58      0.58
# 2  BAL     AL  2012  712  705  93  162         1  0.57      0.50
# 3  BOS     AL  2012  734  806  69  162         0  0.43      0.45
# 4  CHC     NL  2012  613  759  61  162         0  0.38      0.39


# Great job! That's a home run! You practiced using three different approaches to iterate over a pandas DataFrame and perform calculations. Did you notice that the .itertuples() approach beat the .apply() approach? Even though both these implementations can be useful, you should default to using a DataFrame's underlying arrays to perform calculations.

# Take a look at your win percentage predictions (column 'WP_preds') and compare them to the actual win percentages (column 'WP'). Not bad!
