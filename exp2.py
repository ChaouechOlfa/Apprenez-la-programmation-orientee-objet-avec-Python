class Bird:
    #ici on utilise deux attributs de classe
    names=("mouette","pigeon","moineau","hirrondelle")
    positions={}

    def __init__(self,name) -> None:
        """les attributs définis ici sont des attributs d'instance"""
        self.position=1,2
        print(self.position)
        self.name=name
    # On accède à l'attribut de classe "positions" avec self (c'est possible)
        self.positions[self.position]=self.name
    @classmethod
    def find_bird(cls,position):
        """Retrouve un oiseau selon position donnée"""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]}!"
        return "On a rien trouvé..."
    #On peut accéder aux variables de classe sans instanciation
print(Bird.names)
print(Bird.positions)
print(Bird.find_bird((1,3)))
    #On instance un oiseau
bird=Bird("moineau")
#On le retrouve avec la méthode find_bird
print(Bird.find_bird((1,2)))
