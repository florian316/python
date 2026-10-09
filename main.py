class Personnage:

    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def est_vivant(self):
        return self.points_de_vie > 0
    
    def subir_degats(self,degats):
        self.points_de_vie = self.points_de_vie - degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0

    def attaquer(self,cible):
        cible.subir_degats(self.force)
        return (f"{self.nom} attaque {cible.nom} et lui inflige {self.force} degats ({cible.nom}: {cible.points_de_vie} restants)")

    def __repr__(self):
        return (f"{self.nom}({self.points_de_vie} PV)")

    
gobelin = Personnage("Gobelin", 20, 5)
aldric = Personnage("Aldric", 30, 8)
print(aldric.attaquer(gobelin))
print(gobelin)
        



        



    