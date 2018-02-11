from reports import *
# Printing functions


def print_get_most_played():
    print(get_most_played("game_stat.txt"))


def print_sum_sold():
    print(sum_sold("game_stat.txt"))


def print_get_selling_avg():
    print(get_selling_avg("game_stat.txt"))


def print_count_longest_title():
    print(count_longest_title("game_stat.txt"))


def print_get_date_avg():
    print(get_date_avg("game_stat.txt"))


def print_get_game():
    title = input("Which title interests You?: ")
    print(get_game("game_stat.txt", title))


def print_count_grouped_by_genre():
    print(count_grouped_by_genre("game_stat.txt"))


def print_get_date_ordered():
    print(get_date_ordered("game_stat.txt"))


print_get_most_played()
print_sum_sold()
print_get_selling_avg()
print_count_longest_title()
print_get_date_avg()
print_get_game()
print_count_grouped_by_genre()
print_get_date_ordered()
