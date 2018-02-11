from reports import *
# Printing functions


def print_count_games():
    print(count_games("game_stat.txt"))


def print_decide():
    year = input("Which year interests You?: ")
    print(decide("game_stat.txt", year))


def print_get_latest():
    print(get_latest("game_stat.txt"))


def print_count_by_genre():
    genre = input("Which genre interests You?: ")
    print(count_by_genre("game_stat.txt", genre))


def print_line_number_by_title():
    title = input("Which title interests You?: ")
    print(get_line_number_by_title("game_stat.txt", title))


def print_get_genres():
    print(get_genres("game_stat.txt"))


def print_when_was_top_sold_fps():
    print(when_was_top_sold_fps("game_stat.txt"))


def print_sort_abc():
    print(sort_abc("game_stat.txt"))


print_count_games()
print_decide()
print_get_latest()
print_count_by_genre()
print_line_number_by_title()
print_get_genres()
print_when_was_top_sold_fps()
print_sort_abc()
