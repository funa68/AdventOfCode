
def dfs(bag_lookup: dict, currBag: str, target: str, visited_set: set, valid_bag_set: set):
    # print("visited_set: " + str(visited_set))

    if currBag not in visited_set:
        # print("Visiting: " + currBag)
        temp_visited_set = visited_set.copy()
        temp_visited_set.add(currBag)

        for bag in bag_lookup[currBag]:
            if bag == target:
                for v_bag in temp_visited_set:
                    valid_bag_set.add(v_bag)
                # print("temp_visited_set: " + str(temp_visited_set))
                # print("VVV valid_bag_set: " + str(valid_bag_set))

            elif bag not in temp_visited_set:
                dfs(bag_lookup, bag, target, temp_visited_set, valid_bag_set)
    # else:
        # print("Already Visited: " + currBag)
    # print("valid_bag_set: " + str(valid_bag_set))

def solvePart1():
    bag_lookup = {}
    with open("input.txt") as f:
        Lines = f.readlines()
        
        for line in Lines:
            line = line.strip()
            key, val = line.split(" bags contain ")

            if(val[0:2] == "no"):
                bag_lookup[key] = []
            else:
                bag_list = val.split(", ")
                # print(bag_list)
                bag_list = [bag[2:].split(" bag")[0] for bag in bag_list]
                # print(bag_list)
                bag_lookup[key] = bag_list

        # print(bag_lookup)

    # do dfs for each bag
    visited_set = set()
    valid_bag_set = set()
    for bag in bag_lookup.keys():
        # print("Start bag: " + str(bag))
        dfs(bag_lookup, bag, "shiny gold", visited_set, valid_bag_set)

    return len(valid_bag_set)

def dfsPart2(bag_lookup: dict, target: str):
    total = 0

    print("BING: " + str(bag_lookup[target]))
    if len(bag_lookup[target]) == 0:
        print("total: "  + str(1))
        return 0

    for bag_name, amount in bag_lookup[target].items():
        total += dfsPart2(bag_lookup, bag_name) * int(amount)
        total += int(amount)
        print("total: "  + str(total))

    return total

def solvePart2():
    bag_lookup = {}
    with open("input.txt") as f:
        Lines = f.readlines()
        
        # populate bag lookup
        for line in Lines:
            line = line.strip()
            key, val = line.split(" bags contain ")
            bag_lookup[key] = {}
            if(val[0:2] == "no"):
                continue
            else:
                bag_list = val.split(", ")
                # descrip: number
                for bag in bag_list:
                    btype = bag[2:].split(" bag")[0]
                    amount = bag[0].split(" bag")[0]
                    bag_lookup[key][btype] = amount

        print(bag_lookup)

    return dfsPart2(bag_lookup, "shiny gold")

if __name__ == "__main__":
    print("Part1: " + str(solvePart1()))
    print("Part2: " + str(solvePart2()))