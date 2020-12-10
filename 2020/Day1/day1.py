class Solution:
    inputList = []

    def __init__(self):
        self.readInput()

    def readInput(self):
        self.inputList = []

        with open('input.txt') as f:
            line = f.readline()
            while(line):
                self.inputList.append(int(line))
                line = f.readline()
        # print(self.inputList)

    def solvePart1(self, target: int):
        self.inputList.sort()
        # print(self.inputList)

        for startIndex, num in enumerate(self.inputList):
            for i in range(startIndex+1, len(self.inputList)-1):
                # print(str(num) + " + " + str(self.inputList[i]) + " = " + str(num + self.inputList[i]))
                if num + self.inputList[i] > target:
                    break
                if num + self.inputList[i] == target:
                    return num * self.inputList[i]
        return 0

    def solvePart2(self, target: int):
        self.inputList.sort()
        # print(self.inputList)

        for startIndex, num in enumerate(self.inputList):
            for startIndex2 in range(startIndex+1, len(self.inputList)-1):
                for startIndex3 in range(startIndex2+1, len(self.inputList)-1):
                    # print(str(num) + " + " + str(self.inputList[i]) + " = " + str(num + self.inputList[i]))
                    if num + self.inputList[startIndex2] + self.inputList[startIndex3] > target:
                        break
                    if num + self.inputList[startIndex2] + self.inputList[startIndex3] == target:
                        return num * self.inputList[startIndex2] * self.inputList[startIndex3]
        return 0
if __name__ == "__main__":
    steven = Solution()
    print(steven.solvePart1(2020))
    print(steven.solvePart2(2020))
