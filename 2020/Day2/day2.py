
def solvePart1():
    goodPasswordCount = 0
    with open('input.txt') as f:
        Lines = f.readlines()
        for line in Lines: 
            reqt, word = line.split(':')
            word = word.strip()
            bounds, letter = reqt.split(' ')
            _min, _max = bounds.split('-')

            count = word.count(letter)
            if count >= int(_min) and count <= int(_max):
                goodPasswordCount += 1
            # print(str(letter))
            # print(str(_min))
            # print(str(_max))
    return goodPasswordCount

def solvePart2():
    goodPasswordCount = 0
    with open('input.txt') as f:
        Lines = f.readlines()
        for line in Lines: 
            reqt, word = line.split(':')
            word = word.strip()
            bounds, letter = reqt.split(' ')
            _min, _max = bounds.split('-')
            # print(_min)
            # print(_max)
            # print(word)
            if bool(word[int(_max)-1] == letter) != bool(word[int(_min)-1] == letter):
                goodPasswordCount += 1
            # print(str(letter))
            # print(str(_min))
            # print(str(_max))
    return goodPasswordCount


if __name__ == "__main__":
    print(solvePart1())
    print(solvePart2())
