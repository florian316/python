import json
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

    def to_dict(self):
        return {
            "type": "Personnage",
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force
        }
    def sauvegarder(self, chemin):
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)
        

class Heros(Personnage):
    def __init__(self, nom, points_de_vie, force, mana):
        super().__init__(nom, points_de_vie, force)
        self.mana = mana

    def competence_speciale(self, cible):
        if self.mana >=10:
            self.mana -= 10 
            cible.subir_degats(2*self.force)
            return f"{self.nom} lance sa competence sur {cible.nom} et lui inflige {2*self.force} degats ({cible.nom}: {cible.points_de_vie} restants)"
        elif self.mana < 10 :
            return f"{self.nom} n'a pas assez de mana"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Heros"
        d["mana"] = self.mana
        return d            


class Monstre(Personnage):
    def __init__(self, nom, points_de_vie, force, niveau_de_danger, butin):
        super().__init__(nom, points_de_vie, force)
        self.niveau_de_danger = niveau_de_danger
        self.butin = butin

    def attaquer(self,cible):
        degats = self.force*self.niveau_de_danger
        cible.subir_degats(degats)
        return (f"{self.nom} attaque {cible.nom} et lui inflige {degats} degats ({cible.nom}: {cible.points_de_vie} PV restants)")

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Monstre"
        d["niveau_de_danger"] = self.niveau_de_danger
        d["butin"] = self.butin
        return d 

        



    