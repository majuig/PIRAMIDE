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

celda0 = celda(10)
celda1 = celda(0)
celda2 = celda(12)

print(celda0.MostrarValorCelda())
print(celda1.MostrarValorCelda())
print(celda2.MostrarValorCelda())
print("--------------------------")

tri = terna(celda0,celda1,celda2)
print(tri.mostrara())
print(tri.mostrarb())
print(tri.mostrarc())
print("--------------------------")

tri.resolver()

print(tri.mostrara())
print(tri.mostrarb())
print(tri.mostrarc())
print("----------resuelto, valores de tri----------------")

print(celda0.MostrarValorCelda())
print(celda1.MostrarValorCelda())
print(celda2.MostrarValorCelda())
print("----------resuelto, valores de cada celda----------------")
