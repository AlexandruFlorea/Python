MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, \n'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

def find_movie():
    search_item = input("What movie title are you looking for? ")
    for movie in movies:
        if search_item in movie['title']:
            print_movie(movie)
        elif search_item in movie['director']:
            print_movie(movie)
        elif search_item in movie['year']:
            print_movie(movie)
        else:
            print("Movie not found.")
            menu()


def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if  selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movie()
        else:
            print("Unknown command. Please try again.")
        selection = input(MENU_PROMPT)


menu()