import random
pl1 = random.randint(1,2)
pl2 = random.randint(3,4)
pl3 = random.randint(5,6)
print("Места:")
if pl1 == 1:
    print("лес,")
else:
    print("лабиринт,")
if pl2 == 1:
    print("дом,")
else:
    print("портал,")
if pl3 == 1:
    print("лаборатория.")
else:
    print("завод.")
print("Какое место (номер)?")
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
        print("Номер неизвестен...")