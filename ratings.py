"""Restaurant rating lister."""


def gets_restaurant_ratings(text_file):
    """reads restaurant ratings in a file and prints in alphabetical order"""
    file = open(text_file)
    restaurant_ratings_dictionary = {}

    for line in file:
        line = line.rstrip().split(":")
        restaurant_name, rating = line
        restaurant_ratings_dictionary[restaurant_name] = rating

    text_file.close()

    return restaurant_ratings_dictionary


def alphabetized_restaurant_ratings(restaurant_ratings_dictionary):
    """Alphabetizes restaurant ratings dictionary"""




print(gets_restaurant_ratings('scores.txt'))