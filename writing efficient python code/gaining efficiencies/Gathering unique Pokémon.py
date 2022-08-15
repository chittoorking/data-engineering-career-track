# A sample of 500 Pokémon has been created with replacement (meaning a Pokémon could be selected more than once and duplicates exist within the sample).

# Three lists have been loaded into your session:

# The names list contains the names of each Pokémon in the sample.
# The primary_types list containing the corresponding primary type of each Pokémon in the sample.
# The generations list contains the corresponding generation of each Pokémon in the sample.
# The below function was written to gather unique values from each list:

# def find_unique_items(data):
#     uniques = []

#     for item in data:
#         if item not in uniques:
#             uniques.append(item)

#     return uniques
# Let's compare the above function to using the set data type for collecting unique items.

# Instructions 
# Use the provided function to collect the unique Pokémon in the names list. Save this as uniq_names_func.

# Use the provided function to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# output
# 368

# Use a set data type to collect the unique Pokémon in the names list. Save this as uniq_names_set.
# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# # output
# 368
# True

# Within your IPython console, use %timeit to compare the find_unique_items() function with using a set data type to collect unique Pokémon character names in names.

# Which membership testing was faster?

# In [1]:
# %timeit find_unique_items(names)
# 2.79 ms +- 94.7 us per loop (mean +- std. dev. of 7 runs, 100 loops each)
# In [2]:
# %timeit set(names)
# 14.8 us +- 2.36 us per loop (mean +- std. dev. of 7 runs, 100000 loops each)

# Use the most efficient approach for gathering unique items to collect the unique Pokémon types (from the primary_types list)
# and Pokémon generations (from the generations list).

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 
# output:
# {'Dragon', 'Dark', 'Normal', 'Ice', 'Fire', 'Electric', 'Fighting', 'Bug', 'Steel', 'Psychic', 'Ground', 'Water', 'Fairy', 'Grass', 'Ghost', 'Rock', 'Poison'}
# {1, 2, 3, 4, 5, 6}
