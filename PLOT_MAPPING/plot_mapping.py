import matplotlib.pyplot as plt
import os
import json
import string
from math import log2
import csv



myPath ="c:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\2013_camera_dataset" #PER WINDOWS
#myPath = "/Users/roberto/Desktop/Grafici/2013_camera_dataset"   #PER LINUX
tsv1 ='C:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\camera.tsv'
tsv2 ='C:\\Users\\Simone\\Desktop\\università\\AGIW\\Progetto_2\\monitor.tsv'
titles = {}
titles[tsv1] = "Dataset Camera"
titles[tsv2] = "Dataset Monitor"
arr = []

arr.append(tsv1)
arr.append(tsv2)
'''
with open(tsv1, encoding = 'utf-8') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    try:
        print(row)
    except:
        print('----')
'''
for path in arr:
    sourceMapping2values = {}

    with open(path, encoding = 'utf-8') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            lista =[row['source'],row['attribute_name'],row['predicate_name']]
            if lista[2]!='':   
                key = lista[1]+'_'+lista[0]
                if sourceMapping2values.get(key)== None:
                    sourceMapping2values[key]=[lista[2]]
                else:
                    sourceMapping2values[key].append(lista[2])

    print (sourceMapping2values.items())


    len2Count = {}
    for source in sourceMapping2values:
        length = len(sourceMapping2values[source])
        if len2Count.get(length) == None:
            len2Count[length] = 1
        else:
            len2Count[length] += 1




    asseX = []
    asseY = []

    for i in len2Count:
        asseX.append(int(i))
        asseY.append(int(len2Count[i]))
          

    bar_width = 0.8
    bars = plt.bar(asseX,asseY,width= bar_width)





    plt.ylabel('N° di source attributes')
    plt.xlabel('N° di target attributes)')

    plt.title('# di target attributes / # di source attributes ('+titles[path]+')')


    for rect in bars:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom')

    plt.show()




                
