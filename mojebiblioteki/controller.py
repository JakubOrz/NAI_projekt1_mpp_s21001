from mojebiblioteki import kNNcore
from mojebiblioteki import myFileReader
from mojebiblioteki import BibliotekaMenu


class Controller:

    def __init__(self, parent, initk=3, inittata=None, trainingset=None):
        assert isinstance(parent, BibliotekaMenu.ButtonMenu)
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

        self._refresh()

    def __len__(self):
        return len(self.dane)

    def __str__(self):
        return f"Ilość danych treningowych: {len(self.dane)}\n" \
               f"Ilość danych testowych: {len(self.trainingset)}\n" \
               f"Parametr k: {self.paramK}\n" \
               f"Delimiter: {self.delimiter}"

    def _refresh(self):
        self.parent.changetext(str(self))

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
        self._refresh()
        self.parent.showdata("Nauka z pliku zakończona pomyślnie")

    def train(self):
        path, cancel = self.parent.collectdata("Testy", "Podaj ścieżkę do pliku CSV z zbiorem testowym")
        if cancel:
            return
        self.trainingset.extend(myFileReader.readfile(path, delimiter=self.delimiter))

        self._refresh()
        self.parent.showdata("Zbiór testowy pomyślnie dodany")

    def changek(self):
        paramk, cancel = self.parent.collectdata("Zmiana k", "Podaj nowe K")
        if cancel or int(paramk) < 0:
            return
        self.paramK = int(paramk)

        self._refresh()
        self.parent.showdata(f"Parametr k zmieniony na {self.paramK}")

    def changedelimiter(self):
        delimiter, cancel = self.parent.collectdata("Zmiana delimitera", "Podaj nowy delimiter")
        if cancel and len(delimiter) != 1:
            return
        self.delimiter = delimiter

        self._refresh()
        self.parent.showdata(f"Delimiter zmieniony na {self.delimiter}")

    def resettraining(self):
        self.dane.clear()
        self._refresh()
        self.parent.showdata("Zbiór treningowy wyczyszczony")

    def resettest(self):
        self.trainingset.clear()
        self._refresh()
        self.parent.showdata("Zbiór testowy wyczyszczony")

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
            self.parent.showdata("Niedopasowany wymiar wektorów")
            return
        self.dane.extend([clearvector])
        self._refresh()
        self.parent.showdata("Dodano element do zbioru treningowego")

    def testyourself(self):
        if len(self.dane) == 0 or len(self.trainingset) == 0:
            self.parent.showdata("Nie podano danych treningowych lub testowych")
            return
        else:
            self.parent.showdata(f"Skuteczność dla k = {self.paramK} wynosi " 
                                 f"{kNNcore.testSkutecznosci(self.dane, self.trainingset, self.paramK, False, True)}")
            return

    def ocena(self):
        if len(self.dane) == 0:
            self.parent.showdata("Pusty zbiór treningowy")
            return

        vektor, cancel = self.parent.collectdata("Testowanie Irysa",
                                                 f"Podaj {len(self.dane[0]) - 1} parametry"
                                                 f" kwiatka oddzielone {self.delimiter} ")
        if cancel:
            return

        clearvektor = self._makevector(vektor)
        if len(self.dane[0]) != len(clearvektor) + 1:
            self.parent.showdata("Nieprawidłowa ilość parametrów")
            return
        self.parent.showdata(f"Na podstawie danych uważam, że to: {kNNcore.wybierzKwiatek(self.dane, clearvektor)}")
        return

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
        self.parent.drawplot(wyniki, "Wykres dokładności w zależności od k", "k", "Dokładność")

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
