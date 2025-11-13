inputFileName = "PuzzleInput"
masCount = 0

with open (inputFileName) as file:
    map = [x. strip() for x in file.readlines()]


def characterAt(x,y):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return 'f'

    return map[y][x]

def computedXY(startX, startY, cardinalDirection, howManySteps):

    resultX = startX
    resultY = startY

    if cardinalDirection == "E":
        resultX = startX + howManySteps
    if cardinalDirection == "W":
        resultX = startX - howManySteps
    if cardinalDirection == "S":
        resultY = startY + howManySteps
    if cardinalDirection == "N":
        resultY = startY - howManySteps
    if cardinalDirection == "SE":
        resultX = startX + howManySteps
        resultY = startY + howManySteps
    if cardinalDirection == "SW":
        resultX = startX - howManySteps
        resultY = startY + howManySteps
    if cardinalDirection == "NW":
        resultX = startX - howManySteps
        resultY = startY - howManySteps
    if cardinalDirection == "NE":
        resultX = startX + howManySteps
        resultY = startY - howManySteps

    return (resultX, resultY)


def findXMAS(startX, startY):
    global masCount
    # print("Start Location: (", startX,",", startY, ")")  # debugging

    for direction in ["E", "W", "S", "N", "SE", "SW", "NE", "NW"]:
        if characterAt(startX, startY) == 'X':
            nextLocation = computedXY(startX, startY, direction, howManySteps=1)
            if characterAt(nextLocation[0], nextLocation[1]) == "M":
                nextLocation = computedXY(nextLocation[0], nextLocation[1], direction, howManySteps=1)
                if characterAt(nextLocation[0], nextLocation[1]) == "A":
                    nextLocation = computedXY(nextLocation[0], nextLocation[1], direction, howManySteps=1)
                    if characterAt(nextLocation[0], nextLocation[1]) == "S":
                        xmasCount += 1


def whereIsX():
    y = 0
    for row in map:
        # print(row)

        x = 0
        while True:
            xLocation = row.find('X', x)
            if xLocation == -1:
                break

            findXMAS(xLocation, y)
            x = xLocation + 1

        y = y + 1


whereIsX()
print("xmas count: ", masCount)