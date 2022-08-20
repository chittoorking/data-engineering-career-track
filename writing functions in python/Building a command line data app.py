# You are building a command line tool that lets a user interactively explore a dataset. 
# We've defined four functions: mean(), std(), minimum(), and maximum() that users can call to analyze their data.
#  Help finish this section of the code so that your users can call any of these functions by typing the function name at the input prompt.

# Note: The function get_user_input() in this exercise is a mock version of asking the user to enter a command. It randomly returns one of the four function names. 
#   In real life, you would ask for input and wait until the user entered a value.

# Instructions
# Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
# The name of the function the user wants to call is stored in func_name. Use the dictionary of functions, function_map,
#  to call the chosen function and pass data as an argument.


## output:
#  height  weight
# 0    72.1     198
# 1    69.8     204
# 2    63.2     164
# 3    64.7     238
# Type a command: 
# > minimum
# height     63.2
# weight    164.0
# dtype: float64
