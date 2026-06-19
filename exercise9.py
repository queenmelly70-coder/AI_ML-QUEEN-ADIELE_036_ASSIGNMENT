# Our original movie lists
my_movies = ["Inception", "Batman", "Avatar", "Titanic", "Matrix", "Shrek", "Jaws", "Alien"]
friend1_movies = ["Batman", "Matrix", "Spiderman", "Shrek", "Thor", "Hulk", "Ironman", "Blade"]
friend2_movies = ["Avatar", "Batman", "Shrek", "Alien", "Frozen", "Moana", "Mulan", "Up"]

# Convert lists to sets for analysis
my_set = set(my_movies)
friend1_set = set(friend1_movies)
friend2_set = set(friend2_movies)

# 1. Movies everyone wants to watch
perfect_matches = my_set & friend1_set & friend2_set
print(f"Movies we ALL agree on: {perfect_matches}")

# 2. Movies only I like
my_unique_movies = my_set - friend1_set - friend2_set
print(f"Movies I like but friends don't: {my_unique_movies}")

# 3. Movies only friend1 likes
friend1_unique_movies = friend1_set - my_set - friend2_set
print(f"Movies friend1 likes but we don't: {friend1_unique_movies}")

# 4. Movies only friend2 likes
friend2_unique_movies = friend2_set - my_set - friend1_set
print(f"Movies friend2 likes but we don't: {friend2_unique_movies}")
# 3. Movies exactly TWO people agree on
me_and_f1 = (my_set & friend1_set) - friend2_set
me_and_f2 = (my_set & friend2_set) - friend1_set
f1_and_f2 = (friend1_set & friend2_set) - my_set

print(f"Movies me and Friend 1 agree on: {me_and_f1}")
print(f"Movies me and Friend 2 agree on: {me_and_f2}")
print(f"Movies Friend 1 and Friend 2 agree on: {f1_and_f2}")
