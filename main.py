'''
Calcule e mostre o resultado da seguinte expressão:
D = (R+S)/4
Onde: R = (A+B)*2 e S = (B+C)*A
'''

import os
a = (float(input("Digite o valor de a:\n")))
b = (float(input("Digite o valor de b:\n")))
c = (float(input("Digite o valor de c:\n")))
r = (a+b)*2
s = (b+c)*a
d = (r+s)/4
os.system("clear")
print ("O valor de R = ",r)
print ("O valor de S = ",s)
print ("O valor de D = ",d)
