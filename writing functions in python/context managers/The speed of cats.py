image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with  timer():
  print('Pytorch version')
  process_with_pytorch(image)
  
# # output
# Numpy version
# Processing..........done!
# Elapsed: 1.52 seconds
# Pytorch version
# Processing..........done!
# Elapsed: 0.33 seconds
