def __countdst(vektor1, vektor2):
    # upewniam się że wymiary wektorów są zgodne
    if len(vektor1) != len(vektor2):
        raise ValueError("Niezgodne wymiary wektorów")
    # obliczam różnicę w każdym z wymiarów
    vektor3 = [abs(float(v1) - float(v2)) for v1, v2 in zip(vektor1, vektor2)]
    # obliczam kwadrat odległości wektorów
    return sum([element ** 2 for element in vektor3])


def __nametagdata(vektor1, vektor2):
    return [vektor1[-1], __countdst(vektor1[:-1], vektor2)]
    # do policzonej odległości dopisuję kategorię jakiej się tyczy


def __createdistancelist(vectorslist, vector0, k=3):
    distanceList = [__nametagdata(vektor, vector0) for vektor in vectorslist]
    return sorted(distanceList, key=lambda l: l[-1])[:k]
# funkcja tworzy listę k najbliższych wektorów względem wektora zerowego domyślnie k wynosi 3
