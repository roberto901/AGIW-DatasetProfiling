import matplotlib.pyplot as plt
import os
import json

#"c:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\2013_camera_dataset" #PER WINDOWS
myPath = "/Users/roberto/Desktop/Grafici/2013_camera_dataset"   #PER LINUX
index_distance= 5 #distanza tra due pedici
numAttrib2numJson = {}

for filename in os.listdir(myPath):
    #localPath = myPath + "\\" +filename #PER WINDOWS
    localPath = myPath + "/" +filename #PER LINUX
    for element in os.listdir(localPath):
        if element.endswith(".json"):
            #with open(localPath+"\\"+element) as myJson: #PER WINDOWS
            with open(localPath+"/"+element) as myJson:    #PER LINUX
                data = json.load(myJson)
                st = len(data)
                if numAttrib2numJson.get(st) == None:
                    numAttrib2numJson[st] = 1
                else:
                    numAttrib2numJson[st] += 1

print(numAttrib2numJson.items())

sortedDict = sorted(numAttrib2numJson.items())

asseX = []
asseY = []

for i in sortedDict:
    asseX.append(i[0])
    asseY.append(i[1])

bar_width = 0.8
plt.bar(asseX,asseY,width= bar_width)


x_ticks = [] 

for i in range(max(asseX)):
    if i % index_distance ==0:
        x_ticks.append(i)
if max(asseX)% index_distance != 0:
        x_ticks.append(max(asseX))
    
plt.xticks(x_ticks)


plt.xlabel('N° Attributi')
plt.ylabel('N° JSON')
plt.title('Attributi per JSON')

plt.show()

