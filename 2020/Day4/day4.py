
requiredFields = ("byr", "iyr", "eyr","hgt","hcl", "ecl", "pid")

def solvePart1():
    validIdCount = 0
    with open("input.txt") as f:
        Lines = f.readlines()
        validFields = 0
        for line in Lines:
            if len(line) == 1:
                # print("HERE1: " + str(validFields))
                # process id; how many required fields
                if(validFields == 7):
                    validIdCount += 1
                # clear fields
                validFields = 0
            else:
                # parse
                Fields = line.split(' ')
                for field in Fields:
                    key, val = field.split(':')
                    # print(str(key) + " : " + val)
                    # if field is required
                    if str(key) in requiredFields:
                        # print("BING")
                        # add to count
                        validFields += 1
    print(validIdCount)

validEyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def solvePart2():
    validIdCount = 0
    with open("input.txt") as f:
        Lines = f.readlines()
        validFields = 0
        for line in Lines:
            if len(line) == 1:
                # print("HERE1: " + str(validFields))
                # process id; how many required fields
                if(validFields == 7):
                    validIdCount += 1
                # clear fields
                validFields = 0
            else:
                # parse
                Fields = line.split(' ')
                for field in Fields:
                    key, val = field.split(':')
                    key = key.strip()
                    val = val.strip()
                    # print(str(key) + " : " + val)
                    # if field is required
                    if str(key) == "byr" and int(val) >= 1920 and int(val) <= 2002:
                        # add to count
                        validFields += 1
                    elif str(key) == "iyr" and int(val) >= 2010 and int(val) <= 2020:
                        # add to count
                        validFields += 1
                    elif str(key) == "eyr" and int(val) >= 2020 and int(val) <= 2030:
                        # add to count
                        validFields += 1
                    elif str(key) == "hgt":
                        unit = val[-2:]
                        number = val[:-2]
                        if unit == "cm" and int(number) >= 150 and int(number) <= 193:
                            # add to count
                            validFields += 1
                        elif unit == "in" and int(number) >= 59 and int(number) <= 76:
                            # add to count
                            validFields += 1
                    elif str(key) == "hcl" and val[0] == '#' and len(val) == 7:
                        for ch in val[1:]:
                            if not (ch >= 'a' and ch <= 'z') and not ch.isdigit():
                                print(ch)
                                print(val)
                                continue
                        # add to count
                        validFields += 1
                    elif str(key) == "ecl" and val in validEyeColor:
                        # add to count
                        validFields += 1
                    elif str(key) == "pid" and len(val) == 9 and val.isdigit():
                        # add to count
                        validFields += 1
    print(validIdCount)


if __name__ == "__main__":
    solvePart1()
    solvePart2()

