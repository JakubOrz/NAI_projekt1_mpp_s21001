import csv


# metoda wenątrzna której zadaniem jest czytanie pliku celem dalszej obróbki
def __readfile(filepath, delimiter=';'):
    with open(filepath, newline='') as plik:
        dane = list(csv.reader(plik, delimiter=delimiter))
        # usuwa ostatni pusty element
        dane.pop()
        return dane


# metoda która dzieli mi dane na zbiory testowy i treningowy
def splitdata(filepath, trainfilepath, testfilepath, testowe=10):
    try:
        dane = __readfile(filepath)
    except FileNotFoundError:
        print("Nie odnaleziono pliku")
        return

    attrdecyzyjne = dict()
    for wyraz in dane:
        if attrdecyzyjne.get(wyraz[-1]) is None:
            attrdecyzyjne[wyraz[-1]] = list()

        attrdecyzyjne.get(wyraz[-1]).append(wyraz[:-1])

    # dokonuję podziału zbioru danych na testowe i treningowe
    with open(trainfilepath, 'w', newline='') as csvtrainfile, open(testfilepath, 'w', newline='') as csvtestfile:
        trainwriter = csv.writer(csvtrainfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        testwriter = csv.writer(csvtestfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for decisionattr in attrdecyzyjne.keys():

            for singledata in attrdecyzyjne.get(decisionattr)[:testowe]:
                trainwriter.writerow(singledata + [decisionattr])

            for singledata in attrdecyzyjne.get(decisionattr)[testowe:]:
                testwriter.writerow(singledata + [decisionattr])
    print("Dane treningowe podzielone na: ",testowe, "danych z każdej grupy jako trening, pozostałe jako testowe")