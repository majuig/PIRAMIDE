#Piramide
from array import array

class Piramide:
    def __init__ (self, z):
        self._a1 = z[0]
        self._a2 = z[1]
        self._a3 = z[2]
        self._a4 = z[3]
        self._a5 = z[4]
        self._a6 = z[5]
        self._b1 = z[6]
        self._b2 = z[7]
        self._b3 = z[8]
        self._b4 = z[9]
        self._b5 = z[10]
        self._c1 = z[11]
        self._c2 = z[12]
        self._c3 = z[13]
        self._c4 = z[14]
        self._d1 = z[15]
        self._d2 = z[16]
        self._d3 = z[17]
        self._e1 = z[18]
        self._e2 = z[19]
        self._f1 = z[20]

    def mostrara4(self):
        return self._f1 #Para ver si anda

class terna():


#    a
#b       c


    def __init__ (self,b,c,a):
        self._a = a
        self._b = b
        self._c = c
        self.resuelto = False

    def resolver(self):
        if(self._a == 0 and self._b != 0 and self._c !=0):
            self._a = self._b + self._c
        if(self._a != 0 and self._b != 0  and self._c == 0):
            self._c = self._a - self._b
        if(self._a != 0 and self._b == 0 and self._c != 0):
            self._b = self._a - self._c
        if(self._a != 0 and self._b != 0 and self._c != 0):
            self.resuelto = True

    def mostrara(self):
        return self._a
    def mostrarb(self):
        return self._b
    def mostrarc(self):
        return self._c

class subtriangulo3():
#   a
#  b c
# d e f

    def __init__(self,a,b,c,d,e,f):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f

    def resolver(self):
        if(self._a != 0 and self._d != 0 and self._f != 0):
            self._e = (self._a - self._d - self._f) / 2
            if(isinstance(self._e , int)):
                _algoResuelto = 1
            else:
                self._e = 0

_AlgoResuelto = 0
numeros = array("i", [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
test = Piramide(numeros)

terna1 = terna(numeros[0],numeros[1],numeros[6])
terna2 = terna(numeros[1],numeros[2],numeros[7])
terna3 = terna(numeros[2],numeros[3],numeros[8])
terna4 = terna(numeros[3],numeros[4],numeros[9])
terna5 = terna(numeros[4],numeros[5],numeros[10])
terna6 = terna(numeros[6],numeros[7],numeros[11])
terna7 = terna(numeros[7],numeros[8],numeros[12])
terna8 = terna(numeros[8],numeros[9],numeros[13])
terna9 = terna(numeros[9],numeros[10],numeros[14])
terna10 = terna(numeros[11],numeros[12],numeros[15])
terna11 = terna(numeros[12],numeros[13],numeros[16])
terna12 = terna(numeros[13],numeros[14],numeros[17])
terna13 = terna(numeros[15],numeros[16],numeros[18])
terna14 = terna(numeros[16],numeros[17],numeros[19])
terna15 = terna(numeros[18],numeros[19],numeros[20])

subt3_1 = subtriangulo3(numeros[11],numeros[6],numeros[7],numeros[0],numeros[1],numeros[2])

print(terna1.mostrara())
print(terna1.mostrarb())
print(terna1.mostrarc())
print("----")

terna1.resolver()           #Resuelve terna1
if(terna1.resuelto):        #Se fija si terna1 está resuelta
    _AlgoResuelto = 1       #Bandera = 1 si se resolvió
    print("Resolvio Terna")



terna1.resolver()
if(terna1.resuelto):
    _AlgoResuelto = 1



print(terna1.mostrara())
print(terna1.mostrarb())
print(terna1.mostrarc())



"""

TERNAS
a1 a2 b1
a2 a3 b2
a3 a4 b3
a4 a5 b4
a5 a6 b5
6)b1 b2 c1
7) b2 b3 c2
8) b3 b4 c3
9)b4 b5 c4
10)c1 c2 d1
11)c2 c3 d2
12)c3 c4 d3
13)d1 d2 e1
14)d2 d3 e2
15)e1 e2 f1


class Piramide:
    def __init__ (self, a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u):
        self._a1 = a
        self._a4 = b
        self._a3 = c
        self._a4 = d
        self._a5 = e
        self._a6 = f
        self._b1 = g
        self._b2 = h
        self._b3 = i
        self._b4 = j
        self._b5 = k
        self._c1 = l
        self._c2 = m
        self._c3 = n
        self._c4 = o
        self._d1 = p
        self._d2 = q
        self._d3 = r
        self._e1 = s
        self._e2 = t
        self._f1 = u


    git add piramide.py
    git commit -m "comentario"
    git push origin master
"""
