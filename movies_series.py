import random

from datetime import date

date = date.today()


class Movies:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views
    
    def __str__(self):
        return f"{self.title} {self.year}"
    
    def __repr__(self):
        return self.__str__()
    
    def play(self):
        self.views +=1



class Series(Movies):
    def __init__(self, season_number, episode_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episode_number = episode_number
    def __str__(self):
        return f"{self.title} S{self.season_number}E{self.episode_number}"


movie_1 = Movies(title="Harry Potter", year="2001", genre="adventure", views=150)
movie_2 = Movies(title="Ocean's Eleven", year="2008", genre="crime", views=90) 
movie_3 = Movies(title="The Godfather", year="1972", genre="crime", views=200)
movie_4 = Movies(title="Pulp Fiction", year="1994", genre="crime", views=120)
movie_5 = Movies(title="The Usual Suspects", year="1995", genre="crime", views=100)
series_1 = Series(title="Breaking Bad", year="2001", genre="crime", views=100, season_number=2, episode_number=3)
series_2 = Series(title="Gilmore Girls", year="2000", genre="comedy", views=50, season_number=1, episode_number=2)
series_3 = Series(title="Stranger Things", year="2016", genre="drama", views=50, season_number=2, episode_number=2)
series_4 = Series(title="How to get away with Murder", year="2014", genre="crime", views=60, season_number=1, episode_number=5)
series_5 = Series(title="Keeping up Appearances", year="1990", genre="comedy", views=30, season_number=1, episode_number=7)

list_of_all = [movie_1, movie_2, movie_3, movie_4, movie_5, series_1, series_2, series_3, series_4, series_5]

def get_movies():
    list_movies = []
    for i in list_of_all:
        if not isinstance(i, Series):
            list_movies.append(i.title)
    print(sorted(list_movies))


def get_series():
    list_series = []
    for a in list_of_all:
        if isinstance(a, Series):
            list_series.append(a.title)
    print(sorted(list_series))


def generate_views():
    c = random.choice(list_of_all)
    d = random.randint(1,100)
    c.views += d
    print(c.title, d, c.views)


def generate_views_10():
    for e in range(10):
        generate_views()


def top_titles(amount):
    by_views = sorted(list_of_all, key=lambda position: position.views, reverse=True)
    print(by_views[:amount])


def search(name):
    for g in list_of_all:
        if name == g.title:
            print(g)


print("Biblioteka filmów")
print(list_of_all)
generate_views()
print(f"Najpopularniejsze filmy i seriale w dniu {date}:")
top_titles(3)
