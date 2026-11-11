print("Please, set English or Russian language.")
lan = input()
match lan:
    case "English":
        print("Good!")
        import Scripts.en_ver.Structure_game_en
    case "Russian":
        print("Good!")
        import Scripts.ru_ver.Structure_game_ru
    case _:
        print("Sorry, I can't it.")