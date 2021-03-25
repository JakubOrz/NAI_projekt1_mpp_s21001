import sys

from PyQt5.QtWidgets import QApplication
from mojebiblioteki.BibliotekaMenu import ButtonMenu
from mojebiblioteki.controller import Controller

app = QApplication(sys.argv)

okno = ButtonMenu(initinfo="Siemka")

if len(sys.argv) == 4:
    controller = Controller(okno, sys.argv[1], sys.argv[2], sys.argv[3])
else:
    controller = Controller(okno)

okno.addbutton("Dodaj zbior testowy", controller.train)
okno.addbutton("Zmien parametr k", controller.changek)
okno.addbutton("Zmien delimiter", controller.changedelimiter)
okno.addbutton("Zresetuj zbior treningowy", controller.resettraining)
okno.addbutton("Zresetuj zbior testowy", controller.resettest)
okno.addbutton("Ocen kwiatek", controller.ocena)
okno.addbutton("Ocen skutecznosc", controller.testyourself)
okno.addbutton("Dodaj kwiatek", controller.addcase)
okno.addbutton("Wykres k -> dokladnosc", controller.wykresacc)
okno.addbutton("Podziel dane na zbiory", controller.przelamdane)
app.exec_()
