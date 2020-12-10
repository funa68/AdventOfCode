from math import floor

def solvePart2():
    # track all seats
    seatList = []

    #open file and read line by line
    with open("input.txt") as f:
        Lines = f.readlines()

        for line in Lines:
            line = line.strip()
            # pass first 7 chars to findRow
            row = findBinSearchResult(line[:7], 0, 0,127)
            # pass last 3 chars to findCol
            col = findBinSearchResult(line[7:], 0, 0,7)
            # calculate seat id row * 8 + col
            seat_id = row * 8 + col
            # print("Seat Id: " + str(seat_id))
            seatList.append(seat_id)

    seatList.sort()
    # print(seatList)

    for i, seat in enumerate(seatList):
        if seat + 1 != seatList[i+1]:
            return seat+1

    return 0


def solvePart1():
    # track max seat Id
    max_seat_id = 0

    #open file and read line by line
    with open("input.txt") as f:
        Lines = f.readlines()

        for line in Lines:
            line = line.strip()
            # pass first 7 chars to findRow
            row = findBinSearchResult(line[:7], 0, 0,127)
            # pass last 3 chars to findCol
            col = findBinSearchResult(line[7:], 0, 0,7)
            # calculate seat id row * 8 + col
            seat_id = row * 8 + col
            # print("Seat Id: " + str(seat_id))
            # if highest seat id replace max seatIt
            if seat_id > max_seat_id :
                max_seat_id = seat_id

    return max_seat_id


def findBinSearchResult(line: str, inputIndex: int, leftVal: int, rightVal: int):
    # look at each char and search thru start and end recursively

    # calc midVal, floor to behave like 'int'
    midVal = floor((rightVal + leftVal)/2)
    retVal = 0

    if(line[inputIndex] == 'F' or line[inputIndex] == 'L'):
        # if char is F
            # search left floor(midVal)
        if(rightVal-leftVal > 1):
            retVal = findBinSearchResult(line, inputIndex+1, leftVal, midVal)
        else:
            retVal = leftVal

    elif(line[inputIndex] == 'B' or line[inputIndex] == 'R'):
        # if char is B
            # search right floor(midVal)+1
        if(rightVal-leftVal > 1):
            retVal = findBinSearchResult(line, inputIndex+1, midVal+1, rightVal)
        else:
            retVal = rightVal
    return retVal

if __name__ == "__main__":
    print(solvePart1())
    print(solvePart2())