
def treeFinder(slopeX: int, slopeY: int):
    currIndex = 0
    treeCount = 0
    with open('input.txt') as f:
        Lines = f.readlines()
        width = len(Lines[0].strip())
        # print("Width: " + str(width))
        for lineNum, line in enumerate(Lines[1:], 1):
            if(lineNum % slopeY != 0):
                continue
            line = line.strip()
            currIndex += slopeX
            # print("CurrIndex: " + str(currIndex) + " Index: " + str(currIndex % (width)) + " Val: " + str(line[currIndex % (width)]))
            if line[currIndex % (width)] == '#':
                treeCount += 1
    return treeCount

def solvePart1():
    return treeFinder(3, 1)

def solvePart2():
    return treeFinder(1, 1) * treeFinder(3, 1) * treeFinder(5, 1) * treeFinder(7, 1) * treeFinder(1, 2)


if __name__ == "__main__":
    print(solvePart1())
    print(solvePart2())