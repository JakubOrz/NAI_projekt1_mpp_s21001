import sys

from PyQt5.QtWidgets import QApplication
from mojebiblioteki.BibliotekaMenu import ButtonMenu
from mojebiblioteki.controller import Controller

app = QApplication(sys.argv)

okno = ButtonMenu(name="MPP kNN by s21001")

if len(sys.argv) == 4:
    controller = Controller(okno, sys.argv[1], sys.argv[2], sys.argv[3])
else:
    controller = Controller(okno)

okno.addbutton("Dodaj zbiór treningowy", controller.learn)
okno.addbutton("Dodaj zbior testowy", controller.train)
okno.addbutton("Ocen skutecznosc", controller.testyourself)
okno.addbutton("Ocen własny kwiatek", controller.ocena)
okno.addbutton("Wykres k -> dokladnosc", controller.wykresacc)
okno.addbutton("Dodaj kwiatek do zbioru", controller.addcase)
okno.addbutton("Zmien parametr k", controller.changek)
okno.addbutton("Zmien delimiter", controller.changedelimiter)
okno.addbutton("Zresetuj zbior treningowy", controller.resettraining)
okno.addbutton("Zresetuj zbior testowy", controller.resettest)
okno.addbutton("Podziel dane na zbiory", controller.przelamdane)
app.exec_()
