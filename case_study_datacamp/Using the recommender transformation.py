# In the last few exercises, you calculated the average rating per course and cleaned up some course data.
# You will use this data to produce viable recommendations for DataCamp students.

# As a reminder, here are the decision rules for producing recommendations:

# Use technology a student has rated the most.
# Exclude courses a student has already rated.
# Find the three top-rated courses from eligible courses.
# In order to produce the final recommendations, you will use the average course ratings, and the list of eligible recommendations per user,
# stored in avg_course_ratings and courses_to_recommend respectively.
# You will do this by completing the transform_recommendations() function which merges both DataFrames and finds the top 3 highest rated courses to recommend per user.

# Instructions
# Complete the transform_recommendations() function:
# Merge course_to_recommend with avg_course_ratings.
# Sort the results by rating, grouping by user ID.
# Show the top 3 rows and sort by user ID.
# Call the transform_recommendations() function you just defined with the appropriate arguments to store recommendations per user in the recommendations variable.

# Complete the transformation function
def transform_recommendations(avg_course_ratings, courses_to_recommend):
    # Merge both DataFrames
    merged = courses_to_recommend.merge(avg_course_ratings,how='inner',on='course_id') 
    # Sort values by rating and group by user_id
    grouped = merged.sort_values("rating", ascending=False).groupby("user_id")
    # Produce the top 3 values and sort by user_id
    recommendations = grouped.head(3).sort_values("user_id").reset_index()
    final_recommendations = recommendations[["user_id", "course_id","rating"]]
    # Return final recommendations
    return final_recommendations

# Use the function with the predefined DataFrame objects
recommendations = transform_recommendations(avg_course_ratings, courses_to_recommend)

# output:
#     user_id  course_id    rating
# 0             1         24  4.653061
# 1             1         23  4.800000
# 2             1         46  4.800000
# 3             2         46  4.800000
# 4             2         24  4.653061
# ...         ...        ...       ...
# 113452    38173         56  4.661765
# 113453    38173         86  4.608696
# 113454    38174         23  4.800000
# 113455    38174         24  4.653061
# 113456    38174         46  4.800000

# [113457 rows x 3 columns]
