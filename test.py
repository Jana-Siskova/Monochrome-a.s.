import json

def floor_text(letter):
    with open("floors.json") as file:
        floors = json.load(file)
    
    return floors[letter]

print(floor_text("A"))

