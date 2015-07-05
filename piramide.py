#Piramide
from array import array

class Piramide:
    def __init__ (self, z):
        self._a1 = z[0]
        self._a4 = z[1]
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
        return self._a4


numeros = array("i", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
test = Piramide(numeros)
print(test.mostrara4())



"""
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
