import json
#"r" => read
#"w" => write
#"a" => append

file = open("./contacts.json", "r")
data: list = json.load(file)
new_contact = {
    "nom": " julie",
    "prenom": "pignon",
    "adresse": " 1 allée jean giraudoux, 21000 dijon",
    "numero": "06834527"
}



def read_json(fichier_json):
    with open(fichier_json, "r") as f: 
        return json.load(f)



def write_json(ajouter,fichier_json ):
    with open(fichier_json, "w", encoding = "utf-8") as r:
        json.dump(ajouter,r)

def find_contacte():
    pass

  

