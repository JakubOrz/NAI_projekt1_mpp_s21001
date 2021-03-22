from mojebiblioteki import kNNcore
from mojebiblioteki import myFileReader


class Controller:

    def __init__(self, parent, initk=3, inittata=None, trainingset=None):
        if inittata is None:
            self.dane = list()
        else:
            self.dane = myFileReader.readfile(inittata, ';')
        if trainingset is None:
            self.trainingset = list()
        else:
            self.trainingset = myFileReader.readfile(trainingset, ';')
        self.parent = parent
        self.paramK = int(initk)
        self.delimiter = ';'

    def __len__(self):
        return len(self.dane)

    def __str__(self):
        return f"Ilość danych treningowych: {len(self.dane)}\n" \
               f"Ilość danych testowych: {len(self.trainingset)}\n" \
               f"Parametr k: {self.paramK}\n" \
               f"Delimiter: {self.delimiter}"

    def _makevector(self, newvector):
        if isinstance(newvector, list):
            return newvector
        elif isinstance(newvector, str):
            return newvector.split(self.delimiter)
        else:
            raise TypeError("Niepoprawny format danych")

    def learn(self):
        path, cancel = self.parent.collectdata("Nauka", "Podaj ścieżkę do pliku CSV")
        if cancel:
            return
        self.dane.extend(myFileReader.readfile(path, delimiter=self.delimiter))
        return "Nauka z pliku zakończona pomyślnie"

    def train(self):
        path, cancel = self.parent.collectdata("Testy", "Podaj ścieżkę do pliku CSV z zbiorem testowym")
        if cancel:
            return
        self.trainingset.extend(myFileReader.readfile(path, delimiter=self.delimiter))
        return "Nauka z pliku zakończona pomyślnie"

    def changek(self):
        paramk, cancel = self.parent.collectdata("Zmiana k", "Podaj nowe K")
        if cancel or paramk < 0:
            return
        self.paramK = int(paramk)
        return f"Parametr k zmieniony na {self.paramK}"

    def changedelimiter(self):
        delimiter, cancel = self.parent.collectdata("Zmiana delimitera", "Podaj nowy delimiter")
        if cancel and len(delimiter) != 1:
            return
        self.delimiter = delimiter
        return f"Delimiter zmieniony na {self.delimiter}"

    def resettraining(self):
        self.dane.clear()
        return "Zbiór treningowy wyczyszczony"

    def resettest(self):
        self.trainingset.clear()
        return "Zbiór testowy wyczyszczony"

    def addcase(self):

        if len(self.dane) == 0:
            iletrzeba = ""
        else:
            iletrzeba = len(self.dane[0]) - 1

        vektor, cancel = self.parent.collectdata("Dodawanie kwiatka",
                                                 f"Podaj {iletrzeba} parametry kwiatka oraz"
                                                 f" atrybut decyzyjny oddzielone {self.delimiter} ")
        if cancel:
            return

        clearvector = self._makevector(vektor)

        if (len(self.dane) > 0) and (len(clearvector) != len(self.dane[0])):
            return "Niedopasowany wymiar wektorów"
        self.dane.extend([clearvector])
        return "Dodano element do zbioru treningowego"

    def getdata(self):
        return self.dane

    def testyourself(self):
        if len(self.dane) == 0 or len(self.trainingset) == 0:
            return "Nie podano danych treningowych lub testowych"
        else:
            return f"Skuteczność dla k = {self.paramK} wynosi " \
                   f"{kNNcore.testSkutecznosci(self.dane, self.trainingset, self.paramK, False, True)}"

    def ocena(self):
        if len(self.dane) == 0:
            return "Pusty zbiór treningowy"

        vektor, cancel = self.parent.collectdata("Testowanie Irysa",
                                                 f"Podaj {len(self.dane[0]) - 1} parametry"
                                                 f" kwiatka oddzielone {self.delimiter} ")
        if cancel:
            return

        clearvektor = self._makevector(vektor)
        if len(self.dane[0]) != len(clearvektor) + 1:
            return "Nieprawidłowa ilość parametrów"

        return kNNcore.wybierzKwiatek(self.dane, clearvektor)

    def wykresacc(self):

        dane, cancel = self.parent.collectdata("Przygotowywanie wykresu",
                                               f"Podaj przedział kMIN{self.delimiter}kMAX dla którego rysować mam "
                                               f"rysować wykres")
        if cancel:
            return

        przedzial = dane.split(self.delimiter)

        if len(przedzial) != 2:
            return

        if int(przedzial[0]) < 1 or int(przedzial[1]) < int(przedzial[0]):
            return

        wyniki = dict()
        for k in range(int(przedzial[0]), int(przedzial[1]), 1):
            wyniki[k] = kNNcore.testSkutecznosci(self.dane, self.trainingset, k, fullRaport=False,
                                                 wynikProcentowy=False)
        return wyniki

    def przelamdane(self):

        danepath, cancel = self.parent.collectdata("Przygotowywanie danych",
                                               f"Podaj ścieżkę do pliku csv z danymi")
        if cancel:
            return

        trainpath, cancel = self.parent.collectdata("Przygotowywanie danych",
                                                   f"Podaj ścieżkę gdzie utworzyć zbiór treningowy")
        if cancel:
            return

        testpath, cancel = self.parent.collectdata("Przygotowywanie danych",
                                                    f"Podaj ścieżkę gdzie utworzyć zbiór testowy")
        if cancel:
            return

        ilosc, cancel = self.parent.collectdata("Przygotowywanie danych",
                                                   f"Podaj ilość danych dla każdego atrybutu decyzyjnego")
        if cancel:
            return

        return myFileReader.splitcsvdata(danepath, trainfilepath=trainpath, testfilepath=testpath, testowe=int(ilosc))
