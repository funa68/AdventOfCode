
def helper2():
    retVal = 0
    return retVal

def solvePart2():
    retVal = 0
    with open("inputPart2.txt") as f: 
        Lines = f.readlines()

        for index, line in enumerate(Lines):
            line = line.strip()
            first, second = line.split(' ')
    return retVal


def helper1():
    retVal = 0
    return retVal


def solvePart1():
    retVal = 0
    with open("inputPart1.txt") as f: 
        Lines = f.readlines()

        for index, line in enumerate(Lines):
            line = line.strip()
            
            first, second = line.split(' ')

            helper1()


    return retVal

if __name__ == "__main__":
    print("Part1:  " + str(solvePart1()))
    print("Part2:  " + str(solvePart2()))