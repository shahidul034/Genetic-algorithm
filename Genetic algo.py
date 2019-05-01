import math
import random
def initialize():
    cromosome=[]
    for x2 in range(4):
        array = []
        for x in range(6):
            array.append(random.randint(0,1))
        cromosome.append(array)
    return cromosome

def calcuate_fit(cromo):
    flag=0
    val=0
    if cromo[0]==1:
        flag=1
    for x in range(1,6):
        tt=cromo[x]
        val+=tt*(math.pow(2,(len(cromo)-x-1)))
    if flag==1:
        val=-val
    cromo_vv=val
    val=-(val*val)+5
    return val,cromo_vv


def fitness(crr):
    dd_fit=[]
    dec_val=[]
    for x in crr:
        val,cr=calcuate_fit(x)
        print("fitness :",val," and ","decimal value: ",cr)
        dd_fit.append(val)
        dec_val.append(cr)
    return dd_fit,dec_val

def selection(dd,cr):
    d=sorted(dd)
    first=d[3]
    sec=d[2]
    f1=0
    f2=0
    print("1st best fit val: ",first)
    k=[]
    for x in range(4):
        if dd[x]==first and f1==0:
            f1=1
            k.append(cr[x])
    for x in range(4):
        if dd[x]==sec and f2==0:
            f2=1
            k.append(cr[x])
    return first,k

def crossover(new_sel):
    first_cr=new_sel[0]
    sec_cr = new_sel[1]
    cross_point=random.randint(0,5)
    for x in range(cross_point,6):
        first_cr[x],sec_cr[x]=sec_cr[x],first_cr[x]
    new_sel.append(first_cr)
    new_sel.append(sec_cr)
    return new_sel

def mutation(cross_val):
    hh=random.randint(0,50)
    if hh==25:
        i=random.randint(0,3)
        j=random.randint(0,5)
        cross_val[i][j]=1-cross_val[i][j]
    return cross_val
cr=initialize()
cnt=0
while(1):
    cnt+=1
    print("cnt: ",cnt)
    dd,dec=fitness(cr)
    print(cr)
    fr,new_sel=selection(dd,cr)
    if fr==5.0:
        break
    cross_val=crossover(new_sel)
    muted_value=mutation(cross_val)







