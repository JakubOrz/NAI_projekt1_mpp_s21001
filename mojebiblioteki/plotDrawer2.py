import matplotlib.pyplot as plt


def drawplot(dane, nazwa="Wykres", osX="X", osY="Y"):
    if isinstance(dane, dict):
        plt.plot(dane.keys(), dane.values())

    plt.title(nazwa)
    plt.xlabel(osX, fontsize=14)
    plt.ylabel(osY, fontsize=14)
    plt.show()
