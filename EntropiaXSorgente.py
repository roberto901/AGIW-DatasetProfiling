import matplotlib.pyplot as plt
import os
import json
from math import log2
import operator

myPath = "c:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\2013_camera_dataset"

sorgente2Attributes = {}

for filename in os.listdir(myPath):
    localPath = myPath + "\\" +filename
    for element in os.listdir(localPath):
        if element.endswith(".json"):
            with open(localPath+"\\"+element) as myJson: 
                data = json.load(myJson)
                for attribute in data:
                    evaluating_attr = attribute
                    if(sorgente2Attributes.get(filename) == None):
                        sorgente2Attributes[filename] = [evaluating_attr]   
                    else:
                        if(evaluating_attr not in sorgente2Attributes[filename]):
                            sorgente2Attributes[filename].append(evaluating_attr)
    sorgente2Attributes[filename] = sorted(sorgente2Attributes[filename])


sorgente2Jsons2Vettore = {}

for filename in os.listdir(myPath):

    currentAttributes = sorgente2Attributes[filename]
    sorgente2Jsons2Vettore[filename] = {}
    localPath = myPath + "\\" +filename
    initialVector = []
    for attribute in currentAttributes:
        initialVector.append(0)

    for element in os.listdir(localPath):
        if element.endswith(".json"):
            with open(localPath+"\\"+element) as myJson:
                data = json.load(myJson)
                currentVector = initialVector.copy()    

                for attribute in data:
                    index = currentAttributes.index(attribute)
                    currentVector[index] = 1
                sorgente2Jsons2Vettore[filename][element] = currentVector


def vecArrayToString (vecArray):
    string = ''
    for i in vecArray:
        string+= str(i)
    return string

sorgente2Vettore2count = {}

for sorgente in sorgente2Jsons2Vettore:
    sorgente2Vettore2count[sorgente] = {}
    for json in sorgente2Jsons2Vettore[sorgente]:
        vettore =  vecArrayToString(sorgente2Jsons2Vettore[sorgente][json])
        if sorgente2Vettore2count[sorgente].get(vettore) == None:
            sorgente2Vettore2count[sorgente][vettore] = 1
        else:
            sorgente2Vettore2count[sorgente][vettore]+= 1



def calculateEntropy(mappa,totale):

    entropy = 0
    
    for value in mappa:
        parziale = (mappa[value]/totale)
        entropy += -( parziale * log2(parziale))

    return entropy

sorgente2Entropy = {}

for sorgente in sorgente2Vettore2count: 
    vettore2count = sorgente2Vettore2count[sorgente]
    tot = len(sorgente2Jsons2Vettore[sorgente].keys())
    entropy = calculateEntropy(vettore2count,tot)
    sorgente2Entropy[sorgente] = entropy

print('ok')



asseX = []
asseY = []
xticks = []
sorted_d = sorted(sorgente2Entropy.items(), key=operator.itemgetter(1),reverse=True)

for tup in sorted_d:
    asseX.append(tup[0])
    asseY.append(tup[1])


bar_width = 0.8
bars = plt.bar(asseX,asseY,width= bar_width)

for i in asseX:
    splitted = i.split('.')
    if(len(splitted)>2):
        xticks.append(splitted[1])
    else:
        xticks.append(splitted[0])
    
    
plt.xticks(asseX, labels=xticks, rotation=40 )

plt.xlabel('Sorgente') 
plt.ylabel('Entropia')
plt.title('Entropia per sorgente')

for rect in bars:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' % float(height), ha='center', va='bottom')

plt.show()
    






