#insérer les personnages et monstres dans MongoDB.

# Creation de la base de données et des collections
# Creer une liste de monstres 
liste_monstres = [
    {"name": "ZOMBIE", "health": 70, "attack": 12, "defense": 6}, 
    {"name": "SKELETON", "health": 90, "attack": 10, "defense": 7}, 
    {"name": "GOBELIN", "health": 50, "attack": 10, "defense": 5}, 
    {"name": "TROLL", "health": 200, "attack": 25, "defense": 15}, 
    {"name": "SPECTRE", "health": 100, "attack": 18, "defense": 10},
    {"name": "VAMPIRE", "health": 150, "attack": 22, "defense": 12},
    {"name": "ORC", "health": 120, "attack": 20, "defense": 8},
    {"name": "GOLEM", "health": 250, "attack": 30, "defense": 25},
    {"name": "TROLL", "health": 200, "attack": 25, "defense": 15},
    {"name": "DRAGON", "health": 300, "attack": 35, "defense": 20}
]
# Creer une liste de personnages
liste_characters = [
    {"name": "KNIGHT", "health": 120, "attack": 17, "defense": 15}, 
    {"name": "SQUIRE", "health": 60, "attack": 8, "defense": 7}, 
    {"name": "ARCHER", "health": 90, "attack": 18, "defense": 7}, 
    {"name": "MAGE", "health": 80, "attack": 20, "defense": 5},
    {"name": "ROGUE", "health": 85, "attack": 22, "defense": 8},
    {"name": "DUELIST", "heatlh": 100, "attack": 15, "defense": 10},
    {"name": "BBERSERKER", "health": 105, "attack": 23, "defense": 6},
    {"name": "MONK", "health": 95, "attack": 19, "defense": 9}
]

# Inserer les monstres dans la collection "monstres"
# Se connecter à la base de données MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["game"]
# Obtenir la collection "monstres" de la base de données
db.monstres.drop()
db.monstres.insert_many(liste_monstres)

# insertMany
# Inserer les personnages dans la collection "personnages"
db.characters.drop()
db.characters.insert_many(liste_characters)
