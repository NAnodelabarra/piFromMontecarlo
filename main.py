# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:01:46 2020

@author: juani
"""


import random 
import time
import matplotlib.pyplot as plt
import math


f = open("data.csv", "w")
    

tick= 0
  
pto_dentro= 0
pto_fuera= 0
total_pto = 0

for i in range(0,100000000):
    esta_dentro=True
    contador=0
    x= random.uniform(-1, 1) 
    y= random.uniform(-1, 1) 
  
    d= x**2 + y**2
  
    total_pto += 1
    if d<= 1: 
        pto_dentro+= 1
        #plt.plot(x,y, 'o', color='black')
    else:
        esta_dentro=False
        #plt.plot(x,y, 'o', color='red')
        
    pto_fuera+= 1
  
    pi= 4* pto_dentro/total_pto
  
    print("pi se acerca a:", pi)  
    time.sleep(tick)
    contador+=1
    
    plt.plot(total_pto,pi, 'o', color='blue')
    
    results= [x,y,pi,esta_dentro,d,pi/math.pi]
    
    if contador==10:
        plt.show()
    f.write( ','.join([str(x) for x in results])  )
    f.write('\n')
f.close()








