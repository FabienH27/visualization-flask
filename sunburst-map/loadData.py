import csv  
import json

data = {"Data": {}}

file = "data/REF_PROD_TMP.csv"

with open(file,encoding='utf-8-sig') as fh:
    reader = csv.reader(fh)
    row1 = next(reader)
    tempData = data['Data']
    for line in row1:
        description = list(line.strip().split(";", 16))
        for field in description[0:4]:
            tempData[field] = {}
    i = 0
    for row in fh:
        description = list(row.strip().split(";", 16))

        #Insertion des entetes de chaque section dans le dictionnaire
        for dt, desc in zip(tempData,description):
            if(desc not in tempData[dt]):
                tempData[dt].update({desc: {}})

        #Liste avec toutes les données de chaque production
        valueList = []
        prodList = {}
        for value in description[4:16]:
            valueList.append(int(value))
        i += 1
        prodList.update({"prod" + str(i): valueList})

        #Asssignation des données dans le dictionnaire
        for dt,desc in zip(tempData,description):
            for key in tempData[dt].keys():
                if(desc == key):
                    tempData[dt][key].update(prodList)

#Ecriture dans le fichier
out_file = open("data.json", "w",encoding='utf-8')
json.dump(data, out_file, indent=4,ensure_ascii=False)
out_file.close()