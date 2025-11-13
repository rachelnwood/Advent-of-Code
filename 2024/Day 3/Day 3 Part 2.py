from wsgiref.validate import header_re

inputFileName = "input.txt"

with open (inputFileName) as file:
    listOfInputStrings = [x. strip() for x in file.readlines()]
print("test data: ", listOfInputStrings)

def validNumberAtIndex(index):
    validNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    firstChar = inputString[index]
    secondChar = inputString[index+1]
    thirdChar = inputString[index+2]
    fourthChar = inputString[index+3]

    if firstChar in validNumbers and secondChar == ',' or secondChar == ')':
        foundNumber = int(firstChar)
        foundNumberLength = 1
        return True, foundNumber, foundNumberLength
    elif firstChar in validNumbers and secondChar in validNumbers and thirdChar == ',' or thirdChar == ')':
        foundNumber = int(firstChar + secondChar)
        foundNumberLength = 2
        return True, foundNumber, foundNumberLength
    elif firstChar in validNumbers and secondChar in validNumbers and thirdChar in validNumbers and fourthChar == ',' or fourthChar == ')':
        foundNumber = int(firstChar + secondChar + thirdChar)
        foundNumberLength = 3
        return True, foundNumber, foundNumberLength
    else:
        return False, -1, 0

#substring = "mul("
mulList = []
doList = []
dontList = []
finalList = []
inputString = listOfInputStrings[0]
results = 0

def buildMeAList(substring, list):
    start = 0

    while True:
        start = inputString.find(substring, start)
        if start == -1:
            break
        list.append(start)
        start += len(substring) #start = start + len(substring) is the same as this line **PUT ON CHEAT SHEET**

def smallerListItem(candidate):
    if (len(dontList) > 0 and dontList[0] < candidate) and ((len(doList) == 0) or (len(doList) > 0 and dontList[0] < doList[0])):
        return 0 # answer: dontList
    if len(doList) > 0 and doList[0] < candidate:
        return 1 # answer: doList

    return -1 # answer: candidate

def buildFinalList():
    addMultiplies = True
    while len(mulList) > 0:
        candidate = mulList[0]
        listToProcess = smallerListItem(candidate)
        if listToProcess == 0: # dontList
            addMultiplies = False
            del dontList[0]
            continue
        if listToProcess == 1: # doList
            addMultiplies = True
            del doList[0]
            continue

        if addMultiplies == True:
            finalList.append(candidate)

        del mulList[0] # Add the candidate


def setUpTheWorld():
    buildMeAList('mul(', mulList)
    print('mul list content:', mulList)
    buildMeAList('do()', doList)
    print('do list content:', doList)
    buildMeAList("don't()", dontList)
    print('dont list content:', dontList)

    buildFinalList()
    print('finalList:', finalList)

setUpTheWorld()
substring = 'mul('

for index in finalList:
    print(index)
    potentialFirstNumberIndex = index + len(substring)
    didWeFindAFirstNumber, firstNumber, firstNumberLength = validNumberAtIndex(potentialFirstNumberIndex)
    if didWeFindAFirstNumber == True:
        print("Found First Number:", firstNumber, "\nNumber Length is:", firstNumberLength)
        potentialSecondNumberIndex = index + len(substring) + firstNumberLength + 1
        didWeFindASecondNumber, secondNumber, secondNumberLength = validNumberAtIndex(potentialSecondNumberIndex)
        if didWeFindASecondNumber == True:
            print('Found Second Number:', secondNumber, "\nNumber Length is:", secondNumberLength)
            multiplyResult = firstNumber * secondNumber
            print("Multiply Result:", multiplyResult)
            results += multiplyResult
            print("results: ", results)
    else:
        print("not a number!")

