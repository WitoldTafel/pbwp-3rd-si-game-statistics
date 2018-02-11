
# Report functions
def file_to_list(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            stat_list.append(i)
    return stat_list


def count_games(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    return len(game_stat_list)


def decide(filename, year):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        if i[2] == year:
            return True
    return "False"


def get_latest(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    game_stat_list = sorted(game_stat_list, key=lambda x: x[2], reverse=True)
    return game_stat_list[0][0]


def count_by_genre(filename, genre):
    genre_list = []
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        genre_list.append(i[3])
    return genre_list.count(genre)


def get_line_number_by_title(filename, title):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        if i[0] == title:
            return game_stat_list.index(i) + 1
    raise ValueError('No such a game here')

def get_genres(filename):
    game_stat_list = []
    a = set()#set used to get rid of duplicates
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        a.add(i[3])
    a = sorted(a, key=str.lower)
    return a
print (get_genres("game_stat.txt"))

def when_was_top_sold_fps(filename):
    game_stat_list = []
    fps_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        if i[3] == "First-person shooter":
            fps_list.append(i)
    fps_list = sorted(fps_list, key=lambda x: float(x[1]))
    if not fps_list:
        raise ValueError("No fps here")
    return int(fps_list[-1][2])

def sort_abc(filename):
    game_stat_list = []
    title_list = []
    ordered_title_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        title_list.append(i[0])
    for i in range(len(title_list)):
        ordered_title_list.append(min(title_list))
        title_list.remove(min(title_list))
    return ordered_title_list
