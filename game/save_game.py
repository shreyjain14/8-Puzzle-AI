def save_to_file():
    file = open("game/saved_game.txt", "w")
    game = input("Enter Game: ")
    game_list = game.split(" ")
    game_list_add = []
    for i in game_list:
        game_list_add.append(i + "\n")
    file.writelines(game_list_add)
    file.close()
