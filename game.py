import json

def floor_text(floor):
    with open("floors.json", encoding="utf-8") as floors_file:
        floors = json.load(floors_file)
    
    return floors[floor]

def places_text(number):
    with open("places.json", encoding="utf-8") as places_file:
        places = json.load(places_file)
    
    return places[number]

def card_card_text(number_number):
    with open("card_card.json", encoding="utf-8") as card_card_file:
        card_card = json.load(card_card_file)
    
    return card_card[number_number]

def card_place_text(number_place):
    with open("card_place.json", encoding="utf-8") as card_place_file:
        card_place = json.load(card_place_file)
    
    return card_place[number_place]

activity = input('''Jaký bude tvůj další krok?
                     
Chci prozkoumat patro. (1)
Chci prozkoumat pozici v místnosti. (2)
Chci zkombinovat karty dobrodružství. (3)
Chci zkombinovat kartu dobrodružství s místem. (4) 
                                    
Tvůj výběr: ''')

if activity == "1":
    letter = input("Zadej patro: ")
    print(floor_text(letter))

if activity == "2":
    place = input("Zadej číslo místa: ")
    print(places_text(place))

if activity == "3":
    card_card = input("Zadej kombinaci karet: ")
    print(card_card_text(card_card))

if activity == "4":
    card_place = input("Zadej kombinace karty a místa: ")
    print(card_place_text(card_place))

else: 
    print('''Byla zadaná jiná hodnota. Zadaj jednu z možností:
Chci prozkoumat patro. (1)
Chci prozkoumat pozici v místnosti. (2)
Chci zkombinovat karty dobrodružství. (3)
Chci zkombinovat kartu dobrodružství s místem. (4) 
                                    
Tvůj výběr: ''')

