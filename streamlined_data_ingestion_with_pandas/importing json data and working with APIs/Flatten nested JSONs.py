# A feature of JSON data is that it can be nested: an attribute's value can consist of attribute-value pairs.
#   This nested data is more useful unpacked, or flattened, into its own dataframe columns.
#   The pandas.io.json submodule has a function, json_normalize(), that does exactly this.

# The Yelp API response data is nested. Your job is to flatten out the next level of data in the coordinates and location columns.

# pandas (as pd) and requests have been imported. The results of the API call are stored as response.

# Instructions
# Load the json_normalize() function from pandas' io.json submodule.
# Isolate the JSON data from response and assign it to data.
# Use json_normalize() to flatten and load the businesses data to a dataframe, cafes. Set the sep argument to use underscores (_), rather than periods.
# Show the data head.

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = pd.json_normalize(data["businesses"],
             sep='_')

# View data

# output
#                       id                        alias               name                                          image_url  is_closed  ... location_zip_code  location_country location_state  \
# 0  CBmrwh7jHn88M4v8Q9Qyyg       white-noise-brooklyn-2        White Noise  https://s3-media2.fl.yelpcdn.com/bphoto/rcNRZr...      False  ...             11201                US             NY   
# 1  NG-KlDcSjBk3pfdzjXmMVw          devocion-brooklyn-3           Devocion  https://s3-media1.fl.yelpcdn.com/bphoto/xEKPpn...      False  ...             11201                US             NY   
# 2  pimuUR-TEHIjUla3S3jemQ   coffee-project-ny-new-york  Coffee Project NY  https://s3-media2.fl.yelpcdn.com/bphoto/2Wtg4i...      False  ...             10003                US             NY   
# 3  wTA00Dov2lFYXKnZ58eXAQ  spreadhouse-cafe-new-york-3   Spreadhouse Cafe  https://s3-media2.fl.yelpcdn.com/bphoto/YsBfwR...      False  ...             10002                US             NY   
# 4  vijwGDNrPBJHEG7_DsjZNw             usagi-ny-dumbo-7           Usagi NY  https://s3-media2.fl.yelpcdn.com/bphoto/5gCxDD...      False  ...             11201                US             NY   

#                   location_display_address price  
# 0        [71 Smith St, Brooklyn, NY 11201]   NaN  
# 1  [276 Livingston St, Brooklyn, NY 11201]    $$  
# 2       [239 E 5th St, New York, NY 10003]    $$  
# 3     [116 Suffolk St, New York, NY 10002]     $  
# 4       [163 Plymouth St, Dumbo, NY 11201]    $$  

# [5 rows x 24 columns]
