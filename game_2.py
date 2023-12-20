from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
from functools import partial
import json
import sys

def load_json(json_file):
        with open(json_file, encoding="utf-8") as file:
            data = json.load(file)
        return data

# define text variables
welcome_text = "Vítej v Adventure Games: Monochrome a.s."
play_text = "Jaký bude tvůj další krok?"
choice_text_1 = "Chci prozkoumat patro."
choice_text_2 = "Chci prozkoumat pozici v místnosti."
choice_text_3 = "Chci zkombinovat karty dobrodružství."
choice_text_4 = "Chci zkombinovat kartu dobrodružství s místem."

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.initUI()
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("Adventure Games: Monochrome a.s.")
    
    def initUI(self):
        self.welcome_label = QtWidgets.QLabel(self)
        self.welcome_label.setText(welcome_text)
        self.welcome_label.move(10, 50)
        self.welcome_label.adjustSize()

        self.play_label = QtWidgets.QLabel(self)
        self.play_label.setText(play_text)
        self.play_label.move(10, 100)
        self.play_label.adjustSize()

        self.text_label = QTextEdit(self)
        self.text_label.setReadOnly(True)  # Make it read-only
        self.text_label.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.text_label.setGeometry(10, 407, 580, 100)

        self.choice_button_1 = QtWidgets.QPushButton(self)
        self.choice_button_1.setText(choice_text_1)
        self.choice_button_1.move(10, 150)
        self.choice_button_1.resize(300, 40)
        self.choice_button_1.clicked.connect(partial(self.clicked, "Choice_1"))

        self.choice_button_2 = QtWidgets.QPushButton(self)
        self.choice_button_2.setText(choice_text_2)
        self.choice_button_2.move(10, 200)
        self.choice_button_2.resize(300, 40)
        self.choice_button_2.clicked.connect(partial(self.clicked, "Choice_2"))

        self.choice_button_3 = QtWidgets.QPushButton(self)
        self.choice_button_3.setText(choice_text_3)
        self.choice_button_3.move(10, 250)
        self.choice_button_3.resize(300, 40)
        self.choice_button_3.clicked.connect(partial(self.clicked, "Choice_3"))

        self.choice_button_4 = QtWidgets.QPushButton(self)
        self.choice_button_4.setText(choice_text_4)
        self.choice_button_4.move(10, 300)
        self.choice_button_4.resize(300, 40)
        self.choice_button_4.clicked.connect(partial(self.clicked, "Choice_4"))

        self.textbox_1 = QLineEdit(self)
        self.textbox_1.move(320, 157)
        self.textbox_1.resize(270,25)

        self.textbox_2 = QLineEdit(self)
        self.textbox_2.move(320, 207)
        self.textbox_2.resize(270,25)

        self.textbox_3 = QLineEdit(self)
        self.textbox_3.move(320, 257)
        self.textbox_3.resize(270,25)

        self.textbox_4 = QLineEdit(self)
        self.textbox_4.move(320, 307)
        self.textbox_4.resize(270,25)
        
    def clicked(self, value):
        if value == "Choice_1":
            input = self.textbox_1.text()
            source = load_json("floors.json")
            def floor_text(floor, floors):
                return floors.get(floor, "Neplatné patro.")
            text = floor_text(input, source)
            self.text_label.setPlainText(text)
        elif value == "Choice_2":
            input = self.textbox_2.text()
            source = load_json("places.json")
            def places_text(number, places):
                return places.get(number, "Neplatná pozice.")
            text = places_text(input, source)
            self.text_label.setPlainText(text)
        elif value == "Choice_3":
            input = self.textbox_3.text()
            source = load_json("card_card.json")
            def card_card_text(number_number, card_combinations):
                return card_combinations.get(number_number, "Neplatná kombinace karet.")
            text = card_card_text(input, source)
            self.text_label.setPlainText(text)
        elif value == "Choice_4":
            input = self.textbox_4.text()
            source = load_json("card_place.json")
            def card_place_text(number_place, place_combinations):
                return place_combinations.get(number_place, "Neplatná kombinace karty a místa.")
            text = card_place_text(input, source)
            self.text_label.setPlainText(text)
            
        self.update()
    
    def update(self):
        self.welcome_label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = my_window()

    win.show()
    sys.exit(app.exec())

window()