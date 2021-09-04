import numpy as np
import module1 as md

while 1:
    a1 = list(map(float, input().split()))
    if (float(a1[0])<0):
        for i in range(len(a1)):
            a1[i]*=-1
    print("F(x)=",md.print_poly(a1))
    polll = list(map(float,a1))
    a_poly = np.array(list(a1),dtype = float)
    if a1[len(a1)-1] == 0:
        a1 = a1[:len(a1)-1]
    for i in range(len(a1)):
        if a1[i]<0:
            first = i
            B=a1[i]
            break
    for i in range(len(a1)):
        if a1[i]<B:
            B = a1[i]
    #print(a1)
    up = 1.0 + (abs(B)/a1[0])**(1/first)
    print(up)
