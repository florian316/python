
class personnage:
    def __init__(self, name: str):
        self.name: str = name
        self.hp: int = 50
        self.mana: int =50
        self.atq: int = 10
        self.deffense: int = 5
    def attack(self,cible: "personnage") -> None:
        cible.hp -= self.atq 
    def calcul_degat(self,cible:"personnage"):
       degat = self.atq - self.deffense
    def capacite_magie(self):
        self.mana-self.atd



        



    