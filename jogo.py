from game2dboard import Board
import numpy as np



#Checks legal moves
def legal(board, size, coord, direction):
    init_coord = np.asarray(coord)
    empty = True
    new_pos= np.asarray(coord)
    
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
    global b 
    b = Board(size, size)       
    b[0][1] = 1
    b[0][3] = 1
    b[3][2] = 1
    b[1][2] = 2
    b[4][1] = 2
    b[4][3] = 2
    b.title = "Neutreeko"
    b.cell_size = 120       
    b.cell_color = "LightGreen"
    b.margin = 25
    b._margin_color = "MediumSeaGreen"


start_game(5)


def select_piece(btn,row,col):
    for dir in range(1,9):
        legal_coord = legal(b,5,[row,col],dir) #resolver a questão do size
        b[row][col] = 3

b.on_mouse_click = select_piece

#def select_move(btn,row, col):
#   move_piece(b, init_coord,[row,col] )




b.show()