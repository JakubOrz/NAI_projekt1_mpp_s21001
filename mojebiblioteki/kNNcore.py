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


def __createdistancelist(vectorslist, vector0, k):
    distanceList = [__nametagdata(vektor, vector0) for vektor in vectorslist]
    return sorted(distanceList, key=lambda l: l[-1])[:k]
# funkcja tworzy listę k najbliższych wektorów względem wektora zerowego domyślnie k wynosi 3

def __maxelement(slownik):
    assert isinstance(slownik, dict)
    klucze = [*slownik]
    best = klucze[0]
    for klucz in klucze[1:]:
        if slownik[klucz] > slownik[best]:
            best = klucz
    return best

def __decide(closestVectors):
    decisionssttr = dict()
    for vector in closestVectors:
        if decisionssttr.get(vector[0]) is None:
            decisionssttr[vector[0]]=0
        decisionssttr[vector[0]]+=1

    return __maxelement(decisionssttr)


def wybierzKwiatek(data,vector,k=3):
    return __decide(__createdistancelist(data,vector,k))


def testSkutecznosci(daneTreningowe,daneTestowe,k=3, fullRaport = False, wynikProcentowy = False):
    skuteczne = 0
    for przypadek in daneTestowe:
        rezultat = wybierzKwiatek(daneTreningowe,przypadek[:-1],k)
        if rezultat == przypadek[-1]:
            skuteczne+=1
        if fullRaport:
            print("Oczekiwano: ",przypadek[-1]," otrzymano: ",rezultat," zgodność: ", rezultat==przypadek[-1])
    if wynikProcentowy:
        return ""+str(round(skuteczne/len(daneTestowe)*100,2))+"%"
    else:
        return skuteczne/len(daneTestowe)