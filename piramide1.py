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
            self.b.modificar(self.a.valor - self.c.valor)
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

#Instanciar celdas

#Instanciar Piramide

#Instanciando todas las Ternas
terna0 = terna(celda0.valor,celda1.valor,celda6.valor)
terna1 = terna(celda1.valor,celda2.valor,celda7.valor)
terna2 = terna(celda2.valor,celda3.valor,celda8.valor)
terna3 = terna(celda3.valor,celda4.valor,celda9.valor)
terna4 = terna(celda4.valor,celda5.valor,celda10.valor)
terna5 = terna(celda6.valor,celda7.valor,celda11.valor)
terna6 = terna(celda7.valor,celda8.valor,celda12.valor)
terna7 = terna(celda8.valor,celda9.valor,celda13.valor)
terna8 = terna(celda9.valor,celda10.valor,celda14.valor)
terna9 = terna(celda11.valor,celda12.valor,celda15.valor)
terna10 = terna(celda12.valor,celda13.valor,celda16.valor)
terna11 = terna(celda13.valor,celda14.valor,celda17.valor)
terna12 = terna(celda15.valor,celda16.valor,celda18.valor)
terna13 = terna(celda16.valor,celda17.valor,celda19.valor)
terna14 = terna(celda18.valor,celda19.valor,celda20.valor)

#Intanciando todos los Subtriangulos de base 3
subt3_1 = subtriangulo3(celda11.valor,celda6.valor,celda7.valor,celda0.valor,celda1.valor,celda2.valor)
subt3_2 = subtriangulo3(celda12.valor,celda7.valor,celda8.valor,celda1.valor,celda2.valor,celda3.valor)
subt3_3 = subtriangulo3(celda13.valor,celda8.valor,celda9.valor,celda2.valor,celda3.valor,celda4.valor)
subt3_4 = subtriangulo3(celda14.valor,celda9.valor,celda10.valor,celda3.valor,celda4.valor,celda5.valor)
subt3_5 = subtriangulo3(celda15.valor,celda11.valor,celda12.valor,celda6.valor,celda7.valor,celda8.valor)
subt3_6 = subtriangulo3(celda16.valor,celda12.valor,celda13.valor,celda7.valor,celda8.valor,celda9.valor)
subt3_7 = subtriangulo3(celda17.valor,celda13.valor,celda14.valor,celda8.valor,celda9.valor,celda10.valor)
subt3_8 = subtriangulo3(celda18.valor,celda15.valor,celda16.valor,celda11.valor,celda12.valor,celda13.valor)
subt3_9 = subtriangulo3(celda19.valor,celda16.valor,celda17.valor,celda12.valor,celda13.valor,celda14.valor)
subt3_10 = subtriangulo3(celda20.valor,celda18.valor,celda19.valor,celda15.valor,celda16.valor,celda17.valor)

#Instanciando todos los subtriangulos de base 4
subt4_1 = subtriangulo4(celda15.valor,celda11.valor,celda12.valor,celda6.valor,celda7.valor,celda8.valor,celda0.valor,celda1.valor,celda2.valor,celda3.valor)
subt4_2 = subtriangulo4(celda16.valor,celda12.valor,celda13.valor,celda7.valor,celda8.valor,celda9.valor,celda1.valor,celda2.valor,celda3.valor,celda4.valor)
subt4_3 = subtriangulo4(celda17.valor,celda13.valor,celda14.valor,celda9.valor,celda10.valor,celda2.valor,celda3.valor,celda4.valor,celda5.valor,celda3.valor)
subt4_4 = subtriangulo4(celda18.valor,celda15.valor,celda16.valor,celda11.valor,celda12.valor,celda13.valor,celda6.valor,celda7.valor,celda8.valor,celda9.valor)
subt4_5 = subtriangulo4(celda19.valor,celda16.valor,celda17.valor,celda12.valor,celda13.valor,celda14.valor,celda7.valor,celda8.valor,celda9.valor,celda10.valor)
subt4_6 = subtriangulo4(celda20.valor,celda18.valor,celda19.valor,celda15.valor,celda16.valor,celda17.valor,celda11.valor,celda12.valor,celda13.valor,celda14.valor)

#Instanciando todos los Subtriangulos de base 5
subt5_1 = subtriangulo5(celda18.valor,celda15.valor,celda16.valor,celda11.valor,celda12.valor,celda13.valor,celda6.valor,celda7.valor,celda8.valor,celda9.valor,celda0.valor,celda1.valor,celda2.valor,celda3.valor,celda4.valor)
subt5_1 = subtriangulo5(celda19.valor,celda16.valor,celda17.valor,celda12.valor,celda13.valor,celda14.valor,celda7.valor,celda8.valor,celda9.valor,celda10.valor,celda1.valor,celda2.valor,celda3.valor,celda4.valor,celda5.valor)
subt5_1 = subtriangulo5(celda20.valor,celda18.valor,celda19.valor,celda15.valor,celda16.valor,celda17.valor,celda11.valor,celda12.valor,celda13.valor,celda14.valor,celda6.valor,celda7.valor,celda8.valor,celda9.valor,celda10.valor)

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
