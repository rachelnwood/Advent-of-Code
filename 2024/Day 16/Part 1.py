import sys
sys.setrecursionlimit(10000)

inputFileName = "Puzzle Input"

with open (inputFileName) as file:
    map = [x. strip() for x in file.readlines()]

for line in map:
    print(line)

cardinalDirections = {'west':  (-1,  0), 'north': ( 0, -1), 'east':  ( 1,  0), 'south': ( 0,  1)}

bestScore = float('inf')
bestCost = {}
# cachedScores = {} # key: x,y,direction value: score

def startLocation():
    lineCount = len(map)
    rowLength = len(map[0])

    for y in range(lineCount):
        for x in range(rowLength):
            if characterAtXY(x, y) == 'S':
                return x, y

def characterAtXY(x,y):
    return map[y][x]

def possibleDirections(currentX, currentY, lastX, lastY):
    result = {}

    for key in cardinalDirections.keys():
        x, y = newLocation(currentX, currentY, key)

        if (x, y) == (lastX, lastY):
            char = "#"
        else:
            char = characterAtXY(x, y)

        if char == "." or char == 'E':
            result[key] = "We can go this way"

    return result  # [west, north, east, south]

def calculateScore(score, facingDirection, newFacingDirection):
    if facingDirection == newFacingDirection:
        score += 1
    else:
        score += 1000 + 1

    return score

def newLocation(x, y, direction):
    dx, dy = cardinalDirections[direction]

    newX = x + dx
    newY = y + dy

    return newX, newY

def exploreDirections(x, y, directions, score, facingDirection, visitedLocation):
    global bestScore, bestCost

    # If we reached the end, update bestScore
    if characterAtXY(x, y) == 'E':
        print(f"found E with score of {score}")
        if score < bestScore:
            bestScore = score
        return score

    # Simple cycle prevention in current recursion path
    pos_key = (x, y)
    if pos_key in visitedLocation:
        return 0

    # Prune if score already exceeds global best
    if score >= bestScore:
        # reached a path that can't beat the best found
        return 0

    # Prune using best known cost to reach this state (position + facing)
    state = (x, y, facingDirection)
    bestKnown = bestCost.get(state, float('inf'))
    if score >= bestKnown:
        # We've been here with an equal or better score; no need to explore
        return 0
    # record that we reached this state with this (better) score
    bestCost[state] = score

    # mark visited (for cycle prevention in this branch)
    visitedLocation.add(pos_key)

    scores = []

    # iterate over a snapshot of directions; don't mutate 'directions' inside loop
    for direction in list(directions.keys()):
        # compute next position and available directions there
        newX, newY = newLocation(x, y, direction)
        next_dirs = possibleDirections(newX, newY, x, y)
        new_score = calculateScore(score, facingDirection, direction)

        # further prune: if new_score already >= bestScore, skip
        if new_score >= bestScore:
            continue

        # recursive call; pass the same visitedLocation set (we add/remove inside recursion)
        child_score = exploreDirections(newX, newY, next_dirs, new_score, direction, visitedLocation)
        if child_score > 0:
            scores.append(child_score)

    # backtrack visited
    visitedLocation.remove(pos_key)

    if not scores:
        return 0
    return min(scores)

# main program
visitedLocations = set()
currentX, currentY = startLocation()
initialDirection = 'east'
print(currentX, currentY)

directions = possibleDirections(currentX, currentY, currentX, currentY)
print(f'Directions We Can Go:', list(directions.keys()))

score = exploreDirections(currentX, currentY, directions, 0, initialDirection, visitedLocations)
print(score)
# correct best answer: 88416
