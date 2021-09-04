import numpy as np
import module1 as md

while 1:
    a1 = list(map(float, input().split()))
    polll = list(map(float,a1))
    a_poly = np.array(list(a1),dtype = float)
    print("F(x)=",md.print_poly(a1))
    print("Степень многочлена = ",len(a1)-1)
    if a1[len(a1)-1] == 0:
        a1 = a1[:len(a1)-1]
    #print(a1)
    low = 1.0 / (1.0+float(abs(max((a1[:(len(a1)-1)]),key=abs))) / float(abs(a1[len(a1)-1])))
    up = 1.0 + float(abs(max(a1[1:],key=abs)))/abs(a1[0])
    print("Границы положительных корней=",up,low)
    print("Границы отрицательных корней=", -up, -low)