# Sometimes your functions will need to modify a variable that is outside of the local scope of that function.
# While it's generally not best practice to do so, it's still good to know how in case you need to do it.
# Update these functions so they can modify variables that would usually be outside of their scope.

# Instructions 
# Add a keyword that lets us update call_count from inside the function.

call_count = 0

def my_function():
  # Use a keyword that lets us update call_count 
  global call_count
  call_count += 1
  
  print("You've called my_function() {} times!".format(
    call_count
  ))
  
for _ in range(20):
  my_function()
