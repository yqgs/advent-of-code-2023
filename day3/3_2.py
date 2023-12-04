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
        x = re.finditer("[^0-9|.|\n]", curr_line)
        for c_num in x:
            print("-------------------------------")
            start = 0
            end = len(curr_line)

            if c_num.span()[0] > start:
                start = c_num.span()[0] - 1
            if c_num.span()[1] < end:
                end = c_num.span()[1] + 1
            print((start,end), c_num.group(), c_num.span()[0])
            
            check_string = prev_line[start:end] + "||" + curr_line[start:end] + "||" + next_line[start:end]
            print(check_string)
            y = re.findall("[0-9]+", check_string)
            if len(y) == 2:
                print(y)
                prod = 1
                z = re.finditer("[0-9]+", check_string)
                for n in z:
                    if n.span()[0] < 5:
                        p = re.finditer("[0-9]+", prev_line)
                        for m in p:
                            if m.span()[0] <= (c_num.span()[0] - 1 + (n.span()[0]%5)) and (c_num.span()[0] - 1 + (n.span()[0]%5)) <= m.span()[1]:
                                prod *= int(m.group())
                                print(m.group())
                    elif n.span()[0] < 10:
                        p = re.finditer("[0-9]+", curr_line)
                        for m in p:
                            if m.span()[0] <= (c_num.span()[0] - 1 + (n.span()[0]%5)) and (c_num.span()[0] - 1 + (n.span()[0]%5)) <= m.span()[1]:
                                prod *= int(m.group())
                                print(m.group())
                    else:
                        p = re.finditer("[0-9]+", next_line)
                        for m in p:
                            if m.span()[0] <= (c_num.span()[0] - 1 + (n.span()[0]%5)) and (c_num.span()[0] - 1 + (n.span()[0]%5)) <= m.span()[1]:
                                prod *= int(m.group())
                                print(m.group())
                sum += prod

        prev_line = curr_line
        curr_line = next_line


print(sum)


        