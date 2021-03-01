from game2dboard import Board
import numpy as np


board_size=5

b=np.zeros((board_size,board_size))

def init(b):
    b[0,1]=1
    b[0,3]=1
    b[1,2]=2
    b[4,1]=2
    b[4,3]=2
    b[3,2]=1


#Checks legal moves
def legal(board, size, coord, direction):
    init_coord = np.array(coord)
    empty = True
    new_pos= np.array(coord)
    
    if direction == 1: #UP
        while empty == True:
            if new_pos[0]!=0 and board[new_pos[0]-1,new_pos[1]] == 0:
                new_pos[0] = new_pos[0]-1 #não é preciso mudar a coluna
            else:
                empty = False   
    elif direction == 2: #Down
        
        while empty == True:
            if new_pos[0]!= size-1 and board[new_pos[0]+1,new_pos[1]] == 0:
                    new_pos[0] = new_pos[0]+1
            else:
                empty = False   
    elif direction == 3: #Right
        
        while empty == True:
            if new_pos[1]!= size-1 and board[new_pos[0],new_pos[1]+1] == 0:
                    new_pos[1] = new_pos[1]+1
            else:
                empty = False
    elif direction == 4: #Left
        while empty == True:
            if new_pos[1]!=0 and board[new_pos[0],new_pos[1]-1] == 0:
                new_pos[1] = new_pos[1]-1 #não é preciso mudar a coluna
            else:
                empty = False     
    elif direction == 5: #Up right
        
        while empty == True:
            if (new_pos[0]!= 0 and new_pos[1]!= size-1) and board[new_pos[0]-1,new_pos[1]+1] == 0:
                    new_pos[0] = new_pos[0]-1
                    new_pos[1] = new_pos[1]+1
            else:
                empty = False
    elif direction == 6: #Up left
        
        while empty == True:
            if (new_pos[0]!= 0 and new_pos[1]!= 0) and board[new_pos[0]-1,new_pos[1]-1] == 0:
                    new_pos[0] = new_pos[0]-1
                    new_pos[1] = new_pos[1]-1
            else:
                empty = False
    elif direction == 7: #Down right
        
        while empty == True:
            if (new_pos[0]!= size-1 and new_pos[1]!= size-1) and board[new_pos[0]+1,new_pos[1]+1] == 0:
                    new_pos[0] = new_pos[0]+1
                    new_pos[1] = new_pos[1]+1
            else:
                empty = False
    elif direction == 8: #Down left
        
        while empty == True:
            if (new_pos[0]!= size-1 and new_pos[1]!= 0) and board[new_pos[0]+1,new_pos[1]-1] == 0:
                    new_pos[0] = new_pos[0]+1
                    new_pos[1] = new_pos[1]-1
            else:
                empty = False
         
        
        
    if np.array_equal(new_pos,init_coord):
        print("Move not possible")
        return False
    else:
        return new_pos

def move_piece(board, init_coord, final_coord ):
    board[final_coord[0],final_coord[1]] = board[init_coord[0],init_coord[1]]
    board[init_coord[0],init_coord[1]]=0




def start_game(size):
    global bo 
    bo = Board(size, size)       
    bo[0][1] = 1
    bo[0][3] = 1
    bo[3][2] = 1
    bo[1][2] = 2
    bo[4][1] = 2
    bo[4][3] = 2
    bo.title = "Neutreeko"
    bo.cell_size = 120       
    bo.cell_color = "LightGreen"
    bo.margin = 25
    bo._margin_color = "MediumSeaGreen"


start_game(5)


def select_piece(btn,row,col):
    for dir in range(1,9):
        legal_coord = legal(b,5,[row,col],dir) #resolver a questão do size
        bo[row][col] = 3

bo.on_mouse_click = select_piece

def select_move(btn,row, col):
    move_piece(b, init_coord,[row,col] )
    bo[row][col] = 1 #ou 2
    bo[init_coord[0]][init_coord[1]]= 0 



bo.show()