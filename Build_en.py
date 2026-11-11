from Scripts.en_ver.Location_en import plplayer
print("What do you want to build?")
if plplayer == "forest":
    print("Maze, house, portal, laboratory or factory (numbers)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("This is MAZE!!!")
        case 2:
            print("This is HOUSE!!!")
        case 3:
            print("This is PORTAL!!!")
        case 4:
            print("This is LABORATORY!!!")
        case 5:
            print("This is FACTORY!!!")
        case _:
            print("Nothing...")
elif plplayer == "maze":
    print("Forest, house, portal, laboratory or factory (numbers)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("This is FOREST!!!")
        case 2:
            print("This is HOUSE!!!")
        case 3:
            print("This is PORTAL!!!")
        case 4:
            print("This is LABORATORY!!!")
        case 5:
            print("This is FACTORY!!!")
        case _:
            print("Nothing...")
elif plplayer == "house":
    print("Forest, maze, portal, laboratory or factory (numbers)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("This is FOREST!!!")
        case 2:
            print("This is MAZE!!!")
        case 3:
            print("This is PORTAL!!!")
        case 4:
            print("This is LABORATORY!!!")
        case 5:
            print("This is FACTORY!!!")
        case _:
            print("Nothing...")
elif plplayer == "portal":
    print("Forest, maze, house, laboratory or factory (numbers)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("This is FOREST!!!")
        case 2:
            print("This is MAZE!!!")
        case 3:
            print("This is HOUSE!!!")
        case 4:
            print("This is LABORATORY!!!")
        case 5:
            print("This is FACTORY!!!")
        case _:
            print("Nothing...")
elif plplayer == "laboratory":
    print("Forest, maze, house, portal or factory (numbers)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("This is FOREST!!!")
        case 2:
            print("This is MAZE!!!")
        case 3:
            print("This is HOUSE!!!")
        case 4:
            print("This is PORTAL!!!")
        case 5:
            print("This is FACTORY!!!")
        case _:
            print("Nothing...")
elif plplayer == "factory":
    print("Forest, maze, house, portal or laboratory (numbers)?")
    newpl = int(input())
    match newpl:
            case 1:
             print("This is FOREST!!!")
            case 2:
             print("This is MAZE!!!")
            case 3:
             print("This is HOUSE!!!")
            case 4:
             print("This is PORTAL!!!")
            case 5:
             print("This is LABORATORY!!!")
            case _:
             print("Nothing...")
else:
    print("Nothing...")
print("Ending game...")