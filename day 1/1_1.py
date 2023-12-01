sum = 0

with open("day 1/input1_1.txt", "r") as file:
    for line in file:
        num = 0
        for char in line:
            if char.isdigit():
                num += int(char)
                break
        num *= 10
        rev = reversed(line)
        for char in rev:
            if char.isdigit():
                num += int(char)
                break
        sum += num

print(sum)