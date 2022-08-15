# A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers).

# You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.

# def get_publisher_heroes(heroes, publishers, desired_publisher):

#     desired_heroes = []

#     for i,pub in enumerate(publishers):
#         if pub == desired_publisher:
#             desired_heroes.append(heroes[i])

#     return desired_heroes
# def get_publisher_heroes_np(heroes, publishers, desired_publisher):

#     heroes_np = np.array(heroes)
#     pubs_np = np.array(publishers)

#     desired_heroes = heroes_np[pubs_np == desired_publisher]

#     return desired_heroes

# Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe.
# The desired_publisher for Star Wars is 'George Lucas'.

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes,publishers, "George Lucas")

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes,publishers, "George Lucas")

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

# output:
# ['Darth Vader', 'Han Solo', 'Luke Skywalker', 'Yoda']
# <class 'list'>
# ['Darth Vader' 'Han Solo' 'Luke Skywalker' 'Yoda']
# <class 'numpy.ndarray'>

Within your IPython console, load the line_profiler and use %lprun to profile the two functions for line-by-line runtime.
When using %lprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:
Which function has the fastest runtime?


%load_ext line_profiler
%lprun -f get_publisher_heroes get_publisher_heroes(heroes,publishers,"George Lucas")
%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes,publishers,"George Lucas")
The line_profiler extension is already loaded. To reload it, use:
  %reload_ext line_profiler
Timer unit: 1e-06 s

Total time: 0.000649 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def get_publisher_heroes(heroes, publishers, desired_publisher):
     2                                           
     3         1          3.0      3.0      0.5      desired_heroes = []
     4                                           
     5       481        328.0      0.7     50.5      for i,pub in enumerate(publishers):
     6       480        296.0      0.6     45.6          if pub == desired_publisher:
     7         4         22.0      5.5      3.4              desired_heroes.append(heroes[i])
     8                                           
     9         1          0.0      0.0      0.0      return desired_heroes
Timer unit: 1e-06 s

Total time: 0.000242 s
File: <ipython-input-1-5a6bc05c1c55>
Function: get_publisher_heroes_np at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    13                                           
    14         1        120.0    120.0     49.6      heroes_np = np.array(heroes)
    15         1         94.0     94.0     38.8      pubs_np = np.array(publishers)
    16                                           
    17         1         27.0     27.0     11.2      desired_heroes = heroes_np[pubs_np == desired_publisher]
    18                                           
    19         1          1.0      1.0      0.4      return desired_heroes
 


Within your IPython console, load the memory_profiler and use %mprun to profile the two functions for line-by-line memory consumption.
The get_publisher_heroes() function and get_publisher_heroes_np() function have been saved within a file titled hero_funcs.py 
(i.e., you can import both functions from hero_funcs). 
When using %mprun, use each function to gather the Star Wars heroes as you did in the previous step. After you've finished profiling, answer the following question:

Which function uses the least amount of memory?

In [2]:
%load_ext memory_profiler
In [3]:
from hero_funcs import get_publisher_heroes,get_publisher_heroes_np
In [4]:
%mprun -f get_publisher_heroes get_publisher_heroes(heroes,publishers,"George Lucas")
Filename: /tmp/tmptnr16ip_/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4    109.3 MiB    109.3 MiB           1   def get_publisher_heroes(heroes, publishers, desired_publisher):
     5                                         
     6    109.3 MiB      0.0 MiB           1       desired_heroes = []
     7                                         
     8    109.3 MiB      0.0 MiB         481       for i,pub in enumerate(publishers):
     9    109.3 MiB      0.0 MiB         480           if pub == desired_publisher:
    10    109.3 MiB      0.0 MiB           4               desired_heroes.append(heroes[i])
    11                                         
    12    109.3 MiB      0.0 MiB           1       return desired_heroes
In [5]:
%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes,publishers,"George Lucas")
Filename: /tmp/tmptnr16ip_/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15    109.3 MiB    109.3 MiB           1   def get_publisher_heroes_np(heroes, publishers, desired_publisher):
    16                                         
    17    109.3 MiB      0.0 MiB           1       heroes_np = np.array(heroes)
    18    109.3 MiB      0.0 MiB           1       pubs_np = np.array(publishers)
    19                                         
    20    109.3 MiB      0.0 MiB           1       desired_heroes = heroes_np[pubs_np == desired_publisher]
    21                                         
    22    109.3 MiB      0.0 MiB           1       return desired_heroes
