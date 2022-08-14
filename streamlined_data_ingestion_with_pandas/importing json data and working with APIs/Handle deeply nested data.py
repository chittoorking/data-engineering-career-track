# Last exercise, you flattened data nested down one level. Here, you'll unpack more deeply nested data.

# The categories attribute in the Yelp API response contains lists of objects.
# To flatten this data, you'll employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the dataframe.
# You should also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions. We'll work through this in steps.

# pandas (as pd) and json_normalize() have been imported. JSON-formatted Yelp data on cafes in NYC is stored as data.

# Use json_normalize() to flatten records under the businesses key in data, setting underscores (_) as separators.
# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                  sep='_')

# View the data
print(flat_cafes.head())

# Specify the record_path to the categories data.

# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories")

# View the data
print(flat_cafes.head())

# Set the meta keyword argument to get business name, alias, rating, and the attributes nested under coordinates: latitude and longitude.
# Add "biz_" as a meta_prefix to prevent duplicate column names.

# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates','latitude'], 
                          		  ['coordinates','longitude']],
                    		meta_prefix="biz_")





# View the data
print(flat_cafes.head())


#              alias              title           biz_name                   biz_alias biz_rating biz_coordinates_latitude biz_coordinates_longitude
# 0            coffee       Coffee & Tea        White Noise      white-noise-brooklyn-2        4.5                   40.689                   -73.988
# 1            coffee       Coffee & Tea           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 2  coffeeroasteries  Coffee Roasteries           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 3             cafes              Cafes           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
# 4            coffee       Coffee & Tea  Coffee Project NY  coffee-project-ny-new-york        4.5                   40.727                   -73.989


# Great job! Naming meta columns can get tedious for datasets with many attributes, and code is susceptible to breaking if column names or nesting levels change.
# In such cases, you may have to write a custom function and employ techniques like recursion to handle the data.
