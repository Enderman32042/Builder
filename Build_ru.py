from Scripts.ru_ver.Location_ru import plplayer
print("Что вы хотите построить?")
if plplayer == "forest":
    print("Лабиринт, дом, портал, лаборатория или завод (номер)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("Это - ЛАБИРИНТ!!!")
        case 2:
            print("Это - ДОМ!!!")
        case 3:
            print("Это - ПОРТАЛ!!!")
        case 4:
            print("Это - ЛАБОРАТОРИЯ!!!")
        case 5:
            print("Это - ЗАВОД!!!")
        case _:
            print("Ничего...")
elif plplayer == "maze":
    print("Лес, дом, портал, лаборатория или завод (номер)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("Это - ЛЕС!!!")
        case 2:
            print("Это - ДОМ!!!")
        case 3:
            print("Это - ПОРТАЛ!!!")
        case 4:
            print("Это - ЛАБОРАТОРИЯ!!!")
        case 5:
            print("Это - ЗАВОД!!!")
        case _:
            print("Ничего...")
elif plplayer == "house":
    print("Лес, лабиринт, портал, лаборатория или завод (номер)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("Это - ЛЕС!!!")
        case 2:
            print("Это - ЛАБИРИНТ!!!")
        case 3:
            print("Это - ПОРТАЛ!!!")
        case 4:
            print("Это - ЛАБОРАТОРИЯ!!!")
        case 5:
            print("Это - ЗАВОД!!!")
        case _:
            print("Ничего...")
elif plplayer == "portal":
    print("Лес, лабиринт, дом, лаборатория или завод (номер)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("Это - ЛЕС!!!")
        case 2:
            print("Это - ЛАБИРИНТ!!!")
        case 3:
            print("Это - ДОМ!!!")
        case 4:
            print("Это - ЛАБОРАТОРИЯ!!!")
        case 5:
            print("Это - ЗАВОД!!!")
        case _:
            print("Ничего...")
elif plplayer == "laboratory":
    print("Лес, лабиринт, дом, портал или завод (номер)?")
    newpl = int(input())
    match newpl:
        case 1:
            print("Это - ЛЕС!!!")
        case 2:
            print("Это - ЛАБИРИНТ!!!")
        case 3:
            print("Это - ДОМ!!!")
        case 4:
            print("Это - ПОРТАЛ!!!")
        case 5:
            print("Это - ЗАВОД!!!")
        case _:
            print("Ничего...")
elif plplayer == "factory":
    print("Лес, лабиринт, дом, портал или лаборатория (номер)?")
    newpl = int(input())
    match newpl:
            case 1:
             print("Это - ЛЕС!!!")
            case 2:
             print("Это - ЛАБИРИНТ!!!")
            case 3:
             print("Это - ДОМ!!!")
            case 4:
             print("Это - ПОРТАЛ!!!")
            case 5:
             print("Это - ЛАБОРАТОРИЯ!!!")
            case _:
             print("Ничего...")
else:
    print("Ничего...")
print("Окончание игры...")