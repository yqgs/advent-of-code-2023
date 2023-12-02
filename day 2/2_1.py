import re

sum = 0

with open("day 2/input.txt", "r") as file:
    counter = 0
    for line in file:
        counter += 1
        illegal = False
        game = re.sub("Game\s[0-9]*:|\n|\s", "", line)
        game = re.sub("blue", "b", game)
        game = re.sub("red", "r", game)
        game = re.sub("green","g", game)
        game = re.split(";", game)
        # print(game)
        for run in game:
            run = re.split(",", run)
            # print(run)
            for ball in run:
                if ball[-1] == 'b' and int(ball[0:-1]) > 14:
                    illegal = True
                    break
                if ball[-1] == 'g' and int(ball[0:-1]) > 13:
                    illegal = True
                    break
                if ball[-1] == 'r' and int(ball[0:-1]) > 12:
                    illegal = True
                    break
            if illegal == True:
                break
        if illegal == False:
            # print(counter)
            sum += counter
        

print(sum)