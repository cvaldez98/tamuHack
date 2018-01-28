import csv


class museumData():

    def __init__(self):
        readMyFile(self, 'museums.csv')

    def readMyFile(self, filename):
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


#museumName, city, state = readMyFile('static/museums.csv')
    def getMuseum(cityName):
        outputMuseum = []
        for i in range(0, len(city)):
            if (city[i] == cityName):  # enter what the user put for their location
                outputMuseum.append(museumName[i])
        return outputMuseum
