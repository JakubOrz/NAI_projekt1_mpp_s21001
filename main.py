import myFileReader
import kNNmaker
from controller import Controller

PATH = "/home/jakub/Uczelnia/NAI/MPP/MPP 1/"
PATH3 = "treningowe.csv"

dane = myFileReader.__readfile(PATH+"danetreningowe.csv")
testowe = myFileReader.__readfile(PATH+"danetestowe1.csv")


kontroler = Controller(dane)
kontroler.testyourself(testowe,4,False,True)

