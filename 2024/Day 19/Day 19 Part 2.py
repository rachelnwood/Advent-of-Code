designInputFileName = "Design Input"
candidateInputFileName = "Candidate Input"

with open (designInputFileName) as file:
    designs = [x. strip() for x in file.readlines()]

with open(candidateInputFileName) as file:
    candidates = []
    for line in file:
        # Split by whitespace and convert each to int
        candidates.extend(str(x) for x in line.split(', '))

# returns the count of solutions for this designToSolve.
def designSolutionCount(designToSolve: str, memo=None) -> int:
    if memo is None:
        memo = {}

    if designToSolve in memo:
        print(f"memo solve:", memo[designToSolve])
        return memo[designToSolve]

    if designToSolve == "":
        print(f"solved it!!!!")
        return 1

    solvedDesignCount = 0
    for candidate in candidates:
        if designToSolve.startswith(candidate):
            solvedDesignCount += designSolutionCount(designToSolve[len(candidate):], memo)

    memo[designToSolve] = solvedDesignCount
    return solvedDesignCount


# Main section of program follows:
totalCount = 0

for design in designs:
    print(f"design:", design)
    totalCount += designSolutionCount(design)

print(f"solved count: ", totalCount)





