import sys
from mojebiblioteki import plotDrawer2
from mojebiblioteki.controller import Controller
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QInputDialog

class Menu(QWidget):

    def __init__(self, argsy, parent=None):
        super().__init__(parent)
        if len(argsy) == 4:
            self.controller = Controller(parent=self, initk= argsy[1], inittata= argsy[2], trainingset= argsy[3])
        else:
            self.controller = Controller(parent=self)
        self.interfejs(self.controller)


    def collectdata(self, inputname, message):
        text , ok = QInputDialog.getText(self, inputname, message)
        return text , not ok

    def handlebutton(self):
        sender = self.sender()

        funkcje = {'Dodaj zbior treningowy':self.controller.learn,
                   'Dodaj zbior testowy':self.controller.train,
                   'Zmien parametr k':self.controller.changek,
                   'Zmien delimiter':self.controller.changedelimiter,
                   'Zresetuj zbior treningowy':self.controller.resettraining,
                   'Zresetuj zbior testowy': self.controller.resettest,
                   'Ocen kwiatek': self.controller.ocena,
                   'Ocen skutecznosc':self.controller.testyourself,
                   'Dodaj kwiatek':self.controller.addcase,
                   'Wykres k -> dokladnosc':self.controller.wykresacc,
                   'Podziel dane na zbiory':self.controller.przelamdane
                   }

        try:
            callbackdata = funkcje.get(sender.text())()

            self.learntcount.setText(str(self.controller))

            if isinstance(callbackdata,dict):
                plotDrawer2.drawplot(callbackdata, nazwa="Wykres zależności dokładności od k", osx="Parametr K",
                                     osy="Accuracy")
            else:
                self.outputdata.setText(callbackdata)

        except Exception as ex1:
            self.outputdata.setText("Błąd! "+str(ex1))

    def interfejs(self, controller):

        self.resize(400, 100)
        self.setWindowTitle("kNN Menu - s21001")

        layout = QGridLayout()

        self.setLayout(layout)

        self.learntcount = QLabel(str(controller), self)
        self.outputdata = QLabel("", self)

        layout.addWidget(self.learntcount, 0, 0)

        guziczki = list()

        guziczki.append(QPushButton("Ocen kwiatek",self))
        guziczki.append(QPushButton("Ocen skutecznosc",self))
        guziczki.append(QPushButton("Dodaj zbior treningowy", self))
        guziczki.append(QPushButton("Dodaj zbior testowy",self))
        guziczki.append(QPushButton("Wykres k -> dokladnosc", self))
        guziczki.append(QPushButton("Dodaj kwiatek", self))
        guziczki.append(QPushButton("Zmien parametr k", self))
        guziczki.append(QPushButton("Zmien delimiter", self))
        guziczki.append(QPushButton("Zresetuj zbior treningowy", self))
        guziczki.append(QPushButton("Zresetuj zbior testowy", self))
        guziczki.append(QPushButton("Podziel dane na zbiory",self))

        for i, guzik in enumerate(guziczki):
            guzik.clicked.connect(self.handlebutton)
            layout.addWidget(guzik,i+1,0)

        layout.addWidget(self.outputdata,len(guziczki)+2,0)

        self.show()

app = QApplication(sys.argv)
okno = Menu(sys.argv)
sys.exit(app.exec_())
