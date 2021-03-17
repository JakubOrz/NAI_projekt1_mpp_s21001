import kNNmaker
import myFileReader


class Controller:
    dane = list()
    delimiter = ';'

    def __init__(self, inittata=None):
        if inittata is None:
            inittata = list()
        self.dane = inittata

    def __len__(self):
        return len(self.dane)

    def _makevector(self, newvector):
        if isinstance(newvector, list):
            return newvector
        elif isinstance(newvector, str):
            return newvector.split(self.delimiter)
        else:
            raise TypeError("Niepoprawny format danych")

    def learn(self, path, reset=False):
        if reset:
            self.dane.clear()
        self.dane.extend(myFileReader.readfile(path, delimiter=self.delimiter))
        return "Pomyślnie dokonano procesu nauczania"

    def addcase(self, vector):
        clearvector = self._makevector(vector)
        if (len(self.dane) > 1) & (len(clearvector) != len(self.dane[0])):
            raise ValueError("Niedopasowany wymiar wektorów")
        self.dane.extend([clearvector])

    def getdata(self):
        return self.dane

    def printdata(self, arg=None):
        for el in self.dane:
            print(el)

    def setdelimiter(self, delimiter):
        self.delimiter = delimiter

    def testyourself(self, testdata, k=3, fullraport=False, wynikprocentowy=False):
        if len(self.dane) == 0:
            print("Nie podano danych treningowych")
        else:
            print(kNNmaker.testSkutecznosci(self.dane, testdata, k, fullraport, wynikprocentowy))

    def ocena(self, vektor):
        return kNNmaker.wybierzKwiatek(self.dane, self._makevector(vektor))
