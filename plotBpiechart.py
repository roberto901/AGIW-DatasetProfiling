import matplotlib.pyplot as plt
import os
import json


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

sortedDict = sorted(numJson2numSorgenti.items(),reverse=True)

xTicks= []
asseX = []
asseY = []
y_pos = [] 
cont = 0
for i in sortedDict:
    xTicks.append(i[0])
    asseX.append(cont)
    asseY.append(i[1])
    y_pos.append(cont)
    cont+=1


#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

sizes=[]
total=0

for i in asseY:
    total+=i

for i in asseY:
    sizes.append((i*100/total))

def myFunc(evt):
    return str(int(round(evt*total/100)))+'/'+str(total)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=xTicks, autopct=myFunc,
        shadow=False, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

