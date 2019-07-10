import matplotlib.pyplot as plt
import os
import json
import numpy as np

# ampiezza intervalli rappresentati
rangeSorgenti = 100

#"c:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\2013_camera_dataset" #PER WINDOWS
myPath = "/Users/roberto/Desktop/Grafici/2013_camera_dataset"   #PER LINUX

numJson2numSorgenti = {}

for filename in os.listdir(myPath):
    numJson= 0
    #localPath = myPath + "\\" +filename #PER WINDOWS
    localPath = myPath + "/" +filename #PER LINUX
    for element in os.listdir(localPath):
        if element.endswith(".json"):
            numJson+=1
    if numJson2numSorgenti.get(numJson) == None:
        numJson2numSorgenti[numJson] = 1
    else:
        numJson2numSorgenti[numJson]+= 1   

print(numJson2numSorgenti.items())

sortedDict = sorted(numJson2numSorgenti.items(),reverse=False)


#mappa {intervallo -> n°di sorgenti}
range2sorgenti = {}
for x in sortedDict:
    tmp = int(x[0]/rangeSorgenti)
    if range2sorgenti.get(tmp)==None:
        range2sorgenti[tmp]=1
    else:
        range2sorgenti[tmp]+=1


xTicks= []
asseX = []
asseY = []
x_pos = [] 
cont = 0

for i in range2sorgenti.items():
    index=i[0]
    left=index*rangeSorgenti
    rigth=(index*rangeSorgenti)+rangeSorgenti
    tick = "["+str(left)+"-"+str(rigth)+")"
    xTicks.append(tick)
    asseX.append(cont)
    asseY.append(i[1])
    x_pos.append(cont)
    cont+=1

plt.bar(asseX,asseY)
plt.xticks(x_pos, labels=xTicks, rotation=20)

maxSourceNumber= max(range2sorgenti.values())
plt.yticks(np.arange(maxSourceNumber+1))

plt.xlabel('N° JSON')
plt.ylabel('N° Sorgenti')
plt.title('Numero di JSON/numero di sorgenti ')
plt.show()

