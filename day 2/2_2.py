import re

sum = 0

with open("day 2/input.txt", "r") as file:
    for line in file:
        min_r, min_b, min_g = 0, 0, 0
        game = re.sub("Game\s[0-9]*:|\n|\s", "", line)
        game = re.sub("blue", "b", game)
        game = re.sub("red", "r", game)
        game = re.sub("green","g", game)
        game = re.split(";", game)
        # print(game)
        # print("-----------------------------------------------------")
        for run in game:
            run = re.split(",", run)
            # print(run)
            for ball in run:
                if ball[-1] == 'r':
                    min_r = max(int(ball[0:-1]), min_r)
                if ball[-1] == 'g':
                    min_g = max(int(ball[0:-1]), min_g)
                if ball[-1] == 'b':
                    min_b = max(int(ball[0:-1]), min_b)

        # print([min_r,min_g,min_b])
        # print("\n")

        sum += min_r * min_g * min_b

print(sum)