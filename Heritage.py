class Film:
    def __init__(self,name) -> None:
        self.name=name
    def watch(self):
        print("Bon voisinnage!")
class FilmCassette(Film):
    pass

film=Film("2001:L'odyssée de l'espace")
film_Cassette= FilmCassette("Blade Runner")

film.name
film.watch()

film_Cassette.name
film_Cassette.watch()

