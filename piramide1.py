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

    def completo(self):
        global AlgoResuelto
        if(self.a1.valor > 0 and self.a2.valor > 0 and self.a3.valor > 0 and self.a4.valor > 0 and self.a5.valor > 0
         and self.a6.valor > 0 and self.b1.valor > 0 and self.b2.valor > 0 and self.b3.valor > 0 and self.b4.valor > 0
         and self.b5.valor > 0 and self.c1.valor > 0 and self.c2.valor > 0 and self.c3.valor > 0 and self.c4.valor > 0
         and self.d1.valor > 0 and self.d2.valor > 0 and self.d3.valor > 0 and self.e1.valor > 0 and self.e2.valor > 0
         and self.f1.valor):
         AlgoResuelto = 2
        else:
            AlgoResuelto = 3

    def base16(self):
        global AlgoResuelto
        if((self.a1.valor + self.a2.valor + self.a3.valor + self.a4.valor + self.a5.valor + self.a6.valor) == 21 ):
            if(self.a1.valor < 7 and self.a2.valor < 7 and self.a3.valor < 7 and self.a4.valor < 7 and self.a5.valor < 7 and self.a6.valor < 7):
                AlgoResuelto = 2
        else:
            AlgoResuelto = 3

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
        global AlgoResuelto
        if(self.a.valor == 0 and self.b.valor != 0 and self.c.valor !=0):
            self.a.modificar(self.b.valor + self.c.valor)
            if(self.a.valor > 0):
                AlgoResuelto = 1

        if(self.a.valor != 0 and self.b.valor != 0  and self.c.valor == 0):
            self.c.modificar(self.a.valor - self.b.valor)
            if(self.a.valor > 0):
                AlgoResuelto = 1

        if(self.a.valor != 0 and self.b.valor == 0 and self.c.valor != 0):
            self.b.modificar(self.a.valor - self.c.valor)
            if(self.a.valor > 0):
                AlgoResuelto = 1


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
        global AlgoResuelto
        if(self.a.valor != 0 and self.d.valor != 0 and self.f.valor != 0 and self.e.valor == 0):
            self.e.modificar((self.a.valor - self.d.valor - self.f.valor) / 2)

            ValorEntero = int(self.e.valor)
            if(ValorEntero == self.e.valor):
                self.e.valor =  ValorEntero
                AlgoResuelto = 1
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
        global AlgoResuelto
        if(self.a.valor != 0 and self.h.valor != 0 and self.i.valor != 0 and self.j.valor != 0 and self.g.valor == 0): #FALTA G
            resultado = self.a.valor - self.j.valor - (self.i.valor *3) - (self.h.valor*3)

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.g.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.g.modificar(0)

        if(self.a.valor != 0 and self.h.valor != 0 and self.i.valor != 0 and self.g.valor != 0  and self.j.valor == 0): #FALTA J
            resultado = self.a.valor - self.g.valor - (self.i.valor *3) - (self.h.valor *3)

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.j.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.j.modificar(0)

        if(self.a.valor != 0 and self.j.valor != 0 and self.i.valor != 0 and self.g.valor != 0  and self.h.valor == 0): #FALTA H
            resultado = (self.a.valor - self.g.valor - (self.i.valor *3) - self.j.valor)/3

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.h.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.h.modificar(0)

        if(self.a.valor != 0 and self.j.valor != 0 and self.h.valor != 0 and self.g.valor != 0  and self.i.valor == 0): #FALTA I
            resultado = (self.a.valor - self.g.valor - (self.h.valor *3) - self.j.valor)/3

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.i.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.i.modificar(0)

class subtriangulo5():
#   a
#  b c
# d e f
#g h i j
#k l m n o
    def __init__(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
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
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o

        #hay 5 casos
    def resolver(self):

        global AlgoResuelto
        if(self.a.valor != 0 and self.l.valor != 0 and self.m.valor != 0 and self.n.valor != 0 and self.o.valor != 0 and self.k.valor == 0): #FALTA K
            resultado = self.a.valor - (6 * self.m.valor) - (4 * self.l.valor) - (4 * self.n.valor) - self.o.valor

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.k.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.k.modificar(0)

        if(self.a.valor != 0 and self.l.valor != 0 and self.m.valor != 0 and self.n.valor != 0 and self.k.valor != 0 and self.o.valor == 0): #FALTA O
            resultado = self.a.valor - (6 * self.m.valor) - (4 * self.l.valor) - (4 * self.n.valor) - self.k.valor

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.k.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.k.modificar(0)

        if(self.a.valor != 0 and self.k.valor != 0 and self.m.valor != 0 and self.n.valor != 0 and self.o.valor != 0 and self.l.valor == 0): #FALTA L
            resultado = (self.a.valor - (6 * self.m.valor) - self.k.valor - (4 * self.n.valor) - self.o.valor)/4

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.l.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.l.modificar(0)

        if(self.a.valor != 0 and self.k.valor != 0 and self.m.valor != 0 and self.l.valor != 0 and self.o.valor != 0 and self.n.valor == 0): #FALTA N
            resultado = (self.a.valor - (6 * self.m.valor) - self.k.valor - (4 * self.l.valor) - self.o.valor)/4

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.n.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.n.modificar(0)

        if(self.a.valor != 0 and self.k.valor != 0 and self.n.valor != 0 and self.l.valor != 0 and self.o.valor != 0 and self.m.valor == 0): #FALTA M
            resultado = (self.a.valor - (4 * self.n.valor) - self.k.valor - (4 * self.l.valor) - self.o.valor)/6

            ValorEntero = int(resultado)
            if(ValorEntero == resultado):
                self.m.modificar(ValorEntero)
                AlgoResuelto = 1
            else:
                self.m.modificar(0)




#Instanciar celdas
celda0 = celda(0)  #1 #Fila A BASE
celda1 = celda(2)   #2
celda2 = celda(3)   #3
celda3 = celda(4)   #4
celda4 = celda(0)   #5
celda5 = celda(0)   #6
celda6 = celda(0)   #3 #Fila B
celda7 = celda(0)   #5
celda8 = celda(7)   #7
celda9 = celda(0)   #9
celda10 = celda(0) #11
celda11 = celda(0)  #8  #Fila C
celda12 = celda(12) #12
celda13 = celda(0) #16
celda14 = celda(0) #20
celda15 = celda(20)  #20  #Fila D
celda16 = celda(0) #28
celda17 = celda(36) #36
celda18 = celda(0)  #48  #Fila E
celda19 = celda(0)  #64
celda20 = celda(112)   #112  #Fila F PUNTA

#Instanciar Piramide
ThePiramide = Piramide(celda0,celda1,celda2,celda3,celda4,celda5,celda6,celda7,celda8,celda9,celda10,celda11,celda12,celda13,celda14,celda15,celda16,celda17,celda18,celda19,celda20)

#Instanciando todas las Ternas
terna0 = terna(celda0,celda1,celda6)
terna1 = terna(celda1,celda2,celda7)
terna2 = terna(celda2,celda3,celda8)
terna3 = terna(celda3,celda4,celda9)
terna4 = terna(celda4,celda5,celda10)
terna5 = terna(celda6,celda7,celda11)
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
subt3_5 = subtriangulo3(celda15,celda11,celda12,celda6,celda7,celda8)
subt3_6 = subtriangulo3(celda16,celda12,celda13,celda7,celda8,celda9)
subt3_7 = subtriangulo3(celda17,celda13,celda14,celda8,celda9,celda10)
subt3_8 = subtriangulo3(celda18,celda15,celda16,celda11,celda12,celda13)
subt3_9 = subtriangulo3(celda19,celda16,celda17,celda12,celda13,celda14)
subt3_10 = subtriangulo3(celda20,celda18,celda19,celda15,celda16,celda17)

#Instanciando todos los subtriangulos de base 4
subt4_1 = subtriangulo4(celda15,celda11,celda12,celda6,celda7,celda8,celda0,celda1,celda2,celda3)
subt4_2 = subtriangulo4(celda16,celda12,celda13,celda7,celda8,celda9,celda1,celda2,celda3,celda4)
subt4_3 = subtriangulo4(celda17,celda13,celda14,celda9,celda10,celda2,celda3,celda4,celda5,celda3)
subt4_4 = subtriangulo4(celda18,celda15,celda16,celda11,celda12,celda13,celda6,celda7,celda8,celda9)
subt4_5 = subtriangulo4(celda19,celda16,celda17,celda12,celda13,celda14,celda7,celda8,celda9,celda10)
subt4_6 = subtriangulo4(celda20,celda18,celda19,celda15,celda16,celda17,celda11,celda12,celda13,celda14)

#Instanciando todos los Subtriangulos de base 5
subt5_1 = subtriangulo5(celda18,celda15,celda16,celda11,celda12,celda13,celda6,celda7,celda8,celda9,celda0,celda1,celda2,celda3,celda4)
subt5_2 = subtriangulo5(celda19,celda16,celda17,celda12,celda13,celda14,celda7,celda8,celda9,celda10,celda1,celda2,celda3,celda4,celda5)
subt5_3 = subtriangulo5(celda20,celda18,celda19,celda15,celda16,celda17,celda11,celda12,celda13,celda14,celda6,celda7,celda8,celda9,celda10)

print("")
print("------Valores de las celdas SIN RESOLVER-------")
#cimacornudo
print(celda20.MostrarValorCelda())

#quintafila
print(celda18.MostrarValorCelda(), end=' ')
print(celda19.MostrarValorCelda())

#cuartafila
print(celda15.MostrarValorCelda(), end=' ')
print(celda16.MostrarValorCelda(), end=' ')
print(celda17.MostrarValorCelda())


#tercerfila
print(celda11.MostrarValorCelda(), end=' ')
print(celda12.MostrarValorCelda(), end=' ')
print(celda13.MostrarValorCelda(), end=' ')
print(celda14.MostrarValorCelda())

#segundafila

print(celda6.MostrarValorCelda(), end=' ')
print(celda7.MostrarValorCelda(), end=' ')
print(celda8.MostrarValorCelda(), end=' ')
print(celda9.MostrarValorCelda(), end=' ')
print(celda10.MostrarValorCelda())

#base
print(celda0.MostrarValorCelda(), end=' ')
print(celda1.MostrarValorCelda(), end=' ')
print(celda2.MostrarValorCelda(), end=' ')
print(celda3.MostrarValorCelda(), end=' ')
print(celda4.MostrarValorCelda(), end=' ')
print(celda5.MostrarValorCelda())
print("")

AlgoResuelto = 1

while(AlgoResuelto != 0):
    AlgoResuelto = 0

    terna0.resolver()   #Resuelvo Ternas
    terna1.resolver()
    terna2.resolver()
    terna3.resolver()
    terna4.resolver()
    terna5.resolver()
    terna6.resolver()
    terna7.resolver()
    terna8.resolver()
    terna9.resolver()
    terna10.resolver()
    terna11.resolver()
    terna12.resolver()
    terna13.resolver()
    terna14.resolver()

    subt3_1.resolver()   #Resuelvo Triangulos base 3
    subt3_2.resolver()
    subt3_3.resolver()
    subt3_4.resolver()
    subt3_5.resolver()
    subt3_6.resolver()
    subt3_7.resolver()
    subt3_8.resolver()
    subt3_9.resolver()
    subt3_10.resolver()

    subt4_1.resolver()  #Resuelvo triangulos base 4
    subt4_2.resolver()
    subt4_3.resolver()
    subt4_4.resolver()
    subt4_5.resolver()
    subt4_6.resolver()

    subt5_1.resolver()  #Resuelvo triangulos base 5
    subt5_2.resolver()
    subt5_3.resolver()

ThePiramide.completo()
ThePiramide.base16()

if(AlgoResuelto == 2):
    print("------Valores de la piramide RESUELTA-------")
    #cimacornudo
    print(celda20.MostrarValorCelda())

    #quintafila
    print(celda18.MostrarValorCelda(), end=' ')
    print(celda19.MostrarValorCelda())

    #cuartafila
    print(celda15.MostrarValorCelda(), end=' ')
    print(celda16.MostrarValorCelda(), end=' ')
    print(celda17.MostrarValorCelda())


    #tercerfila
    print(celda11.MostrarValorCelda(), end=' ')
    print(celda12.MostrarValorCelda(), end=' ')
    print(celda13.MostrarValorCelda(), end=' ')
    print(celda14.MostrarValorCelda())

    #segundafila

    print(celda6.MostrarValorCelda(), end=' ')
    print(celda7.MostrarValorCelda(), end=' ')
    print(celda8.MostrarValorCelda(), end=' ')
    print(celda9.MostrarValorCelda(), end=' ')
    print(celda10.MostrarValorCelda())

    #base
    print(celda0.MostrarValorCelda(), end=' ')
    print(celda1.MostrarValorCelda(), end=' ')
    print(celda2.MostrarValorCelda(), end=' ')
    print(celda3.MostrarValorCelda(), end=' ')
    print(celda4.MostrarValorCelda(), end=' ')
    print(celda5.MostrarValorCelda())
else:
    print("No se puede resolver la piramide o faltan datos para hacerlo")

    while(True):
        eleccion = input("Ingrese Y para ver hasta donde se pudo resolver la piramide y N para salir: ")
        if(eleccion == 'Y' or eleccion == 'y'):
            print("")
            print("------Valores de las celdas RESUELTAS-------")
            #cimacornudo
            print(celda20.MostrarValorCelda())

            #quintafila
            print(celda18.MostrarValorCelda(), end=' ')
            print(celda19.MostrarValorCelda())

            #cuartafila
            print(celda15.MostrarValorCelda(), end=' ')
            print(celda16.MostrarValorCelda(), end=' ')
            print(celda17.MostrarValorCelda())


            #tercerfila
            print(celda11.MostrarValorCelda(), end=' ')
            print(celda12.MostrarValorCelda(), end=' ')
            print(celda13.MostrarValorCelda(), end=' ')
            print(celda14.MostrarValorCelda())

            #segundafila

            print(celda6.MostrarValorCelda(), end=' ')
            print(celda7.MostrarValorCelda(), end=' ')
            print(celda8.MostrarValorCelda(), end=' ')
            print(celda9.MostrarValorCelda(), end=' ')
            print(celda10.MostrarValorCelda())

            #base
            print(celda0.MostrarValorCelda(), end=' ')
            print(celda1.MostrarValorCelda(), end=' ')
            print(celda2.MostrarValorCelda(), end=' ')
            print(celda3.MostrarValorCelda(), end=' ')
            print(celda4.MostrarValorCelda(), end=' ')
            print(celda5.MostrarValorCelda())
            break

        if(eleccion == 'N' or eleccion == 'n'):
            break


"""

    git add piramide.py
    git commit -m "comentario"
    git push origin master
"""
