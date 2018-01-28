import csv

def readMyFile(filename):
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


restaurantName, city = readMyFile('r.csv')

for i in range(0, len(city)):
    if(city[i] == "Brooklyn"): #enter what the user put for their location
        print(restaurantName[i])
