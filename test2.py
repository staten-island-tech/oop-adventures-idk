import random
items = [
    {
        "id": 1,
        "name": "Twig",
        "atk": 5,  
        "type": "weapon",
    },
    {
        "id": 2,
        "name": "Glock",
        "atk": 10,
        "type": "weapon",
    },
    {
        "id": 3,
        "name": "Textbook Troika",
        "atk": 20,
        "type": "weapon",
    },
    {
        "id": 4, 
        "name": "Duck",
        "def": 10,
        "type": "armor",
    },
    {
        "id": 5, 
        "name": "Car",
        "def": 20,
        "type": "armor",
    },
    {
        "id": 7, 
        "name": "Excalibur",
        "atk": 1,
        "type": "weapon",
    },
    {
        "id": 8, 
        "name": "Impenetrable Armor",
        "def": 1,
        "type": "armor",
    },
    {
        "id": 9, 
        "name": "Pebble",
        "atk": 25,
        "type": "weapon",
    },
]
for i in items:
    armorquip=[i]["type"]["armor"]["hp"]["name"]
