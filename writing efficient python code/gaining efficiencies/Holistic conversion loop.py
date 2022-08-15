# A list of all possible Pokémon types has been loaded into your session as pokemon_types. It's been printed in the console for convenience.

# You'd like to gather all the possible pairs of Pokémon types. 
# You want to store each of these pairs in an individual list with an enumerated index as the first element of each list.
# This allows you to see the total number of possible pairs and provides an indexed label for each pair.

# The below loop was written to accomplish this task:

# enumerated_pairs = []

# for i,pair in enumerate(possible_pairs, 1):
#     enumerated_pair_tuple = (i,) + pair
#     enumerated_pair_list = list(enumerated_pair_tuple)
#     enumerated_pairs.append(enumerated_pair_list)
# Let's make this loop more efficient using a holistic conversion.

# combinations from the itertools module has been loaded into your session.
# Use it to create a list called possible_pairs that contains all possible pairs of Pokémon types (each pair has 2 Pokémon types).
# Create an empty list called enumerated_tuples above the for loop.
# Within the for loop, append each enumerated_pair_tuple to the empty list you created in the above step.
# Use a built-in function to convert each tuple in enumerated_tuples to a list.

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)
# print(enumerated_tuples)
# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

# output
# [[1, 'Bug', 'Dark'], [2, 'Bug', 'Dragon'], [3, 'Bug', 'Electric'], [4, 'Bug', 'Fairy'], [5, 'Bug', 'Fighting'], [6, 'Bug', 'Fire'],
# [7, 'Bug', 'Flying'], [8, 'Bug', 'Ghost'], [9, 'Bug', 'Grass'], [10, 'Bug', 'Ground'], [11, 'Bug', 'Ice'], [12, 'Bug', 'Normal'], [13, 'Bug', 'Poison'],
# [14, 'Bug', 'Psychic'], [15, 'Bug', 'Rock'], [16, 'Bug', 'Steel'], [17, 'Bug', 'Water'], [18, 'Dark', 'Dragon'], [19, 'Dark', 'Electric'], [20, 'Dark', 'Fairy'],
# [21, 'Dark', 'Fighting'], [22, 'Dark', 'Fire'], [23, 'Dark', 'Flying'], [24, 'Dark', 'Ghost'], [25, 'Dark', 'Grass'], [26, 'Dark', 'Ground'], [27, 'Dark', 'Ice'],
# [28, 'Dark', 'Normal'], [29, 'Dark', 'Poison'], [30, 'Dark', 'Psychic'], [31, 'Dark', 'Rock'], [32, 'Dark', 'Steel'], [33, 'Dark', 'Water'],
# [34, 'Dragon', 'Electric'], [35, 'Dragon', 'Fairy'], [36, 'Dragon', 'Fighting'], [37, 'Dragon', 'Fire'], [38, 'Dragon', 'Flying'], [39, 'Dragon', 'Ghost'], 
# [40, 'Dragon', 'Grass'], [41, 'Dragon', 'Ground'], [42, 'Dragon', 'Ice'], [43, 'Dragon', 'Normal'], [44, 'Dragon', 'Poison'], [45, 'Dragon', 'Psychic'],
# [46, 'Dragon', 'Rock'], [47, 'Dragon', 'Steel'], [48, 'Dragon', 'Water'], [49, 'Electric', 'Fairy'], [50, 'Electric', 'Fighting'], [51, 'Electric', 'Fire'], 
# [52, 'Electric', 'Flying'], [53, 'Electric', 'Ghost'], [54, 'Electric', 'Grass'], [55, 'Electric', 'Ground'], [56, 'Electric', 'Ice'], [57, 'Electric', 'Normal'],
# [58, 'Electric', 'Poison'], [59, 'Electric', 'Psychic'], [60, 'Electric', 'Rock'], [61, 'Electric', 'Steel'], [62, 'Electric', 'Water'], [63, 'Fairy', 'Fighting'], 
# [64, 'Fairy', 'Fire'], [65, 'Fairy', 'Flying'], [66, 'Fairy', 'Ghost'], [67, 'Fairy', 'Grass'], [68, 'Fairy', 'Ground'], [69, 'Fairy', 'Ice'], 
# [70, 'Fairy', 'Normal'], [71, 'Fairy', 'Poison'], [72, 'Fairy', 'Psychic'], [73, 'Fairy', 'Rock'], [74, 'Fairy', 'Steel'], [75, 'Fairy', 'Water'], 
# [76, 'Fighting', 'Fire'], [77, 'Fighting', 'Flying'], [78, 'Fighting', 'Ghost'], [79, 'Fighting', 'Grass'], [80, 'Fighting', 'Ground'], [81, 'Fighting', 'Ice'],
# [82, 'Fighting', 'Normal'], [83, 'Fighting', 'Poison'], [84, 'Fighting', 'Psychic'], [85, 'Fighting', 'Rock'], [86, 'Fighting', 'Steel'], [87, 'Fighting', 'Water'],
# [88, 'Fire', 'Flying'], [89, 'Fire', 'Ghost'], [90, 'Fire', 'Grass'], [91, 'Fire', 'Ground'], [92, 'Fire', 'Ice'], [93, 'Fire', 'Normal'], [94, 'Fire', 'Poison'],
# [95, 'Fire', 'Psychic'], [96, 'Fire', 'Rock'], [97, 'Fire', 'Steel'], [98, 'Fire', 'Water'], [99, 'Flying', 'Ghost'], [100, 'Flying', 'Grass'],
# [101, 'Flying', 'Ground'], [102, 'Flying', 'Ice'], [103, 'Flying', 'Normal'], [104, 'Flying', 'Poison'], [105, 'Flying', 'Psychic'], [106, 'Flying', 'Rock'], 
# [107, 'Flying', 'Steel'], [108, 'Flying', 'Water'], [109, 'Ghost', 'Grass'], [110, 'Ghost', 'Ground'], [111, 'Ghost', 'Ice'], [112, 'Ghost', 'Normal'],
# [113, 'Ghost', 'Poison'], [114, 'Ghost', 'Psychic'], [115, 'Ghost', 'Rock'], [116, 'Ghost', 'Steel'], [117, 'Ghost', 'Water'], [118, 'Grass', 'Ground'], 
# [119, 'Grass', 'Ice'], [120, 'Grass', 'Normal'], [121, 'Grass', 'Poison'], [122, 'Grass', 'Psychic'], [123, 'Grass', 'Rock'], [124, 'Grass', 'Steel'], 
# [125, 'Grass', 'Water'], [126, 'Ground', 'Ice'], [127, 'Ground', 'Normal'], [128, 'Ground', 'Poison'], [129, 'Ground', 'Psychic'], [130, 'Ground', 'Rock'],
# [131, 'Ground', 'Steel'], [132, 'Ground', 'Water'], [133, 'Ice', 'Normal'], [134, 'Ice', 'Poison'], [135, 'Ice', 'Psychic'], [136, 'Ice', 'Rock'],
# [137, 'Ice', 'Steel'], [138, 'Ice', 'Water'], [139, 'Normal', 'Poison'], [140, 'Normal', 'Psychic'], [141, 'Normal', 'Rock'], [142, 'Normal', 'Steel'],
# [143, 'Normal', 'Water'], [144, 'Poison', 'Psychic'], [145, 'Poison', 'Rock'], [146, 'Poison', 'Steel'], [147, 'Poison', 'Water'], [148, 'Psychic', 'Rock'],
# [149, 'Psychic', 'Steel'], [150, 'Psychic', 'Water'], [151, 'Rock', 'Steel'], [152, 'Rock', 'Water'], [153, 'Steel', 'Water']]
