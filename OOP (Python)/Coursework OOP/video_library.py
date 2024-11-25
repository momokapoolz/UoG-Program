#library items ae
class LibraryItem:
    def __init__(self, name, director, rating=0, play_count = 0):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
    


library = {}
library["1"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["2"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["3"] = LibraryItem("Casablanca 1", "Michael Curtiz", 2)
library["4"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["5"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)



def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
    
    
def update_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return



