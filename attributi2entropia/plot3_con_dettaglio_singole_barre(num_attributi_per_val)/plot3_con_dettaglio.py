import matplotlib.pyplot as plt
import os
import numpy as np
import json
import string
from math import log2

plot = '1'
entropyRange = 0.5

def string_transformer(stringa):
    for punct in string.punctuation:
        stringa = stringa.replace(punct," ")
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

  # ------------ #
  # mod
            
attribute2Entropy = {}
for attribute in attribute2ValuesToCont.keys():
    entropy = calculateEntropy(attribute2ValuesToCont[attribute])
    attribute2Entropy[attribute] = entropy
print(len(attribute2Entropy.keys()))


entropyRangeIndex2attributes={}
for attribute in attribute2Entropy.keys():
    entropy=attribute2Entropy.get(attribute)
    index=int(entropy/entropyRange)
    if entropyRangeIndex2attributes.get(index)==None:
        entropyRangeIndex2attributes[index]=[attribute]
    else :
        entropyRangeIndex2attributes[index].append(attribute)

        


# scelgo intervallo di entropia da visualizzare

#print(entropyRangeIndex2attributes.get(indexRange))
for indexRange in sorted(entropyRangeIndex2attributes.keys()):
# asse x = n° valori diversi | asse y= n° di attr.
    occorrenze2attributi={}
    for attribute in entropyRangeIndex2attributes[indexRange]:
        values = attribute2ValuesToCont.get(attribute).keys()
        number = len(values) -1
        if occorrenze2attributi.get(number)==None:
            occorrenze2attributi[number]=[attribute]
        else:
            occorrenze2attributi[number].append(attribute)


    sortedKeys=sorted(occorrenze2attributi.keys())
    asseX=np.arange(len(sortedKeys))

    asseY=[]
    for y in sortedKeys:
        asseY.append(len(occorrenze2attributi.get(y)))




    bar_width = 0.8
    bars = plt.bar(asseX,asseY,width= bar_width)
    plt.xticks(asseX, labels=sortedKeys, rotation= 45)

    plt.xlabel('Numero di valori') 

    if plot == '1':
        plt.ylabel('Numero di attributi (no token)')
    else:
        plt.ylabel('Numero di attributi  (token)')    
    plt.title('Number of attributes to entropy range   ( base ' +str(entropyRange)+ ')')
    left= indexRange*entropyRange
    right = (indexRange*entropyRange)+entropyRange
    label = "["+str(left)+"-"+str(right)+")"
    plt.title('Numero di attributi per valori distinti intervallo: ' +label)


    for rect in bars:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

    plt.show()




 


                        


