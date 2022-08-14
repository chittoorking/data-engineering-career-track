# Datasets can contain columns that are not required for an analysis, like the weather table in data.db does.
# Some, such as elevation, are redundant, since all observations occurred at the same place, while others contain variables we are not interested in. After making a database engine, you'll write a query to SELECT only the date and temperature columns, and pass both to read_sql() to make a dataframe of high and low temperature readings.

# pandas has been loaded as pd, and create_engine() has been imported from sqlalchemy.

# Note: The SQL checker is quite picky about column positions and expects fields to be selected in the specified order.

# Instructions
# Create a database engine for data.db.
# Write a SQL query that SELECTs the date, tmax, and tmin columns from the weather table.
# Make a dataframe by passing the query and engine to read_sql() and assign the resulting dataframe to temperatures.


# Create database engine for data.db
engine = create_engine("sqlite:///data.db")

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query,engine)

# View the resulting dataframe
print(temperatures)
