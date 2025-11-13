import time
start_time = time.time()

#inputFileName = "input-sample.txt" # 10x10 sample map from website. Correct answer: 6
inputFileName = "rwday6part2input.txt" # 130x130 data map for logged in account. Correct answer: 2262 which takes 228 seconds to compute

with open (inputFileName) as file:
    map = [x. strip() for x in file.readlines()]

# print("map: \n", map)

originalMap = map.copy()

height = len(map)
print('The room height is:', height)

width = len(map[0])
print('The room width is:', width)

guardCharacters = "^><v"

def increaseCountAtLocation(location):
    x = location[0]
    y = location[1]
    row = countMap[y]
    row[x] += 1


def countAtLocation(location):
    x = location[0]
    y = location[1]
    row = countMap[y]
    return row[x]


def guardLocation(inputMap):
    for guardCharacter in guardCharacters:
        y = 0
        # print(guardCharacter)

        for row in inputMap:
            x = row.find(guardCharacter)
            if x > -1:
                # print(x, y)
                return (x, y)
            y = y + 1

    raise Exception('There is no guard on this map')


def makeSecondMap(width, height):
    secondMapList = []
    for number in range(height):
        row = []
        for item in range(width):
            row.append(0)

        secondMapList.append(row)
    return secondMapList


def characterAtLocation(location):
    x = location[0]
    y = location[1]
    if x < 0 or y < 0:
        raise Exception('Invalid X or Y value')
    row = map[y]
    char = row[x]
    return char


def obstacleAt(location):
    char = characterAtLocation(location)
    if char == '#':
        return True
    else:
        return False


def nextGuardLocation(location, guardCharacter):
    x = location[0]
    y = location[1]
    if guardCharacter == '^':
        return x, y - 1
    elif guardCharacter == '>':
        return x + 1, y
    elif guardCharacter == 'v':
        return x, y + 1
    elif guardCharacter == '<':
        return x - 1, y


def replaceCharacterInMap(location, newCharacter):
    x = location[0]
    y = location[1]
    row = map[y]
    newRow = row[:x] + newCharacter + row[x + 1:]
    map[y] = newRow


def guardRotation():
    currentLocation = guardLocation(map)
    guardCharacter = characterAtLocation(currentLocation)

    if guardCharacter == '^':
        guardCharacter = '>'
    elif guardCharacter == '>':
        guardCharacter = 'v'
    elif guardCharacter == 'v':
        guardCharacter = '<'
    elif guardCharacter == '<':
        guardCharacter = '^'

    replaceCharacterInMap(currentLocation, guardCharacter)


def isThisLocationOnTheMap(location):
    x = location[0]
    y = location[1]
    if x < 0:
        return False
    if y < 0:
        return False
    if x >= width:
        return False
    if y >= height:
        return False

    return True

guardStartingLocation = guardLocation(map)

def doesThisLoop():
    currentLocation = guardStartingLocation
    while True:
        guardCharacter = characterAtLocation(currentLocation)
        nextLocation = nextGuardLocation(currentLocation, guardCharacter)
        if isThisLocationOnTheMap(nextLocation) is False:
            break

        blocked = obstacleAt(nextLocation)
        # print('The guard is at', currentLocation)
        # print('Next guard location is', nextLocation)
        # print('Next location is on the map:', isThisLocationOnTheMap(nextLocation))
        # print('Obstacle at this location?', blocked)

        if blocked == True:
            guardRotation()
        else:
            increaseCountAtLocation(currentLocation)
            if countAtLocation(currentLocation) == 5:
                return True

            replaceCharacterInMap(nextLocation, guardCharacter)
            # print(map)
            replaceCharacterInMap(currentLocation, '.')
            currentLocation = nextLocation

    return False


obstacleCauseLoopsCount = 0
countMap = makeSecondMap(width, height)
print(countMap)

guardStartingLocation = guardLocation(map)

for y in range(height):
    print('Y =', y)
    for x in range(width):
        location = (x, y)
        #print(location)
        if guardStartingLocation == location:
            print("Guard was skipped")
            continue
        replaceCharacterInMap(location, '#')
        #print(map)

        result = doesThisLoop()
        if result is True:
            obstacleCauseLoopsCount += 1

        #print(countMap)
        map = originalMap.copy()
        countMap = makeSecondMap(width, height)

end_time = time.time()
print("compute time", end_time - start_time)

print("There are", obstacleCauseLoopsCount, "spots that create loops")