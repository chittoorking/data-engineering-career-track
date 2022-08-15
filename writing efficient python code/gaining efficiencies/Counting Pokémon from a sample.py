# A sample of 500 Pokémon has been generated, and three lists from this sample have been loaded into your session:

# The names list contains the names of each Pokémon in the sample.
# The primary_types list containing the corresponding primary type of each Pokémon in the sample.
# The generations list contains the corresponding generation of each Pokémon in the sample.
# You want to quickly gather a few counts from these lists to better understand the sample that was generated.
# Use Counter from the collections module to explore what types of Pokémon are in your sample, what generations they come from, 
# and how many Pokémon have a name that starts with a specific letter.

# Counter has already been imported into your session for convenience.

# Collect the count of each primary type from the sample.
# Collect the count of each generation from the sample.
# Use list comprehension to collect the first letter of each Pokémon in the names list. Save this as starting_letters.
# Collect the count of starting letters from the starting_letters list. Save this as starting_letters_count.

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

# output:
# Counter({'Water': 66, 'Normal': 64, 'Bug': 51, 'Grass': 47, 'Psychic': 31, 'Rock': 29, 'Fire': 27, 'Electric': 25, 'Ground': 23, 'Fighting': 23, 'Poison': 22,
#          'Steel': 18, 'Ice': 16, 'Fairy': 16, 'Dragon': 16, 'Ghost': 13, 'Dark': 13}) 

# Counter({5: 122, 3: 103, 1: 99, 4: 78, 2: 51, 6: 47}) 

# Counter({'S': 83, 'C': 46, 'D': 33, 'M': 32, 'L': 29, 'G': 29, 'B': 28, 'P': 23, 'A': 22, 'K': 20, 'E': 19, 'W': 19, 'T': 19, 'F': 18, 'H': 15, 'R': 14, 'N': 13,
#          'V': 10, 'Z': 8, 'J': 7, 'I': 4, 'O': 3, 'Y': 3, 'U': 2, 'X': 1})
