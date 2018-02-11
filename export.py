from reports import *
# Export functions
def export_reports(export_filename,source_filename):
    output = open(export_filename, "w")
    output.write(str(count_games(source_filename)) + '\n')
    year = input("Which year interests You?: ")
    output.write(str(decide(source_filename,year)) + '\n')
    output.write(get_latest(source_filename) + '\n')
    genre = input("Which genre interests You?: ")
    output.write(str(count_by_genre(source_filename, genre)) + '\n')
    title = input("Which title interests You?: ")
    output.write(str(get_line_number_by_title(source_filename, title)) + '\n')
    output.write(str(sort_abc(source_filename)) + '\n')
    output.write(str(get_genres(source_filename)) + '\n')
    output.write(str(when_was_top_sold_fps(source_filename)) + '\n')
    output.close()

export_reports("export.txt", "game_stat.txt")
