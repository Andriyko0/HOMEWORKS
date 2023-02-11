GameList = [{"name":"HOI4","category":'strategi',"comentar":"Good game" }

            ]
game = {"name":None,"category":None,"comentar":None }
while True:
    print("""функціонал:
     додати гру з описом і з категорією = add game
     вивести інформацію по назві гри = Google_On
     вивести усі ігри = show all game
     вивести усі ігри по категорії = show category
     видалити гру = del
     змінити категорію для гри = corect category
     зміними опис для гри = corect category""")
    chose = input('Infut funkshen ')
    if chose == "add game":
        game["name"] = input("Input name ")
        game["category"] = input("Input category ")
        game["comentar"] = input("Input comentr")
        GameList.append(game)
        print(GameList)
    elif chose == "Google_On":
        name = input("Input name ")
        Zminna = 0
        for contact in GameList:
            if contact["name"] == name:
                print(f"{contact['name']},{contact['category']},{contact['comentar']}")
                Zminna += 1
            else: print("I dont Know this game :(")
    elif chose == "show all game":
        Zminna2 = 0
        for contact in GameList:
                print(f"{contact['name']}")
                Zminna2 += 1
    elif chose == "show category":
        category = input("Input category ")
        Zminna3 = 0
        for contact in GameList:
            if contact["category"] == category:
                print(f"{contact['name']}")
                Zminna3 += 1
            else:print("None game")
    elif chose == "del":
        name = input("Input name ")
        Zminna4 = 0
        for contact in GameList:
            game1 = GameList[Zminna4]
            if contact["name"] == name:
                game1["name"] = None
                game1["category"] = None
                game1["comentar"] = None
                Zminna4 += 1
            else:print("None game")
    elif chose == "corect category":
        name = input("Input name ")
        Zminna5 = 0
        for contact in GameList:
            game1 = GameList[Zminna5]
            if contact["name"] == name:
                game1["category"] = input("input new category ")
                Zminna5 += 1
            else: print("I dont Know this game :(")
    elif chose == "corect comentar":
        name = input("Input name ")
        Zminna6 = 0
        for contact in GameList:
            game1 = GameList[Zminna6]
            if contact["name"] == name:
                game1["comentar"] = input("input new comentar ")
                Zminna6 += 1
            else: print("I dont Know this game :(")

