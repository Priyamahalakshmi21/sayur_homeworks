#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like
first_friend_movies = input("First friend, what movies do you like? (Enter a list separated by commas): ").split(',')
common_movies = []
common_movie_count = 0 
attempts = 0 
while common_movie_count < 3 and attempts < 5:
    movie = input("Second friend, what movie do you like? (Enter one at a time): ").strip()
    attempts += 1
    if movie in first_friend_movies:
        common_movies.append(movie)
        common_movie_count += 1 
        print(f"You both like '{movie}'!")
    else:
        print("Try again.")
if common_movie_count >= 3:
    print("You both like the following movies:")
    for movie in common_movies:
        print(f"- {movie}")
else:
    print("You didn't find 3 common movies, or the second friend reached 5 attempts.")        