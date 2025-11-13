import time

from datetime import datetime

inputFileName = "Test Input"

with open(inputFileName) as file:
    numbers = []
    for line in file:
        # Split by whitespace and convert each to int
        numbers.extend(int(x) for x in line.split())


def oneBlink():
    results = []
    global numbers

    for stone in numbers:
        if stone == 0:
            results.append(1)
        else:
            stoneString = str(stone)
            countOfDigits = len(stoneString)

            if countOfDigits % 2 == 0:
                halfLength = int(countOfDigits / 2)
                leftStoneString = stoneString[:halfLength]
                rightStoneString = stoneString[halfLength:]

                results.append(int(leftStoneString))
                results.append(int(rightStoneString))
            else:
                newStone = stone * 2024
                results.append(newStone)

    numbers = results

    numberOfStones = len(results)
    print('Stone Count:', numberOfStones)

for index in range(75):
    print(datetime.now().strftime("%H:%M:%S"))
    print("loopIndex: ", index)

    oneBlink()

print("Finished")

#####################
#####################
#####################
#####################
# This is the dictionary based solution we did the 75 blinks with

from collections import Counter

def transform(n):
    if n == 0:
        return [1]
    s = str(n)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return [int(s[:mid]), int(s[mid:])]
    else:
        return [n * 2024]

# Starting with 3 and 0
stone_counts = Counter([27, 10647, 103, 9, 0, 5524, 4594227, 902936])

# Show initial state
print("Blink 0:", dict(stone_counts))

# Run a few blinks
for blink in range(75):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        for new_stone in transform(stone):
            new_counts[new_stone] += count
    stone_counts = new_counts
    print(f"Blink {blink}: stoneCount: {sum(stone_counts.values())} unique numbers: {len(stone_counts.keys())}", dict(stone_counts))

