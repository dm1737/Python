game = [[0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,]]


def game_board(player=0, row=0, col=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][col] = player
    for count, row in enumerate(game):
        print(count, row)

game_board()
game_board(player=1, row=2, col=0)


    