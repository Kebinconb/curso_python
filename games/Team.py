'''
    Clase Team: Equipo
'''
from Athlete import Athlete
from Sport import Sport
class Team:
    """ Clase para representar un equipo"""
    def __init__(self, name:str,sport:Sport,players:list):
        """ Constructor de la clase Team """
        self.name = name
        self.sport = sport
        self.players = players
        def __str__(self):
            """ Mètodo para representar la clase como string"""
            return f"Team: {self.name}, {self.sport}, {self.players}"
        def __repr__(self):
            """ Mètodo para representar la clase como string"""
            return f"Team:(name= {self.name}, sport= {self.sport}, player ={self.players})"
        def to_json(self):
            """ Mètodo para representar la clase como diccionario"""
            return {"name": self.name, "sport": self.sport.to_json(), "players": [p.to_json() for p in self.players]}
if __name__ == '__main__':
    a1 = Athlete("Michael Jordan")
    a1 = Athlete("Michael Jordan")
    a1 = Athlete("Michael Jordan")
    a1 = Athlete("Michael Jordan")
    a1 = Athlete("Michael Jordan")
    
        