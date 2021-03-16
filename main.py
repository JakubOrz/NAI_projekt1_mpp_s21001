import myFileReader
import kNNmaker

PATH = "/home/jakub/Uczelnia/NAI/MPP/MPP 1/iris.csv"
PATH2 = "/home/jakub/Uczelnia/NAI/MPP/MPP 1/"
PATH3 = "treningowe.csv"

dane = myFileReader.__readfile(PATH)
# myFileReader.splitdata(PATH, PATH2 + "danetreningowe.csv", PATH2 + "danetestowe1.csv", 35)

wektorZero = [5.1, 3.2, 0.9, 0.1]

for odl in kNNmaker.__createdistancelist(dane, wektorZero, k=5):
    print(odl)
