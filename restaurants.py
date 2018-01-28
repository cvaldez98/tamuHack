import csv

class restaurantData():

    def __init__(self):
        readMyFile(self, filename)

    def readMyFile(self, filename):
        city = []
        restaurantName = []
        #state = []

        with open(filename) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                restaurantName.append(row[20])
                city.append(row[2])
                #state.append(row[8])
        return restaurantName, city

    def getRestaurant(cityName):
        for i in range(0, len(city)):
            if(city[i] == cityName): #enter what the user put for their location
                return(restaurantName[i]) #returns a single restaurant, the first on the list..
