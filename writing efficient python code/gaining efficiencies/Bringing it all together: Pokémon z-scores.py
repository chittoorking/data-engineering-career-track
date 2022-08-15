# A list of 720 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a NumPy array called hps.
# You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.

# The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

# poke_zscores = []

# for name,hp in zip(names, hps):
#     hp_avg = hps.mean()
#     hp_std = hps.std()
#     z_score = (hp - hp_avg)/hp_std
#     poke_zscores.append((name, hp, z_score))
# highest_hp_pokemon = []

# for name,hp,zscore in poke_zscores:
#     if zscore > 2:
#         highest_hp_pokemon.append((name, hp, zscore))
# Instructions

# Use NumPy to eliminate the for loop used to create the z-scores.
# Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2.

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# output

# ('Abomasnow', 80.0, 0.46797638117739043)
# ('Abra', 60.0, -0.3271693284337512)
# ('Absol', 131.0, 2.4955979406858013)

# Use list comprehension to replace the for loop used to collect Pokémon with the highest HPs based on their z-score.

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')

# output:
# ('Absol', 131.0, 2.4955979406858013)
# ('Absol', 131.0, 2.4955979406858013)
# ('Bonsly', 127.0, 2.3365687987635733)
# ('Caterpie', 122.0, 2.137782371360788)
# ('Cofagrigus', 133.0, 2.575112511646916)
# ('Cresselia', 126.0, 2.296811513283016)
# ('Dewgong', 122.0, 2.137782371360788)
# ('Druddigon', 126.0, 2.296811513283016)
# ('Froakie', 123.0, 2.1775396568413448)
# ('Kadabra', 135.0, 2.65462708260803)
# ('Klang', 123.0, 2.1775396568413448)
# ('Kricketune', 122.0, 2.137782371360788)
# ('Lumineon', 129.0, 2.4160833697246873)
# ('Magnemite', 137.0, 2.734141653569144)
# ('Nidorina', 119.0, 2.0185105149191167)
# ('Onix', 126.0, 2.296811513283016)
# ('Prinplup', 124.0, 2.217296942321902)
# ('Skuntank', 128.0, 2.3763260842441305)
# ('Swellow', 125.0, 2.2570542278024592)
