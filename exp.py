class Bird:
    """un oiseau"""
    def __init__(self) -> None:
        """les attributs définis ici sont des attributs d'instance"""
        self.wings=2
    def fly(self):
        """Cette méthode est une méthode d'instance"""
        print("Je vole!")
bird=Bird() #Obligations d'instantier un oiseau pour utiliser ses attributs
bird.wings
bird.fly()

