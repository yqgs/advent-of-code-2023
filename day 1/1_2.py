import re


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight" : 8,
    "nine" : 9
}

reversed_numbers = {
    "eno" : 1,
    "owt" : 2,
    "eerht" : 3,
    "ruof" : 4,
    "evif" : 5,
    "xis" : 6,
    "neves" : 7,
    "thgie" : 8,
    "enin" : 9
}

sum = 0

with open("day 1/input1_1.txt", "r") as file:
    for line in file:
        num = 0
        nums = re.findall("one|two|three|four|five|six|seven|eight|nine|[0-9]", line)
        
        if nums[0].isdigit():
            num += int(nums[0])
        else:
            num += numbers[nums[0]]
        
        num *= 10
        
        rev = line[::-1]

        nums = re.findall("eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9]", rev)

        if nums[0].isdigit():
            num += int(nums[0])
        else:
            num += reversed_numbers[nums[0]]
        
        sum += num

print(sum)



