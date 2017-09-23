# coding=utf-8
import pandas as pd
import numpy as np
from config.neighborhoods import Neighborhoods

dataFrame = pd.read_csv('data/uber_map.csv')

def rgb(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    r = 255
    ratio = (value-minimum)/(maximum - minimum)
    bg = 20 + int(max(0, 235*ratio))
    b =  bg
    g = bg
    return r, g, b

nb_avgs = []
for nbhood in Neighborhoods:
    requests = []
    for request in dataFrame[nbhood['name']]:
        requests.append(request)
    avg = np.mean(requests)
    if not nbhood['name']=="Salinas":
        nb_avgs.append(avg)
    print nbhood['name'],":",avg

minimo = np.min(nb_avgs)
maximo = np.max(nb_avgs)
print ("Minimo:", minimo)
print ("Maximo:", maximo)

index = 0
for nbhood in Neighborhoods:
    print nbhood['name']
    if not nbhood['name']=="Salinas":
        print rgb(minimo, maximo, nb_avgs[index])
        index = index + 1
    
