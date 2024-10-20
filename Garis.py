# Nama File   = Garis.py
# Deskripsi   = Membuat tipe bentukan garis 
# Nama        = Akmal Kafli Anan
# Tanggal     = 28 September 2024

# Definisi dan Spesifikasi type
# type Garis: <P1:point, P2:point>
#   {<P1,P2> adalah sebuah garis dengan P1 adalah Point1 dan P2 adalah Point2}
# 
# Definisi type
# type Point: <x:real, y:real>
#   {<x,y> adalah sebuah point dengan x adalah absis dan y adalah ordinat}

# Definisi Dan Spesifikasi Selector
# GetPoint1: Garis --> Point
#   {GetPoint1(G) memberikan Point-1 dari Garis G}
# 
# GetPoint2: Garis --> Point
#   {GetPoint2(G) memberikan Point-2 dari Garis G}
# 
# absis: point --> real
#   {absis(P) memberikan absis dari point P}
# 
# ordinat: point --> real
#   {ordinat(P) memberikan ordinat dari point P}
# Realisasi
def GetPoint1(G):
    return G[0]

def GetPoint2(G):
    return G[1]

def Getabsis(P):
    return P[0]

def Getordinat(P):
    return P[1]

# Definisi Dan Spesifikasi Konstruktor
# Make-Garis: 2point --> Garis
#   {Make_Garis(P1,P2) membentuk Garis dari P1 dan P2 dengan P1 sebagai point-1 dan P2 sebagai point-2}
# 
# Make-point: 2real --> point
#   {Make_point(X,Y) membentuk point dari x dan y dengan x sebagai absis dan y sebagai ordinat}
# Realisasi
def makeGaris(P1,P2):
    return [P1,P2]

def makePoint(x,y):
    return [x,y]

# Definisi dan Spesifikasi Operator
# Gradien: Garis --> real
#   {Gradien(G) menghitung gradien garis G}
# 
# PanjangGaris(G):
#   {PanjangGaris(G) menghitung panjang garis G}

# Definisi dan Spesifikasi Predikat
# IsSejajar: 2Garis --> boolean
#   {IsSejajar(G1,G2) benar jika G1 sejajar dengan G2}
# 
# IsTegakLurus: 2Garis --> boolean
#   {IsTegakLurus(G1,G2) benar jika G1 tegak lulus dengan G2 }

# Realisasi
def Gradien(G):
    return (Getordinat(GetPoint2(G)) - Getordinat(GetPoint1(G))) / (Getabsis(GetPoint2(G)) - Getabsis(GetPoint1(G)))

def PanjangGaris(G):
    panjang_x = Getabsis(GetPoint2(G)) - Getabsis(GetPoint1(G))
    panjang_y = Getordinat(GetPoint2(G)) - Getordinat(GetPoint1(G))
    return ((panjang_x * panjang_x) + (panjang_y * panjang_y))**0.5

def IsSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

def IsTegakLurus(G1,G2):
    return (Gradien(G1) * Gradien(G2)) == -1

# Aplikasi
print(Gradien(makeGaris(makePoint(2,3), makePoint(7,9))))
print(PanjangGaris(makeGaris(makePoint(2,3), makePoint(7,8))))
print(IsSejajar(makeGaris(makePoint(0,3),makePoint(2,7)),makeGaris(makePoint(0,-4),makePoint(2,0))))
print(IsTegakLurus(makeGaris(makePoint(1,1),makePoint(2,2)),makeGaris(makePoint(1,1),makePoint(2,0))))