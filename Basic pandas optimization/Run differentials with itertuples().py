# The New York Yankees have made a trade with the San Francisco Giants for your analyst contract— you're a hot commodity! Your new boss has seen your work with the Giants and now wants you to do something similar with the Yankees data. He'd like you to calculate run differentials for the Yankees from the year 1962 to the year 2012 and find which season they had the best run differential.

# You've remembered the function you used when working with the Giants and quickly write it down:

# def calc_run_diff(runs_scored, runs_allowed):

#     run_diff = runs_scored - runs_allowed

#     return run_diff
# Let's use .itertuples() to loop over the yankees_df DataFrame (which has been loaded into your session) and calculate run differentials.

# Instructions
# Use .itertuples() to loop over yankees_df and grab each row's runs scored and runs allowed values.

run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA
    run_diffs=runs_scored-runs_allowed
    
# Now, calculate each row's run differential using calc_run_diff(). Be sure to append each row's run differential to run_diffs.
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)
# Append a new column called 'RD' to the yankees_df DataFrame that contains the run differentials you calculated.

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

# # output
# eam League  Year   RS   RA    W    G  Playoffs   RD
# 0   NYY     AL  2012  804  668   95  162         1  136
# 1   NYY     AL  2011  867  657   97  162         1  210
# 2   NYY     AL  2010  859  693   95  162         1  166
# 3   NYY     AL  2009  915  753  103  162         1  162
# 4   NYY     AL  2008  789  727   89  162         0   62
# 5   NYY     AL  2007  968  777   94  162         1  191
# 6   NYY     AL  2006  930  767   97  162         1  163
# 7   NYY     AL  2005  886  789   95  162         1   97
# 8   NYY     AL  2004  897  808  101  162         1   89
# 9   NYY     AL  2003  877  716  101  163         1  161
# 10  NYY     AL  2002  897  697  103  161         1  200
# 11  NYY     AL  2001  804  713   95  161         1   91
# 12  NYY     AL  2000  871  814   87  161         1   57
# 13  NYY     AL  1999  900  731   98  162         1  169
# 14  NYY     AL  1998  965  656  114  162         1  309
# 15  NYY     AL  1997  891  688   96  162         1  203
# 16  NYY     AL  1996  871  787   92  162         1   84
# 17  NYY     AL  1993  821  761   88  162         0   60
# 18  NYY     AL  1992  733  746   76  162         0  -13
# 19  NYY     AL  1991  674  777   71  162         0 -103
# 20  NYY     AL  1990  603  749   67  162         0 -146
# 21  NYY     AL  1989  698  792   74  161         0  -94
# 22  NYY     AL  1988  772  748   85  161         0   24
# 23  NYY     AL  1987  788  758   89  162         0   30
# 24  NYY     AL  1986  797  738   90  162         0   59
# 25  NYY     AL  1985  839  660   97  161         0  179
# 26  NYY     AL  1984  758  679   87  162         0   79
# 27  NYY     AL  1983  770  703   91  162         0   67
# 28  NYY     AL  1982  709  716   79  162         0   -7
# 29  NYY     AL  1980  820  662  103  162         1  158
# 30  NYY     AL  1979  734  672   89  160         0   62
# 31  NYY     AL  1978  735  582  100  163         1  153
# 32  NYY     AL  1977  831  651  100  162         1  180
# 33  NYY     AL  1976  730  575   97  159         1  155
# 34  NYY     AL  1975  681  588   83  160         0   93
# 35  NYY     AL  1974  671  623   89  162         0   48
# 36  NYY     AL  1973  641  610   80  162         0   31
# 37  NYY     AL  1971  648  641   81  162         0    7
# 38  NYY     AL  1970  680  612   93  163         0   68
# 39  NYY     AL  1969  562  587   80  162         0  -25
# 40  NYY     AL  1968  536  531   83  164         0    5
# 41  NYY     AL  1967  522  621   72  163         0  -99
# 42  NYY     AL  1966  611  612   70  160         0   -1
# 43  NYY     AL  1965  611  604   77  162         0    7
# 44  NYY     AL  1964  730  577   99  164         1  153
# 45  NYY     AL  1963  714  547  104  161         1  167
# 46  NYY     AL  1962  817  680   96  162         1  137
