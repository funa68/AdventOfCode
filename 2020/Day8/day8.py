def part2RunProg(instruction_dict: dict):
    visited_set = set()
    # execute instruction
    pc = 0
    accumulated_val = 0

    # loop until index is in the visited_set
    while pc < len(instruction_dict):
        if pc in visited_set:
            return None

        # print(instruction_dict[pc])
        visited_set.add(pc)

        # if acc
        if instruction_dict[pc][0] == "acc":
            # accumulated_val += val
            accumulated_val += instruction_dict[pc][1]
            pc += 1
        # elif jmp
        elif instruction_dict[pc][0] == "jmp":
            # index += val
            pc += instruction_dict[pc][1]
        # else it is noop
        else:
            # index +=1
            pc += 1
    return accumulated_val

def solvePart2():
    with open("inputPart2.txt") as f: 
        Lines = f.readlines()

        # var accumulated_val
        accumulated_val = 0
        # var set of visited_set of indexes
        visited_set = set()
        # populate dict
        instruction_dict = {}

        potential_fix_list = []

        # cycle thru all lines
        for index, line in enumerate(Lines):
            line = line.strip()
            # split on space
            first, second = line.split(' ')

            # first == instruction as string
            # second == sign and number; convert to int
            # add to dict {index: (first, second)
            instruction_dict[index] = [first, int(second)]
            if first == "nop" or first == "jmp":
                potential_fix_list.append(index)

        # print(instruction_dict)
        # print(potential_fix_list)

        for fix_index in potential_fix_list:
            # fix instruction
            if instruction_dict[fix_index][0] == "nop":
                # accumulated_val += val
                instruction_dict[fix_index][0] = "jmp"
            # elif jmp
            elif instruction_dict[fix_index][0] == "jmp":
                # accumulated_val += val
                instruction_dict[fix_index][0] = "nop"
            # print(instruction_dict)

            retVal = part2RunProg(instruction_dict)
            # print(retVal)
            # run it
            if retVal is not None:
                return retVal
            else:
                # fix instruction
                if instruction_dict[fix_index][0] == "nop":
                    # accumulated_val += val
                    instruction_dict[fix_index][0] = "jmp"
                # elif jmp
                elif instruction_dict[fix_index][0] == "jmp":
                    # accumulated_val += val
                    instruction_dict[fix_index][0] = "nop"
                # print(instruction_dict)


        return "WTF"



def solvePart1():
    with open("inputPart1.txt") as f: 
        Lines = f.readlines()

        # var accumulated_val
        accumulated_val = 0
        # var set of visited_set of indexes
        visited_set = set()
        # populate dict
        instruction_dict = {}

        # cycle thru all lines
        for index, line in enumerate(Lines):
            line = line.strip()
            # split on space
            first, second = line.split(' ')

            # first == instruction as string
            # second == sign and number; convert to int
            # add to dict {index: (first, second)
            instruction_dict[index] = (first, int(second))

        # execute instruction
        # index == 0
        pc = 0
        # loop until index is in the visited_set
        while pc not in visited_set :
            # print(instruction_dict[pc])
            visited_set.add(pc)
            # if acc
            if instruction_dict[pc][0] == "acc":
                # accumulated_val += val
                accumulated_val += instruction_dict[pc][1]
                pc += 1
            # elif jmp
            elif instruction_dict[pc][0] == "jmp":
                # index += val
                pc += instruction_dict[pc][1]
            # else it is noop
            else:
                # index +=1
                pc += 1

        return accumulated_val


if __name__ == "__main__":
    print("Part1:  " + str(solvePart1()))
    print("Part2:  " + str(solvePart2()))