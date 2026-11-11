import random
pl1 = random.randint(1,2)
pl2 = random.randint(3,4)
pl3 = random.randint(5,6)
print("Places:")
if pl1 == 1:
    print("forest,")
else:
    print("maze,")
if pl2 == 1:
    print("house,")
else:
    print("portal,")
if pl3 == 1:
    print("laboratory.")
else:
    print("factory.")
print("What place (number)?")
plplayer = int(input())
match plplayer:
    case 1:
        if pl1 == 1:
            plplayer = "forest"
        else:
            plplayer = "maze"
    case 2:
        if pl2 == 3:
            plplayer = "house"
        else:
            plplayer = "portal"
    case 3:
        if pl3 == 5:
            plplayer = "laboratory"
        else:
            plplayer = "factory"
    case _:
        print("Unknown place number...")