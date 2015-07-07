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
        if(self._a != 0 and self._d != 0 and self._f != 0 and self._e == 0):
            self._e = (self._a - self._d - self._f) / 2
            if(isinstance(self._e , int)):
                _algoResuelto = 1
            else:
                self._e = 0

class subtriangulo4():
#   a
#  b c
# d e f
#g h i j

    def __init__(self,a,b,c,d,e,f,g,h,i,j):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
        self._g = g
        self._h = h
        self._i = i
        self._j = j

    def resolver(self): #hay 4 casos que falta g,h,i ó j
        if(self._a != 0 and self._h!= 0 and self._i != 0 and self._j != 0 and self._g == 0):
            self._g = self._a - (4 * self._i) - (3 * self._h)

        if(isinstance(self._g , int)):
            _algoResuelto = 1
        else:
            self._g = 0

    #caso2
        if(self._a != 0 and self._h!= 0 and self._i != 0 and self._g != 0  and self._j == 0):
            self._j = self._a - self._g - self._i - self._i - self._i - self._h - self._h - self._h
        if(isinstance(self._j , int)):
            _algoResuelto = 1
        else:
            self._j = 0

    #caso3
        if(self._a != 0 and self._j != 0 and self._i != 0 and self._g != 0  and self._h == 0):
            self._h = (self._a - self._g - self._i - self._i - self._i - self._j)/3
        if(isinstance(self._h , int)):
            _algoResuelto = 1
        else:
            self._h = 0

    #caso4
        if(self._a != 0 and self._j != 0 and self._h != 0 and self._g != 0  and self._i == 0):
            self._i = (self._a - self._g - self._h - self._h - self._h - self._j)/3
        if(isinstance(self._i , int)):
            _algoResuelto = 1
        else:
            self._i = 0

class subtriangulo5():
#   a
#  b c
# d e f
#g h i j
#k l m n o
    def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
        self._g = g
        self._h = h
        self._i = i
        self._j = j
        self._k =k
        self._l = l
        self._m = m
        self._n = n
        self._o = o

        #hay 5 casos
        def resolver(self):
            if(self._a != 0 and self._l!= 0 and self._m != 0 and self._n != 0 and self._o != 0 and self._k == 0):
                self._k = self._a - (6 * self._m) - (4 * self._l) - (4 * self._n) - self._o
            if(isinstance(self._k , int)):
                _algoResuelto = 1
            else:
                self._k = 0

            if(self._a != 0 and self._l!= 0 and self._m != 0 and self._n != 0 and self._k != 0 and self._o == 0):
                self._o = self._a - (6 * self._m) - (4 * self._l) - (4 * self._n) - self._k
            if(isinstance(self._o , int)):
                _algoResuelto = 1
            else:
                self._o = 0


            if(self._a != 0 and self._k!= 0 and self._m != 0 and self._n != 0 and self._o != 0 and self._l == 0):
                self._l = (self._a - (6 * self._m) - self._k - (4 * self._n) - self._o)/4
            if(isinstance(self._l , int)):
                _algoResuelto = 1
            else:
                self._l = 0

            if(self._a != 0 and self._k!= 0 and self._m != 0 and self._l != 0 and self._o != 0 and self._n == 0):
                self._n = (self._a - (6 * self._m) - self._k - (4 * self._l) - self._o)/4
            if(isinstance(self._n , int)):
                _algoResuelto = 1
            else:
                self._n = 0

            if(self._a != 0 and self._k!= 0 and self._n != 0 and self._l != 0 and self._o != 0 and self._m == 0):
                self._m = (self._a - (4 * self._n) - self._k - (4 * self._l) - self._o)/6
            if(isinstance(self._m , int)):
                _algoResuelto = 1
            else:
                self._m = 0



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
subt3_2 = subtriangulo3(numeros[12],numeros[7],numeros[8],numeros[1],numeros[2],numeros[3])
subt3_3 = subtriangulo3(numeros[13],numeros[8],numeros[9],numeros[2],numeros[3],numeros[4])
subt3_4 = subtriangulo3(numeros[14],numeros[9],numeros[10],numeros[3],numeros[4],numeros[5])
subt3_5 = subtriangulo3(numeros[15],numeros[11],numeros[12],numeros[6],numeros[7],numeros[8])
subt3_6 = subtriangulo3(numeros[16],numeros[12],numeros[13],numeros[7],numeros[8],numeros[9])
subt3_7 = subtriangulo3(numeros[17],numeros[13],numeros[14],numeros[8],numeros[9],numeros[10])
subt3_8 = subtriangulo3(numeros[18],numeros[15],numeros[16],numeros[11],numeros[12],numeros[13])
subt3_9 = subtriangulo3(numeros[19],numeros[16],numeros[17],numeros[12],numeros[13],numeros[14])
subt3_10 = subtriangulo3(numeros[20],numeros[18],numeros[19],numeros[15],numeros[16],numeros[17])


subt4_1 = subtriangulo4(numeros[15],numeros[11],numeros[12],numeros[6],numeros[7],numeros[8],numeros[0],numeros[1],numeros[2],numeros[3])

subt4_2 = subtriangulo4(numeros[16],numeros[12],numeros[13],numeros[7],numeros[8],numeros[9],numeros[1],numeros[2],numeros[3],numeros[4])

subt4_3 = subtriangulo4(numeros[17],numeros[13],numeros[14],numeros[8],numeros[9],numeros[10],numeros[2],numeros[3],numeros[4],numeros[5])

subt4_4 = subtriangulo4(numeros[18],numeros[15],numeros[16],numeros[11],numeros[12],numeros[13],numeros[6],numeros[7],numeros[8],numeros[9])

subt4_5 = subtriangulo4(numeros[19],numeros[16],numeros[17],numeros[12],numeros[13],numeros[14],numeros[7],numeros[8],numeros[9],numeros[10])

subt4_6 = subtriangulo4(numeros[20],numeros[18],numeros[19],numeros[15],numeros[16],numeros[17],numeros[11],numeros[12],numeros[13],numeros[14])


subt5_1 = subtriangulo5(numeros[18],numeros[15],numeros[16],numeros[11],numeros[12],numeros[13],numeros[6],numeros[7],numeros[8],numeros[9],numeros[0],numeros[1],numeros[2],numeros[3],numeros[4])

subt5_2 = subtriangulo5(numeros[19],numeros[16],numeros[17],numeros[12],numeros[13],numeros[14],numeros[7],numeros[8],numeros[9],numeros[10],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5])

subt5_3 = subtriangulo5(numeros[20],numeros[18],numeros[19],numeros[15],numeros[16],numeros[17],numeros[11],numeros[12],numeros[13],numeros[14],numeros[6],numeros[7],numeros[8],numeros[9],numeros[10])

print("Hola")

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

print("----")


for item in numeros:
    print(item)


"""

    git add piramide.py
    git commit -m "comentario"
    git push origin master
"""
