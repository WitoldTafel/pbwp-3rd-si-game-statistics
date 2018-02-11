
# Report functions
def get_most_played(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    game_stat_list = sorted(game_stat_list, key=lambda x: float(x[1]), reverse=True)
    return game_stat_list[0][0]

def sum_sold(filename):
    game_stat_list = []
    sold = 0
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        sold += float(i[1])
    return sold

#("game_stat.txt")

def get_selling_avg(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    return sum_sold(filename)/len(game_stat_list)

def count_longest_title(filename):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    title_list = [i[0] for i in game_stat_list]
    return len(max(title_list, key=len))

def get_date_avg(filename):
    game_stat_list = []
    dates = 0
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        dates += float(i[2])
    return round(dates/len(game_stat_list))

def get_game(filename, title):
    game_stat_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        if i[0] == title:
            i[1] = float(i[1])
            i[2] = float(i[2])
            return i
    return "No such a game here"

def count_grouped_by_genre(filename):
    game_stat_list = []
    genre_set = set()#set used to get rid of duplicates
    to_be_values=[]
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    for i in game_stat_list:
        genre_set.add(i[3])
    to_be_keys = list(genre_set)
    genre_list_with_dupes = [i[3] for i  in game_stat_list]
    for i in to_be_keys:
        to_be_values.append(genre_list_with_dupes.count(i))
    genre_grouped_dict = dict(zip(to_be_keys,to_be_values))
    return genre_grouped_dict

def get_date_ordered(filename):
    game_stat_list = []
    ordered_title_list = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            i = i.split("\t")
            game_stat_list.append(i)
    game_stat_list = sorted(game_stat_list,key= lambda x:(-float(x[2]),x[0]))
    ordered_title_list = [i[0] for i in game_stat_list]
    return ordered_title_list
#print(get_date_ordered("game_stat.txt"))
