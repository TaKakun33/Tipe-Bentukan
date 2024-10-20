def make_PC(b,n,d):
    return [b,n,d]

def get_bil(Pc):
    return Pc[0]

def get_pemb(Pc):
    return Pc[1]

def get_peny(Pc):
    return Pc[2]

def make_P(n,d):
    return [n,d]

def konvesiP(Pc):
    if get_bil(Pc)> 0:
        return make_P(get_bil(Pc)*get_peny(Pc) + get_pemb(Pc),get_peny(Pc))
    else:
        return make_P(get_bil(Pc)*get_peny(Pc) - get_pemb(Pc),get_peny(Pc))

def konvesiReal(Pc):
    if get_bil(Pc) > 0:
        return get_bil(Pc)+(get_pemb(Pc)/get_peny(Pc))
    else:
        return get_bil(Pc)-(get_pemb(Pc)/get_peny(Pc))

def AddP(Pc1,Pc2):
    return(make_PC(get_bil(Pc1) + get_bil(Pc2),get_pemb(Pc1)*get_peny(Pc2) + get_pemb(Pc2)*get_peny(Pc1),get_peny(Pc1)*get_peny(Pc2)))

def SubP(Pc1,Pc2):
    return(make_PC(get_bil(Pc1) - get_bil(Pc2),get_pemb(Pc1)*get_peny(Pc2) - get_pemb(Pc2)*get_peny(Pc1),get_peny(Pc1)*get_peny(Pc2)))

def MulP(Pc1,Pc2):
    pembX2 = (get_peny(Pc1)*get_bil(Pc1) + get_pemb(Pc1)) * (get_peny(Pc2)*get_bil(Pc2) + get_pemb(Pc2))
    penyX2 =  get_peny(Pc1) * get_peny(Pc2)
    return make_PC(pembX2//penyX2, pembX2%penyX2, penyX2)

def DivP(Pc1,Pc2):
    pembX2 = (get_peny(Pc1)*get_bil(Pc1) + get_pemb(Pc1)) * (get_peny(Pc2))
    penyX2 = (get_peny(Pc1)) * (get_peny(Pc2)*get_bil(Pc2) + get_pemb(Pc2))
    return make_PC(pembX2//penyX2, pembX2%penyX2, penyX2)

print(konvesiP(make_PC(-2,3,5))) 
print(konvesiReal(make_PC(-2,3,5))) 
print(AddP(make_PC(5,2,5),make_PC(1,1,6)))
print(SubP(make_PC(5,2,5),make_PC(1,1,6)))

print(MulP(make_PC(3,2,5),make_PC(2,1,8)))
print(DivP(make_PC(3,3,5),make_PC(2,1,8)))