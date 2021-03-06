board = [["_","_","_"],["_","_","_"],["_","_","_"]]

turn = 'x'
winnerfound= False
i = 0

win_combos = [
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,1],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]]]

x=0
y=0

def check_win():
    for combo in win_combos:
        if board[combo[0][0]][combo[0][1]]==board[combo[1][0]][combo[1][1]] and board[combo[0][0]][combo[0][1]]==board[combo[2][0]][combo[2][1]]:
            if board[combo[0][0]][combo[0][1]]=="x" or board[combo[0][0]][combo[0][1]]=="o":
                return True
                break
    return False

def play_turn(turn):
    print(f"Player {turn}\n ==========")   
    x,y =  input("row column\n").split(' ')
    if int(x)>2 or int(y)>2:
        print('Please ensure that you are playing within the board')
        x,y = play_turn(turn)
    return x,y

def place_piece(x,y,turn):
    board[int(x)][int(y)]=turn


while not winnerfound and i<8:
    x,y = play_turn(turn)

    place_piece(x,y,turn)

    for arr in board:
        print(arr)
    
    winnerfound = check_win()
    print(winnerfound)
    if winnerfound:
        print("Congratulations {turn}!!! you are the winner")
    i+=1

    turn = 'o' if turn == 'x' else 'x'
if not winnerfound:
    "Well done you two!!! Match was a draw"