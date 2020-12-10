
def solvePart2():
    total = 0
    with open("input.txt") as f:
        Lines = f.readlines()
        num_people = 0
        num_questions = 0
        letter_count_list = [0] * 26

        for line in Lines:
            line = line.strip()
            # print("Line Length: " + str(len(line)))
            if len(line) >= 1:
                num_people += 1
                for ch in line:
                    # print("-----")
                    # print(ch)
                    # print('a')
                    # print(ord(ch) - ord('a'))
                    letter_count_list[ord(ch) - ord('a')] += 1
            else:
                # print("BING")
                # if any letter has count == num_people
                print("NumPeeps: " + str(num_people))
                print(letter_count_list)
                for val in letter_count_list:
                    if val == num_people:
                        num_questions += 1
                print("NumQs: " + str(num_questions))

                num_people = 0
                letter_count_list  = [0] * 26

    print("NumPeeps: " + str(num_people))
    print(letter_count_list)
    for val in letter_count_list:
        if val == num_people:
            num_questions += 1
    print("NumQs: " + str(num_questions))


    return num_questions

def solvePart1():
    total = 0
    with open("input.txt") as f:
        Lines = f.readlines()
        letter_set = set()
        num_groups = 0
        # read file line by line
        for line in Lines:
            line = line.strip() # remove newline char
            # print(len(line))
            if len(line):
                # print("BING")
                # read each char and add to a set
                for ch in line:
                    letter_set.add(ch)
            else:
                # print("BOO")
                # on new line breaks tally unique chars and add to total
                # clear set
                total += len(letter_set)
                num_groups += 1
                # print(len(letter_set))
                letter_set.clear()

        total += len(letter_set)

    print("Groups:" + str(num_groups))
    return total

if __name__ == "__main__":
    print(solvePart1())
    print(solvePart2())