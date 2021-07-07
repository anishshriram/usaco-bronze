"""
ID: ashrira1
LANG: PYTHON3
TASK: beads
"""

f = open('beads.in')
f = f.readlines()

numBeads = int(f[0])
beads = f[1]

answer = 0


# every white encompassed by one color should turn into that color
# should the remaining whites be red or blue ? what's the biggest chain to the left or right
# only have to choose an index point to start traversing from if there's a color discrepancy in between adjacent beads

def changeWhiteColor(beads, i):
    # pretend we only to figure out what this specific white color should change to

    rightIndex = i + 1
    while beads[rightIndex] == "w":
        rightIndex += 1
        if rightIndex >= len(beads):
            rightIndex = 0

    leftIndex = i - 1
    while beads[leftIndex] == "w":
        leftIndex -= 1
        if leftIndex <= -1:
            leftIndex = len(beads) - 1

    if beads[leftIndex] == beads[rightIndex]:
        return beads[leftIndex]
    else:
        rightIndexPointer = rightIndex
        leftIndexPointer = leftIndex
        rightCount = 0
        leftCount = 0

        while beads[rightIndexPointer] == beads[rightIndex]:
            rightIndexPointer += 1
            rightCount += 1
            if rightIndexPointer >= len(beads):
                rightIndexPointer = 0

        while beads[leftIndexPointer] == beads[leftIndex]:
            leftIndexPointer -= 1
            leftCount += 1
            if leftIndexPointer <= -1:
                leftIndexPointer = len(beads) - 1

        if leftCount > rightCount:
            return beads[leftIndex]
        else:
            return beads[rightIndex]


# strings are immutable
def assignWhiteBeads(beads):
    coloredBeads = ""
    for i in range(0, len(beads), 1):
        if beads[i] == 'w':
            coloredBeads += changeWhiteColor(beads, i)
        else:
            coloredBeads += beads[i]
    return coloredBeads


def countTotal(beads):
    beads = assignWhiteBeads(beads)
    tempAns = 0

    for i in range(0, len(beads), 1):

        rightIndex = i
        leftIndex = i - 1

        if leftIndex <= -1:
            leftIndex = len(beads) - 1

        if rightIndex >= len(beads):
            rightIndex = 0

        if beads[rightIndex] != beads[leftIndex]:

            rightIndexPointer = rightIndex
            leftIndexPointer = leftIndex
            rightCount = 0
            leftCount = 0

            while beads[rightIndexPointer] == beads[rightIndex]:
                rightIndexPointer += 1
                rightCount += 1
                if rightIndexPointer >= len(beads):
                    rightIndexPointer = 0

            while beads[leftIndexPointer] == beads[leftIndex]:
                leftIndexPointer -= 1
                leftCount += 1
                if leftIndexPointer <= -1:
                    leftIndexPointer = len(beads) - 1

            countTotal = rightCount + leftCount

            if (countTotal > tempAns):
                tempAns = countTotal

    return tempAns


answer = countTotal(beads)

o = open('beads.out', 'w+')
o.write(str(answer) + '\n')
o.close()
