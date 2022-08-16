# Remember, .itertuples() returns each DataFrame row as a special data type called a namedtuple. You can look up an attribute within a namedtuple with a special syntax.
# Let's practice working with namedtuples.

# A pandas DataFrame has been loaded into your session called rangers_df. This DataFrame contains the stats ('Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', and 'Playoffs') for the Major League baseball team named the Texas Rangers (abbreviated as 'TEX').

# Instructions 
# Use .itertuples() to loop over rangers_df and print each row.

# example output

# Pandas(Index=33, Team='TEX', League='AL', Year=1976, RS=616, RA=652, W=76, G=162, Playoffs=0)

# Loop over rangers_df with .itertuples() and save each row's Index, Year, and Wins (W) attribute as i, year, and wins.

for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  print(i, year, wins)
  
#   Example output
# 0 2012 93
# 1 2011 96
# 2 2010 90
# 3 2009 87
# 4 2008 79

# Now, loop over rangers_df and print these values only for those rows where the Rangers made the playoffs.

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

# output
# 0 2012 93
# 1 2011 96
# 2 2010 90
# 13 1999 95
# 14 1998 88
# 16 1996 90
