import random
import math
import statistics

NUM_RUNS = 100
NUM_GENERATIONS = 100
POLICY_SIZE = 10

# ! Make this a function that generates a random list of 20 ints, [-1, 1]
def initializeBitString():
    policy = []
    for i in range(POLICY_SIZE):
        policy.append(random.randint(-1, 1))
    return policy


# finalPolicy stores the policy generated by enumerate with the best score
finalPolicy = []

# bestScore stores the actual sum of elements from finalPolicy
bestScore = []
bestPolicy = []

# score pertinent to each run
score = 0

# score per generation
scoreGeneration = []

for run in range(NUM_RUNS):
    bestScore.append(0)
    bestPolicy.append([])
    scoreGeneration.append([])

    for gen in range(NUM_GENERATIONS):
        position = POLICY_SIZE
        # ! Create a variable for policy, also a list of 10 ints
        policy = initializeBitString()

        policyList = []
        for i in range(POLICY_SIZE*2+1):
            policyList.append(0)

        for k in range(len(policy)):
            position = position + policy[k]
            policyList[position] = 1

        score = 0

        for space in policyList:
            if space == 1:
                score = score + 1

        if score > bestScore[run]:
            bestScore[run] = score
            bestPolicy[run] = policy

        scoreGeneration[run].append(bestScore[run])

topScore = bestScore[0]
topPolicy = bestPolicy[0]
topScorePerGeneration = scoreGeneration[0]

for run in range(NUM_RUNS):

    if bestScore[run] > topScore:
        topScore = bestScore[run]
        topPolicy = bestPolicy[run]
        topScorePerGeneration = scoreGeneration[run]


avgScore = statistics.mean(bestScore)
stdScore = statistics.stdev(bestScore)

print("Top Score: ", topScore)
print("\nTop Policy: ", topPolicy)
print("\nAvg Score: ", avgScore)
print("\nStd. Dev: ", stdScore)
print("\nScore Per Gen: ", topScorePerGeneration)