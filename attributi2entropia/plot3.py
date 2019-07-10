import matplotlib.pyplot as plt
import os
import json
import string
from math import log2

plot = '1'
entropyRange = 0.5

def string_transformer(stringa):
    for punct in string.punctuation:
        stringa = stringa.replace(punct,"")
    stringa = " ".join(stringa.split())
    stringa = stringa.upper()
    return stringa

def append_values(lista, listaDaAppendere):
    
    if(type(listaDaAppendere) == str ):
        currentList = [listaDaAppendere]
    else:
        currentList = listaDaAppendere
    if plot == '2':
        for i in range(len(currentList)):
            currentList[i] = string_transformer(currentList[i])
    lista.extend(currentList)
    return lista

def calculateEntropy(mappa):
    entropy = 0
    totale = mappa["_totale"]
    for value in mappa:
        if value != "_totale":
            parziale = (mappa[value]/totale)
            entropy += -( parziale * log2(parziale))
    return entropy


#"c:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\2013_camera_dataset" #PER WINDOWS
myPath = "/Users/roberto/Desktop/Grafici/2013_camera_dataset"   #PER LINUX

attribute2Values = {}

for filename in os.listdir(myPath):
    #localPath = myPath + "\\" +filename #PER WINDOWS
    localPath = myPath + "/" +filename #PER LINUX
    for element in os.listdir(localPath):
        if element.endswith(".json"):
            #with open(localPath+"\\"+element) as myJson: #PER WINDOWS
            with open(localPath+"/"+element) as myJson:    #PER LINUX
                data = json.load(myJson)
                for attribute in data:
                    evaluating_attr = attribute
                    if(attribute2Values.get(evaluating_attr) == None):
                        currentList = []   
                    else:
                        currentList = attribute2Values.get(evaluating_attr)

                    attribute2Values[evaluating_attr] = append_values(currentList,data[attribute])

attribute2ValuesToCont = {}
if plot == '1':
    for attribute in attribute2Values:
        value2Count = {}
        for value in attribute2Values[attribute]:
            if value2Count.get(value) == None:
                value2Count[value] = 1
            else:
                value2Count[value] += 1
        tot = 0
        for value in value2Count.values():
            tot+=value
        value2Count["_totale"] = tot
        attribute2ValuesToCont[attribute] = value2Count

elif plot == '2':
    for attribute in attribute2Values:
        value2Count = {}
        for value in attribute2Values[attribute]:
            for word in value.split(' '):
                if value2Count.get(word) == None:
                    value2Count[word] = 1
                else:
                    value2Count[word] += 1
                tot = 0
        for value in value2Count.values():
            tot+=value
        value2Count["_totale"] = tot

        attribute2ValuesToCont[attribute] = value2Count

            
attribute2Entropy = {}
for attribute in attribute2ValuesToCont:
    entropy = calculateEntropy(attribute2ValuesToCont[attribute])
    attribute2Entropy[attribute] = entropy


rangeEntropy2NumAttribute = {}

for attribute in attribute2Entropy:
    entropyRanged = int(attribute2Entropy[attribute] / entropyRange)
    if rangeEntropy2NumAttribute.get(entropyRanged) == None:
        rangeEntropy2NumAttribute[entropyRanged] = 1
    else:
        rangeEntropy2NumAttribute[entropyRanged] += 1
print(rangeEntropy2NumAttribute)

asseX = sorted(rangeEntropy2NumAttribute.keys())
asseY = []

for i in asseX:
    asseY.append(rangeEntropy2NumAttribute[i])

bar_width = 0.8
bars = plt.bar(asseX,asseY,width= bar_width)

# indici normali
#plt.xticks(asseX)
asseXticks= []             
for i in asseX:
    left= i*entropyRange
    right = (i*entropyRange)+entropyRange
    tick = "["+str(left)+"-"+str(right)+")"
    asseXticks.append(tick)

# imposto ticks con lista di labels allegata
plt.xticks(asseX, labels=asseXticks, rotation= 45)

plt.xlabel('Range di Entropia (Moltiplicatore ' +str(entropyRange) +' )') 
if plot == '1':
    plt.ylabel('Numero di attributi (non tokenizzati)')
else:
    plt.ylabel('Numero di attributi (tokenizzati)')    
plt.title('Numero di attributi per range di entropia ( base ' +str(entropyRange)+ ')')

for rect in bars:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

plt.show()




 


                        


