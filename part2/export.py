from reports import *
# Export functions


def export_reports(export_filename, source_filename):
    output = open(export_filename, "w")
    output.write(str(get_most_played(source_filename)) + '\n')
    output.write(str(sum_sold(source_filename)) + '\n')
    output.write(str(get_selling_avg(source_filename)) + '\n')
    output.write(str(count_longest_title(source_filename)) + '\n')
    output.write(str(get_date_avg(source_filename)) + '\n')
    title = input("Which title interests You?: ")
    output.write(str(get_game(source_filename, title)) + '\n')
    output.write(str(count_grouped_by_genre(source_filename)) + '\n')
    output.write(str(get_date_ordered(source_filename)) + '\n')
    output.close()


export_reports("export.txt", "game_stat.txt")
