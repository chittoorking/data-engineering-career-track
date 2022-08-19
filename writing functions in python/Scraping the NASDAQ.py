# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt','w') as  f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
# Opening stock ticker for NVDA
# Logging $139.50 for NVDA
# Logging $139.54 for NVDA
# Logging $139.61 for NVDA
# Logging $139.65 for NVDA
# Logging $139.72 for NVDA
# Logging $139.73 for NVDA
# Logging $139.80 for NVDA
# Logging $139.78 for NVDA
# Logging $139.73 for NVDA
# Logging $139.64 for NVDA
# Closing stock ticker
