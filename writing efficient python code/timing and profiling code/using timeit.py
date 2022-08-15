# Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)
