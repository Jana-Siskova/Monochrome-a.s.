import json

text = ""

text_dict = {}

text_lines = text.split("\n")

for line in text_lines: 
    if line.strip() == "":
        continue

    key, value = line.split(":", 1)

    key = key.strip()
    value = value.strip()

    text_dict[key] = value

with open("card_place.json", mode="w", encoding="utf-8") as file: 
    json.dump(text_dict, file, ensure_ascii=False, indent=2)