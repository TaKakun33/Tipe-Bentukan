def makePoint(x,y):
    return [x,y]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def makeGaris(P1,P2):
    return [P1,P2]

def Point1(G):
    return G[0]

def Point2(G):
    return G[1]

def Gradien(G):
    if absis(Point2(G)) == absis(Point1(G)):
        return None
    else:
        return (ordinat(Point2(G)) - ordinat(Point1(G))) / (absis(Point2(G)) - absis(Point1(G)))

def PanjangGaris(G):
    panjang_x = absis(Point2(G)) - absis(Point1(G))
    panjang_y = ordinat(Point2(G)) - ordinat(Point1(G))
    return ((panjang_x * panjang_x) + (panjang_y * panjang_y))**0.5

def isSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

def isTegakLurus(G1,G2):
    if Gradien(G1) == None or Gradien(G2) == None:
        return None
    else:
        return (Gradien(G1) * Gradien(G2)) == -1

print(Gradien(makeGaris(makePoint(2,3), makePoint(2,3))))
print(isTegakLurus(makeGaris(makePoint(1,1),makePoint(2,2)),makeGaris(makePoint(1,1),makePoint(2,0))))