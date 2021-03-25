import matplotlib.pyplot as plt


def drawplot(dane, nazwa="Wykres", osx="X", osy="Y"):
    if isinstance(dane, dict):
        plt.plot(dane.keys(), dane.values())

    plt.title(nazwa)
    plt.xlabel(osx, fontsize=14)
    plt.ylabel(osy, fontsize=14)
    plt.show()
