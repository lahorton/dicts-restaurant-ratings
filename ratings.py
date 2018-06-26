import sys
"""Restaurant rating lister."""


def gets_restaurant_ratings(text_file):
    """reads restaurant ratings in a file and prints in alphabetical order"""
    file = open(text_file)
    restaurant_ratings_dictionary = {}

    for line in file:
        line = line.rstrip().split(":")
        restaurant_name, rating = line
        restaurant_ratings_dictionary[restaurant_name] = rating

    file.close()

    return restaurant_ratings_dictionary


def adds_user_ratings(restaurant_ratings_dictionary):
    """adds in new restaurants with user ratings to restaurant ratings dictionary"""
    while True:
        add_restaurant = input("Would you like to add a restaurant review? Type Y or N\n> ").lower()
        if add_restaurant == "n":
            print("n")
            break
        elif add_restaurant == "y":
            print("y")
            break
        else:
            print("Type Y or N.")
            continue

    while add_restaurant == "y":
        try:
            new_restaurant = (input("Restaurant name: ")).title()
            new_rating = int(input("Restaurant rating: "))
            restaurant_ratings_dictionary[new_restaurant] = new_rating
        except TypeError:
            print("Type the restaurant name in letters and rating in numbers.")

        more = input("Add another restaurant? Type Y or N\n> ").lower()
        if more == "y":
            continue
        elif more == "n":
            add_restaurant = "n"
        else:
            print("Type Y or N.")

    return restaurant_ratings_dictionary


def alphabetized_restaurant_ratings(restaurant_ratings_dictionary):
    """Alphabetizes restaurant ratings dictionary"""
    for name, rating in sorted(restaurant_ratings_dictionary.items()):
        print(f"{name} is rated at {rating}.")


file_name = sys.argv[0]
text_file = sys.argv[1]

restaurant_ratings_dictionary = gets_restaurant_ratings('scores.txt')
restaurant_ratings_dictionary = adds_user_ratings(restaurant_ratings_dictionary)
alphabetized_restaurant_ratings(restaurant_ratings_dictionary)
