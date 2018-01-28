import csv

class museumData():

    def __init__(self):


    def getMuseum(self):




def readMyFile(filename):
    city = []
    museumName = []
    state = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            museumName.append(row[1])
            city.append(row[7])
            state.append(row[8])

    return museumName, city, state


museumName, city, state= readMyFile('static/museums.csv')

for i in range(0, len(city)):
    if(city[i] == "ANCHORAGE"): #enter what the user put for their location
        print(museumName[i])
