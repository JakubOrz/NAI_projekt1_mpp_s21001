import matplotlib
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.parent = parent
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Wykres(QtWidgets.QMainWindow):

    def __init__(self, dane, name="Wykres"):
        super().__init__()
        assert isinstance(dane, dict)
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot(dane.keys(), dane.values())
        self.setWindowTitle(name)
        self.setCentralWidget(sc)
        self.show()
