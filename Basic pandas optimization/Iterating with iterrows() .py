# In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs.
# But, what does this mean? Let's explore with a few coding exercises.

# A pandas DataFrame has been loaded into your session called pit_df.
# This DataFrame contains the stats for the Major League Baseball team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012.
# It has been printed into your console for convenience.

# Instructions 
# Use .iterrows() to loop over pit_df and print each row. Save the first item from .iterrows() as i and the second as row.

# Add two lines to the loop: one before print(row) to print each index variable and one after to print each row's type.

# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))
# output:
#  Name: 0, dtype: object
#     <class 'pandas.core.series.Series'>
#     1
#     Team         PIT
#     League        NL
#     Year        2011
#     RS           610
#     RA           712
#     W             72
#     G            162
#     Playoffs       0
#     Name: 1, dtype: object
#     <class 'pandas.core.series.Series'>
#     2
#     Team         PIT
#     League        NL
#     Year        2010
#     RS           587
#     RA           866
#     W             57
#     G            162
#     Playoffs       0
#     Name: 2, dtype: object
#     <class 'pandas.core.series.Series'>
#     3
#     Team         PIT
#     League        NL
#     Year        2009
#     RS           636
#     RA           768
#     W             62
#     G            161
#     Playoffs       0
#     Name: 3, dtype: object
#     <class 'pandas.core.series.Series'>
#     4
#     Team         PIT
#     League        NL
#     Year        2008
#     RS           735
#     RA           884
#     W             67
#     G            162
#     Playoffs       0
#     Name: 4, dtype: object
#     <class 'pandas.core.series.Series'>

# Instead of using i and row in the for statement to store the output of .iterrows(), use one variable named row_tuple.

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

# (0, Team         PIT
# League        NL
# Year        2012
# RS           651
# RA           674
# W             79
# G            162
# Playoffs       0
# Name: 0, dtype: object)
# (1, Team         PIT
# League        NL
# Year        2011
# RS           610
# RA           712
# W             72
# G            162
# Playoffs       0
# Name: 1, dtype: object)
# (2, Team         PIT
# League        NL
# Year        2010
# RS           587
# RA           866
# W             57
# G            162
# Playoffs       0
# Name: 2, dtype: object)
# (3, Team         PIT
# League        NL
# Year        2009
# RS           636
# RA           768
# W             62
# G            161
# Playoffs       0
# Name: 3, dtype: object)
# (4, Team         PIT
# League        NL
# Year        2008
# RS           735
# RA           884
# W             67
# G            162
# Playoffs       0
# Name: 4, dtype: object)

# Add a line in the for loop to print the type of each row_tuple.

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))
# <class 'tuple'>
