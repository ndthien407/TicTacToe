def print_board(board):
    board_format =" "

    for i in range(0, len(board)):
        if i % 3 == 0:
            board_format = board_format + "\n"
        board_format = board_format + board[i] +"|"
    print(board_format)
def row(board, start, mark):
    return board[start] == board[start + 1] and board[start +1] == board[start +2] and board[start +2] == mark

def column(board, start, mark):
    return board[start] == board[start + 3] and board[start +3] == board[start +6] and board[start +6] == mark
    
def diagonal_1(board, start, mark):
    return board[start] == board[start + 4] and board[start +4] == board[start +8] and board[start +8] == mark

def diagonal_2(board, start, mark):
    return board[start] == board[start + 2] and board[start +2] == board[start +4] and board[start +4] == mark

def is_draw(board):
    for i in range(0, len(board)):
        if board[i] != "O" and board[i] != "X":
            return False
    return True
            
def game_continue(board):
    for mark in ["O","X"]:
        if row(board, 0,mark) or row(board, 3,mark) or row(board, 6,mark):
            return False
        if column(board, 0, mark) or column(board, 1, mark) or column(board, 2, mark):
            return False
        if diagonal_1 (board, 0, mark):
            
            return False
        if diagonal_2 (board, 2, mark):
            return False 

    
    return not is_draw(board) # return True
if __name__ == "__main__" :
    
    #tạo 2 người chơi, tại dòng 
    
    print("Welcome to Tic Tac Toe")
    print("Choose player, type X or O \nChoose X if you want go first")
    """Get Player """
    
    while True:
        player_1= input().upper()
        if player_1 == "X":
            player_2 = "O"
            current_player = player_1
            break
        elif player_1== "O":
            player_2 = "X"
            current_player = player_2
            break
        else:
            print("Please Choose Again !!!")
            continue
                    
    print("Player 1 : ", player_1)
    print("Player 2 : ", player_2)
    
    #Hiển thị board lên màn hình
    board = [" "] *9
              
    #tạo số hiển thị trên board
              
    for i in range(0, len(board)):
        board[i] = str(i+1)
        
    print_board(board)
    
    print("\nType from 1-9 to mark your move\n")

    print_board(board)
    
    while game_continue(board):
        
        print("Player",current_player,"turn :")
        try : 
            move = int(input())
        except Exception as e:

            print("Choose 1 - 9 for each turn")

            print_board(board)            
            continue
        
        if board[move - 1] == "O" or board[move -1] == "X":

            print("Your place had been chosen")
            print("Pls , choose again !")

            print_board(board)

            continue
        
        if move >=1 and move <= 9 :
            board[move - 1] = current_player
        
        else:
            print("Eror, Try Again!!")
            print_board(board)
            continue
            
        # hien thi bảng để add số vào vị trí :
        
        print_board(board)
        
        if not game_continue(board):
            break
        
        #luân phiên 2 ng chơi
        if current_player == player_1:
            current_player = player_2
        elif current_player == player_2:
            current_player = player_1

        #trường hợp - thắng/thua/hòa -
    if is_draw(board):
        print("\nDRAW")
    else:
        print("\nWinner is : ",current_player)

    
    
























