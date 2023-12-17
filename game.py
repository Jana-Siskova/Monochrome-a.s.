import json

# Function that loads json file
def load_json(json_file):
    with open(json_file, encoding="utf-8") as file:
        data = json.load(file)
    return data

# Functions that loads text from json files
def floor_text(floor, floors):
    return floors.get(floor, "Neplatné patro.")

def places_text(number, places):
    return places.get(number, "Neplatná pozice.")

def card_card_text(number_number, card_combinations):
    return card_combinations.get(number_number, "Neplatná kombinace karet.")

def card_place_text(number_place, place_combinations):
    return place_combinations.get(number_place, "Neplatná kombinace karty a místa.")


def main():
    floors = load_json("floors.json")
    places = load_json("places.json")
    card_combinations = load_json("card_card.json")
    place_combinations = load_json("card_place.json")

    while True:
        activity = input('''Jaký bude tvůj další krok?
                     
    Chci prozkoumat patro. (1)
    Chci prozkoumat pozici v místnosti. (2)
    Chci zkombinovat karty dobrodružství. (3)
    Chci zkombinovat kartu dobrodružství s místem. (4) 
    Chci ukončit hru. (exit)
                                    
    Tvůj výběr: ''').strip().lower()

        if activity == "1":
            letter = input("Zadej patro: ").upper().strip()
            print(floor_text(letter, floors))

        elif activity == "2":
            place = input("Zadej číslo místa: ").strip()
            print(places_text(place, places))

        elif activity == "3":
            card_card = input("Zadej kombinaci karet: ").strip()
            print(card_card_text(card_card, card_combinations))

        elif activity == "4":
            card_place = input("Zadej kombinaci karty a místa: ").strip()
            print(card_place_text(card_place, place_combinations))
        
        elif activity == "exit":
            print("Konec hry.")
            break

        else:
            print("Neplatná hodnota. Zadej číslo 1-4 nebo ukonči hru.")

if __name__ == "__main__":
    main()
