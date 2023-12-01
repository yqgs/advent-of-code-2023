import re

sum = 0

with open("day 1/input1_1.txt", "r") as file:
    for line in file:
        x = re.findall("[0-9]", line)
        sum += (int(x[0]) * 10) + int(x[-1])


print(sum)