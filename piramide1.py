#Piramide
from array import array

class Piramide:
    def __init__ (self, a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u):
        self.a1 = a
        self.a2 = b
        self.a3 = c
        self.a4 = d
        self.a5 = e
        self.a6 = f
        self.b1 = g
        self.b2 = h
        self.b3 = i
        self.b4 = j
        self.b5 = k
        self.c1 = l
        self.c2 = m
        self.c3 = n
        self.c4 = o
        self.d1 = p
        self.d2 = q
        self.d3 = r
        self.e1 = s
        self.e2 = t
        self.f1 = u

class celda():
    def __init__ (self, valor):
        self.valor = valor
    def modificar(self, NuevoValor):
        self.valor = NuevoValor
    def MostrarValorCelda(self):
        return self.valor


class terna():

#    a
#b       c


    def __init__ (self,b,c,a):
        self.a = a
        self.b = b
        self.c = c
        self.resuelto = False

    def resolver(self):
        if(self.a.valor == 0 and self.b.valor != 0 and self.c.valor !=0):
            self.a.modificar(self.b.valor + self.c.valor)
        if(self.a.valor != 0 and self.b.valor != 0  and self.c.valor == 0):
            self.c.modificar(self.a.valor - self.b.valor)
        if(self.a.valor != 0 and self.b.valor == 0 and self.c.valor != 0):
            self.b.modificar(self.a.valor.valor - self.c.valor)
        if(self.a.valor != 0 and self.b.valor != 0 and self.c.valor != 0):
            self.resuelto = True

    def mostrara(self):
        return self.a.valor
    def mostrarb(self):
        return self.b.valor
    def mostrarc(self):
        return self.c.valor

class subtriangulo3():
#   a
#  b c
# d e f

    def __init__(self,a,b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def resolver(self):
        if(self.a.valor != 0 and self.d.valor != 0 and self.f.valor != 0 and self.e.valor == 0):
            self.e.modificar((self.a.valor - self.d.valor - self.f.valor) / 2)

            ValorEntero = int(self.e.valor)
            if(ValorEntero == self.e.valor):
                self.e.valor =  ValorEntero
                _algoResuelto = 1
            else:
                self.e.valor = 0


class subtriangulo4():
#   a
#  b c
# d e f
#g h i j

    def __init__(self,a,b,c,d,e,f,g,h,i,j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j

    def resolver(self): #hay 4 casos que falta g,h,i ó j

        if(self.a.valor != 0 and self.h.valor != 0 and self.i.valor != 0 and self.j.valor != 0 and self.g.valor == 0):
            resultado = self.a.valor - self.j.valor - (self.valor.i *3) - (self.h.valor*3)

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.h.modificar(ValorEntero)
                _algoResuelto = 1
            else:
                self.h.modificar(0)

        if(self.a.valor != 0 and self.h.valor!= 0 and self.i.valor != 0 and self.g.valor != 0  and self.j.valor == 0):
            resultado = self.a.valor - self.j.valor - (self.valor.i *3) - (self.h.valor *3)

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.h.modificar(ValorEntero)
                _algoResuelto = 1
            else:
                self.h.modificar(0)

        if(self.a.valor != 0 and self.j.valor != 0 and self.i.valor != 0 and self.g.valor != 0  and self.h.valor == 0):
            resultado = (self.a.valor - self.g.valor - (self.i.valor *3) - self.j.valor)/3

            ValorEntero = int(resultado)
            print("VALOR:")
            print(ValorEntero)
            print(resultado)
            print("--")

            if(ValorEntero == resultado):
                self.h.modificar(ValorEntero)
                _algoResuelto = 1
            else:
                self.h.modificar(0)

        if(self.a.valor != 0 and self.j.valor != 0 and self.h.valor != 0 and self.g.valor != 0  and self.i.valor == 0):
            self.i.valor = (self.a.valor - self.g.valor - (self.h.valor*3) - self.j.valor)/3

            ValorEntero = int(self.i.valor)
            if(ValorEntero == self.i.valor):
                self.i.valor =  ValorEntero
                _algoResuelto = 1
            else:
                self.i.valor = 0

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
        self.g = g
        self.h = h
        self.i = i
        self.j = j
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

#Instanciar celdas
celda0 = celda(1)   #Fila A BASE
celda1 = celda(0)
celda2 = celda(3)
celda3 = celda(5)
celda4 = celda(0)
celda5 = celda(6)
celda6 = celda(0)   #Fila B
celda7 = celda(0)
celda8 = celda(0)
celda9 = celda(9)
celda10 = celda(10)
celda11 = celda(0)  #Fila C
celda12 = celda(0)
celda13 = celda(17)
celda14 = celda(0)
celda15 = celda(20)  #Fila D
celda16 = celda(0)
celda17 = celda(0)
celda18 = celda(0)  #Fila E
celda19 = celda(0)
celda20 = celda(0)  #Fila F PUNTA

#Instanciar Piramide
ThePiramide = Piramide(celda0,celda1,celda2,celda3,celda4,celda5,celda6,celda7,celda8,celda9,celda10,celda11,celda12,celda13,celda14,celda15,celda16,celda17,celda18,celda19,celda20)

#Instanciando todas las Ternas
terna0 = terna(celda0,celda1,celda6)
terna1 = terna(celda1,celda2,celda7)
terna2 = terna(celda2,celda3,celda8)
terna3 = terna(celda3,celda4,celda9)
terna4 = terna(celda4,celda5,celda10)
terna5 = terna(celda6.valor,celda7,celda11)

terna6 = terna(celda7,celda8,celda12)
terna7 = terna(celda8,celda9,celda13)
terna8 = terna(celda9,celda10,celda14)
terna9 = terna(celda11,celda12,celda15)
terna10 = terna(celda12,celda13,celda16)
terna11 = terna(celda13,celda14,celda17)
terna12 = terna(celda15,celda16,celda18)
terna13 = terna(celda16,celda17,celda19)
terna14 = terna(celda18,celda19,celda20)

#Intanciando todos los Subtriangulos de base 3
subt3_1 = subtriangulo3(celda11,celda6,celda7,celda0,celda1,celda2)
subt3_2 = subtriangulo3(celda12,celda7,celda8,celda1,celda2,celda3)
subt3_3 = subtriangulo3(celda13,celda8,celda9,celda2,celda3,celda4)
subt3_4 = subtriangulo3(celda14,celda9,celda10,celda3,celda4,celda5)
subt3_5 = subtriangulo3(celda15,celda11,celda12,celda6.valor,celda7,celda8)
subt3_6 = subtriangulo3(celda16,celda12,celda13,celda7,celda8,celda9)
subt3_7 = subtriangulo3(celda17,celda13,celda14,celda8,celda9,celda10)
subt3_8 = subtriangulo3(celda18,celda15,celda16,celda11,celda12,celda13)
subt3_9 = subtriangulo3(celda19,celda16,celda17,celda12,celda13,celda14)
subt3_10 = subtriangulo3(celda20,celda18,celda19,celda15,celda16,celda17)

#Instanciando todos los subtriangulos de base 4
subt4_1 = subtriangulo4(celda15,celda11,celda12,celda6.valor,celda7,celda8,celda0,celda1,celda2,celda3)
subt4_2 = subtriangulo4(celda16,celda12,celda13,celda7,celda8,celda9,celda1,celda2,celda3,celda4)
subt4_3 = subtriangulo4(celda17,celda13,celda14,celda9,celda10,celda2,celda3,celda4,celda5,celda3)
subt4_4 = subtriangulo4(celda18,celda15,celda16,celda11,celda12,celda13,celda6.valor,celda7,celda8,celda9)
subt4_5 = subtriangulo4(celda19,celda16,celda17,celda12,celda13,celda14,celda7,celda8,celda9,celda10)
subt4_6 = subtriangulo4(celda20,celda18,celda19,celda15,celda16,celda17,celda11,celda12,celda13,celda14)

#Instanciando todos los Subtriangulos de base 5
subt5_1 = subtriangulo5(celda18,celda15,celda16,celda11,celda12,celda13,celda6.valor,celda7,celda8,celda9,celda0,celda1,celda2,celda3,celda4)
subt5_1 = subtriangulo5(celda19,celda16,celda17,celda12,celda13,celda14,celda7,celda8,celda9,celda10,celda1,celda2,celda3,celda4,celda5)
subt5_1 = subtriangulo5(celda20,celda18,celda19,celda15,celda16,celda17,celda11,celda12,celda13,celda14,celda6.valor,celda7,celda8,celda9,celda10)

print("Hola")

print(celda15.MostrarValorCelda())
print(celda11.MostrarValorCelda())
print(celda12.MostrarValorCelda())
print(celda6.MostrarValorCelda())
print(celda7.MostrarValorCelda())
print(celda8.MostrarValorCelda())
print(celda0.MostrarValorCelda())
print(celda1.MostrarValorCelda())
print(celda2.MostrarValorCelda())
print(celda3.MostrarValorCelda())
print("------valores de las celdas-------")
subt4_1.resolver()

print(celda15.MostrarValorCelda())
print(celda11.MostrarValorCelda())
print(celda12.MostrarValorCelda())
print(celda6.MostrarValorCelda())
print(celda7.MostrarValorCelda())
print(celda8.MostrarValorCelda())
print(celda0.MostrarValorCelda())
print(celda1.MostrarValorCelda())
print(celda2.MostrarValorCelda())
print(celda3.MostrarValorCelda())
print("------valores de las celdas RESUELTAS-------")

"""

    git add piramide.py
    git commit -m "comentario"
    git push origin master
"""
