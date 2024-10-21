# Nama File   = Pecahan Campuran.py
# Deskripsi   = Membuat tipe bentukan Pecahan campuran 
# Nama        = akmal kafli anan
# Tanggal     = 21 Oktober 2024

# Definisi Dan Spesifikasi type
# type PecahanC: <bil:Integer, n:Integer>=0, d:Integer>0>
#   {<bil,n,d> adalah sebuah Pecahan Campuran dengan bil adalah Bilangan, n adalah Pembilang, d adalah Penyebut}
# 
# type Pecahan: <n:Integer>=0, d:Integer>0>
#   {<,n,d> adalah sebuah Pecahan dengan n adalah Pembilang, d adalah Penyebut}

# Definisi dan Spesifikasi Selektor
# GetBil: PecahanC --> Integer
#   {(GetBil(Pc) memberikan Bilangan bulat dari pecahan campuran tsb)}
# 
# GetPemb: PecahanC --> Integer >= 0
#   {(GetPemb(Pc) memberikan Pembilang dari pecahan campuran tsb)}
# 
# GetPeny: PecahanC --> Integer > 0
#   {(GetPeny(Pc) memberikan Penyebut dari pecahan campuran tsb)}

# Realisasi Selektor
def getBil(Pc):
    return Pc[0]

def getPemb(Pc):
    return Pc[1]

def getPeny(Pc):
    return Pc[2]

# Definisi dan Spesifikasi Konstrukstor
# makePc: Integer, Integer >= 0, Integer > 0 --> PecahanC
#   {(makePc(Pc) Membentuk Pecahan Campuran dengan Bil merupakan bilangan, n merupakan pembilang, dan d merupakan penyebut
# 
# makeP: Integer, Integer >= 0, Integer > 0 --> PecahanC
#   {(makeP(Pc) Membentuk Pecahan dengan n merupakan pembilang, dan d merupakan penyebut

# Realisasi Konstruktor
def makePc(b,n,d):
    return [b,n,d]

def makeP(n,d):
    return [n,d]

# Definisi dan Spesifikasi Operator
# KonvensiP: PecahanC --> Pecahan
#   {KonvensiP(Pc) : mengubah pecahan campuran P ke tipe pecahan biasa dan jika pecahan bernilai negatif, nilai negatif dilekatkan pada pembilang}
# 
# KonvensiReal: PecahanC --> real
#   {KonvensiReal(Pc) : mengubah pecahan campuran P menjadi nilai real}
# 
# AddP: 2 PecahanC --> PecahanC
#   {AddP(P1,P2) menjumlahkan pecahan campuran P1 dan P2}
# 
# SubP: 2 PecahanC --> PecahanC
#   {SubP(P1,P2) mengurangkan pecahan campuran P1 dan P2}
# 
# DivP: 2 PecahanC --> PecahanC
#   {DivP(P1,P2) membagi pecahan campuran P1 dan P2}
# 
# MulP: 2 PecahanC --> PecahanC
#   {MulP(P1,P2) mengalikan pecahan campuran P1 dan P2}

# Definisi dan Spesifikasi Predikat
# IsEqP: PecahanC --> boolean
#   {IsEqP(P1,P2): membandingkan apakah P1 sama dengan P2}
# 
# IsLtP: PecahanC --> boolean
#   {IsLtP(P1,P2): membandingkan apakah P1 lebih kecil P2}
# 
# IsGtP: PecahanC --> boolean
#   {IsGtP(P1,P2): membandingkan apakah P1 lebih besar P2}

# Realisasi
def konvesiP(Pc):
    if getBil(Pc) > 0:
        return makeP(getBil(Pc)*getPeny(Pc) + getPemb(Pc),getPeny(Pc))
    else:
        return makeP(getBil(Pc)*getPeny(Pc) - getPemb(Pc),getPeny(Pc))

def konvesiReal(Pc):
    if getBil(Pc) > 0:
        return getBil(Pc)+(getPemb(Pc)/getPeny(Pc))
    else:
        return getBil(Pc)-(getPemb(Pc)/getPeny(Pc))

def AddP(Pc1,Pc2):
    return(makePc(getBil(Pc1) + getBil(Pc2),getPemb(Pc1)*getPeny(Pc2) + getPemb(Pc2)*getPeny(Pc1),getPeny(Pc1)*getPeny(Pc2)))

def SubP(Pc1,Pc2):
    return(makePc(getBil(Pc1) - getBil(Pc2),getPemb(Pc1)*getPeny(Pc2) - getPemb(Pc2)*getPeny(Pc1),getPeny(Pc1)*getPeny(Pc2)))

def DivP(Pc1,Pc2):
    pembX2 = (getPeny(Pc1)*getBil(Pc1) + getPemb(Pc1)) * (getPeny(Pc2))
    penyX2 = (getPeny(Pc1)) * (getPeny(Pc2)*getBil(Pc2) + getPemb(Pc2))
    return makePc(pembX2//penyX2, pembX2%penyX2, penyX2)

def MulP(Pc1,Pc2):
    pembX2 = (getPeny(Pc1)*getBil(Pc1) + getPemb(Pc1)) * (getPeny(Pc2)*getBil(Pc2) + getPemb(Pc2))
    penyX2 =  getPeny(Pc1) * getPeny(Pc2)
    return makePc(pembX2//penyX2, pembX2%penyX2, penyX2)

def isEqP(Pc1,Pc2):
    return konvesiReal(Pc1) == konvesiReal(Pc2)

def isLtP(Pc1,Pc2):
    return konvesiReal(Pc1) < konvesiReal(Pc2)

def IsGtP(Pc1,Pc2):
    return konvesiReal(Pc1) > konvesiReal(Pc2)

# Aplikasi
print(konvesiP(makePc(-2,3,5))) 
print(konvesiReal(makePc(-2,3,5))) 

print(AddP(makePc(5,2,5),makePc(1,1,6)))
print(SubP(makePc(5,2,5),makePc(1,1,6)))

print(DivP(makePc(3,3,5),makePc(2,1,8)))
print(MulP(makePc(3,2,5),makePc(2,1,8)))

print(isEqP(makePc(2,2,16),makePc(2,1,8)))
print(isLtP(makePc(2,1,16),makePc(2,1,8)))
print(IsGtP(makePc(2,1,16),makePc(2,1,8)))