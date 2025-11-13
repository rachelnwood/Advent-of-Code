designInputFileName = "Design Input"
candidateInputFileName = "Candidate Input"

with open (designInputFileName) as file:
    designs = [x. strip() for x in file.readlines()]

with open(candidateInputFileName) as file:
    candidates = []
    for line in file:
        # Split by whitespace and convert each to int
        candidates.extend(str(x) for x in line.split(', '))


solvedDesignCount = 0

def isThisDesignSolvable(designToSolve: str, memo=None) -> bool:
    #print(f"design:", designToSolve)
    if memo is None:
        memo = {}

    if designToSolve in memo:
        return memo[designToSolve]

    if designToSolve == "":
        print("solved it!!!!")
        return True

    for candidate in candidates:
        if designToSolve.startswith(candidate):
            if isThisDesignSolvable(designToSolve[len(candidate):], memo):
                memo[designToSolve] = True
                return True

    memo[designToSolve] = False
    return False


# Main section of program follows:
for design in designs:
    print(f"design:", design)
    if isThisDesignSolvable(design) == True:
        solvedDesignCount += 1


print(f"solved count: ", solvedDesignCount)




