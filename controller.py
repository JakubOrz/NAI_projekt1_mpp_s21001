import kNNmaker


class Controller:
    dane = list()

    def __init__(self, inittata):
        self.dane = inittata

    def learn(self, newdata, reset=False):
        if reset:
            self.dane = list()
        self.dane.extend(newdata)

    def getdata(self):
        return self.dane

    def testyourself(self, testdata, k=3, fullraport=False, wynikprocentowy=False):
        if len(self.dane) == 0:
            print("Nie podano danych treningowych")
        else:
            print(kNNmaker.testSkutecznosci(self.dane, testdata, k, fullraport, wynikprocentowy))
