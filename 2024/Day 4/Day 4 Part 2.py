# When A is found, search in diagonal directions for one 'M' and one 'S'
# if two 'MAS's are found, accumulate counter


inputFileName = "PuzzleInput"
masCount = 0

with open (inputFileName) as file:
    map = [x. strip() for x in file.readlines()]


def characterAt(x,y):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 'f'

    return map[y][x]

def computedXY(startX, startY, cardinalDirection):
    if cardinalDirection == "SE":
        resultX = startX + 1
        resultY = startY + 1
    if cardinalDirection == "SW":
        resultX = startX - 1
        resultY = startY + 1
    if cardinalDirection == "NW":
        resultX = startX - 1
        resultY = startY - 1
    if cardinalDirection == "NE":
        resultX = startX + 1
        resultY = startY - 1

    return (resultX, resultY)


def findMAS(startX, startY):
    global masCount
    xLegCount = 0
    # print("Start Location: (", startX,",", startY, ")")  # debugging

    # for direction in ["NE", "SW"]:
    #if characterAt(startX, startY) == 'A':

    # Find our locations of interest
    NELocation = computedXY(startX, startY, 'NE')
    SWLocation = computedXY(startX, startY, 'SW')
    NWLocation = computedXY(startX, startY, 'NW')
    SELocation = computedXY(startX, startY, 'SE')

    # Find our characters of interest
    NEChar = characterAt(NELocation[0], NELocation[1])
    SWChar = characterAt(SWLocation[0], SWLocation[1])
    NWChar = characterAt(NWLocation[0], NWLocation[1])
    SEChar = characterAt(SELocation[0], SELocation[1])

    # Write all checking here from NE to SW
    if NEChar  == 'M' and SWChar == 'S':
        xLegCount += 1
    if NEChar == 'S' and SWChar == 'M':
        xLegCount += 1
    if NWChar == 'M' and SEChar == 'S':
        xLegCount += 1
    if NWChar == 'S' and SEChar == 'M':
        xLegCount += 1

    if xLegCount == 2:
        masCount += 1


def whereIsA():
    y = 0
    for row in map:
        # print(row)

        x = 0
        while True:
            xLocation = row.find('A', x)
            if xLocation == -1:
                break

            findMAS(xLocation, y)
            x = xLocation + 1

        y = y + 1


whereIsA()
print("x-mas count: ", masCount)
