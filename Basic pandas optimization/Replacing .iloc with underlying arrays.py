# Now that you have a better grasp on a DataFrame's internals let's update one of your previous analyses to leverage a DataFrame's underlying arrays. 
# You'll revisit the win percentage calculations you performed row by row with the .iloc method:

# def calc_win_perc(wins, games_played):
#     win_perc = wins / games_played
#     return np.round(win_perc,2)

# win_percs_list = []

# for i in range(len(baseball_df)):
#     row = baseball_df.iloc[i]

#     wins = row['W']
#     games_played = row['G']

#     win_perc = calc_win_perc(wins, games_played)

#     win_percs_list.append(win_perc)

# baseball_df['WP'] = win_percs_list
# Let's update this analysis to use arrays instead of the .iloc method. A DataFrame (baseball_df) has been loaded into your session.

# Instructions 
# Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. 
# Store the result as a variable called win_percs_np.

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Create a new column in baseball_df called 'WP' that contains the win percentages you just calculated.
# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())
# # output
# Team League  Year   RS   RA   W    G  Playoffs    WP
# 0  ARI     NL  2012  734  688  81  162         0  0.50
# 1  ATL     NL  2012  700  600  94  162         1  0.58
# 2  BAL     AL  2012  712  705  93  162         1  0.57
# 3  BOS     AL  2012  734  806  69  162         0  0.43
# 4  CHC     NL  2012  613  759  61  162         0  0.38
