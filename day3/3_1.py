import re

sum = 0

with open("day3/input.txt", "r") as file:
    scheme = ['............................................................................................................................................']
    for line in file.readlines():
        scheme.append(line)
    scheme.append('............................................................................................................................................')

    prev_line = scheme[0]
    curr_line = scheme[1]
    next_line = []

    for line in scheme[2:]:
        next_line = line
        x = re.finditer("[0-9]+", curr_line)
        for c_num in x:
            #print("-------------------------------")
            start = 0
            end = len(curr_line)

            if c_num.span()[0] > start:
                start = c_num.span()[0] - 1
            if c_num.span()[1] < end:
                end = c_num.span()[1] + 1
            #print((start,end), c_num.group())
            
            check_string = prev_line[start:end] + "11" + curr_line[start:end] + "11" + next_line[start:end]
            #print(check_string)
            y = re.search("[^0-9|.|\n]", check_string)
            if y is not None:
                #print(y)
                #print(c_num.group())
                sum += int(c_num.group())

        prev_line = curr_line
        curr_line = next_line


print(sum)


        