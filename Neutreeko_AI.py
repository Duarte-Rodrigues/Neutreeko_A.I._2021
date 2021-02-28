# Neutreeko - This project was developed by Duarte Rodrigues and Jacinta Ferreira for IA_MECD course.

import numpy as np

size=5

b=np.zeros((size,size))

def init(b):
    b[0,1]=1
    b[0,3]=1
    b[1,2]=2
    b[4,1]=2
    b[4,3]=2
    b[3,2]=1
    
init(b)
blah=(1,2)
print(b[blah[0],blah[1]])


#Checks legal moves
def legal(board, coord, direction):
    init_coord = np.array(coord)
    empty = True
    new_pos= np.array(coord)
    
    if direction == 1: #UP
        while empty == True:
            if new_pos[0]!=0 and board[new_pos[0]-1,new_pos[1]] == 0:
                new_pos[0] = new_pos[0]-1 #não é preciso mudar a coluna
            else:
                empty = False         
    elif direction == 5: #Up right
        
        while empty == True:
            if new_pos[0]!= 0 and new_pos[1]!= size-1:
                if  board[new_pos[0]-1,new_pos[1]+1] == 0:
                    new_pos[0] = new_pos[0]-1
                    new_pos[1] = new_pos[1]+1
            else:
                empty = False
                
        
        
    if np.array_equal(new_pos,init_coord):
        print("Move not possible")
    else:
        return new_pos

def move_piece(board, init_coord, final_coord ):
    board[final_coord[0],final_coord[1]] = board[init_coord[0],init_coord[1]]
    board[init_coord[0],init_coord[1]]=0


#It is necessary to define the piece coordinates as an array
coord = [3,2]
print(b) 
move_piece(b, coord, legal(b, coord, 5))

print(b) 

#Heuristica

pieces