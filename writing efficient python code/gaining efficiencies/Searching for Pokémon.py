# Two Pokémon trainers, Ash and Brock, have a collection of ten Pokémon each. Each trainer's Pokédex (their collection of Pokémon) has been loaded into your session as lists called ash_pokedex and brock_pokedex respectively.

# You'd like to see if certain Pokémon are members of either Ash or Brock's Pokédex.

# Let's compare using a set versus using a list when performing this membership testing.

# Instructions 
# Convert Brock's Pokédex list (brock_pokedex) to a set called brock_pokedex_set.

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)
# {'Dugtrio', 'Machop', 'Zubat', 'Geodude', 'Tauros', 'Omastar', 'Kabutops', 'Golem', 'Onix', 'Vulpix'}


# Check if 'Psyduck' is in Ash's Pokédex list (ash_pokedex) and if 'Psyduck' is in Brock's Pokédex set (brock_pokedex_set).

# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)
# True
# False

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

# False
# True

# Within your IPython console, use %timeit to compare membership testing for 'Psyduck' in ash_pokedex, 'Psyduck' in brock_pokedex_set, 'Machop' in ash_pokedex,
# and 'Machop' in brock_pokedex_set (a total of four different timings).

# Don't include the print() function. Only time the commands that you wrote inside the print() function in the previous steps.

# Which membership testing was faster?

# In [1]:
# %timeit 'Psyduck' in ash_pokedex
# 285 ns +- 39.1 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
# In [2]:
# %timeit 'Psyduck' in brock_pokedex_set
# 49.3 ns +- 2.62 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
# In [3]:
# %timeit 'Machop' in ash_pokedex
# 249 ns +- 12.5 ns per loop (mean +- std. dev. of 7 runs, 1000000 loops each)
# In [4]:
# %timeit 'Machop' in brock_pokedex_set
# 52.2 ns +- 3.48 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)
