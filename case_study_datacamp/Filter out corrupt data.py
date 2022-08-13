# One recurrent step you can expect in the transformation phase would be to clean up some incomplete data. In this exercise, you're going to look at course data, which has the following format:

# course_id	title	description	programming_language
# 1	Some Course	…	r
# You're going to inspect this DataFrame and make sure there are no missing values by using the pandas DataFrame's .isnull().sum() methods. You will find that the programming_language column has some missing values.

# As such, you will complete the transform_fill_programming_language() function by using the .fillna() method to fill missing values.

# Instructions
# Print the number of missing values in course_data.
# Missing values of the programming_language should be the language "R".
# Print out the number of missing values per column once more, this time for transformed.

course_data = extract_course_data(db_engines)

# Print out the number of missing values per column
print(course_data.isnull().sum())

# The transformation should fill in the missing values
def transform_fill_programming_language(course_data):
    imputed = course_data.fillna({"programming_language": "R"})
    return imputed

transformed = transform_fill_programming_language(course_data)

# Print out the number of missing values per column of transformed
print(transformed.isnull().sum())

# output:
#   course_id               0
# title                   0
# description             0
# programming_language    3
# dtype: int64
# course_id               0
# title                   0
# description             0
# programming_language    0
# dtype: int64
