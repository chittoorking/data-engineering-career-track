# Let's practice slicing numpy arrays and using NumPy's broadcasting concept.
# Remember, broadcasting refers to a numpy array's ability to vectorize operations, so they are performed on all elements of an object at once.

# A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience.
# numpy has been imported into your session as np.

# Instructions 
# second row of nums.
# Print the items of nums that are greater than six.
# Create nums_dbl that doubles each number in nums.
# Replace the third column in nums with a new column that adds 1 to each item in the original column.

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)
# original:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
##output
# [ 6  7  8  9 10]
# [ 7  8  9 10]
# [[ 2  4  6  8 10]
#  [12 14 16 18 20]]
# [[ 1  2  4  4  5]
#  [ 6  7  9  9 10]]
