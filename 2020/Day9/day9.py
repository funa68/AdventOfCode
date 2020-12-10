def helper1(preamble_list: list, target: int):
    for index, num1 in enumerate(preamble_list):
        for num2 in preamble_list[index:]:
            if num1 + num2 == target:
                return True
    return False


def solvePart1():
    retVal = None
    bad_num = None
    with open("inputPart1.txt") as f: 
        Lines = f.readlines()

        preamble_list = []
        for index, line in enumerate(Lines):
            line = line.strip()
            
            if len(preamble_list) < 25:
                preamble_list.append(int(line))
            else:
                # print(str(preamble_list))
                # print("NUM: " + str(line))

                currNum = int(line)
                if helper1(preamble_list, currNum):
                    preamble_list.pop(0)
                    preamble_list.append(currNum)
                    continue
                else:
                    return currNum
    return retVal

def helper2():
    for index, num1 in enumerate(preamble_list):
        for num2 in preamble_list[index:]:
            if num1 + num2 == target:
                return True
    return False


# Part 1 Answer: 466456641
def solvePart2():
    retVal = None
    num_list = []
    with open("inputPart1.txt") as f: 
        Lines = f.readlines()

        for index, line in enumerate(Lines):
            line = line.strip()
            num_list.append(int(line))

    target = 466456641
    startIndex = 0
    endIndex = 1
    while(endIndex < len(num_list)):
        curr_sum = sum(num_list[startIndex:endIndex+1])
        if curr_sum > target:
            startIndex += 1
        elif curr_sum < target:
            endIndex += 1
        else:
            # equal!
            return min(num_list[startIndex:endIndex+1]) + max(num_list[startIndex:endIndex+1])

    return retVal

if __name__ == "__main__":
    print("Part1:  " + str(solvePart1()))
    print("Part2:  " + str(solvePart2()))