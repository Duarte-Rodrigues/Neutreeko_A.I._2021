# Neutreeko - This project was developed by Duarte Rodrigues and Jacinta Ferreira for IA_MECD course.

import numpy as np
import copy 
size=5

b=np.zeros((size,size))

def inic(b):
    b[0,2]=2
    b[3,4]=2
    b[4,4]=2
    b[0,4]=1
    b[1,0]=1
    b[4,2]=1

def init(b):
    b[0,1]=1
    b[0,3]=1
    b[3,2]=1
    b[1,2]=2
    b[4,1]=2
    b[4,3]=2
    # pieces_loc=np.array([[0,1],[0,3],[3,2],[1,2],[4,1],[4,3]])
    # return pieces_loc

# init(b)
inic(b)
#Sets an array with the position of the pieces [1 1 1 2 2 2]
def locationOfPieces(board):
    pieces_loc=np.array([[0,0]])
    for i in range(size):
        for j in range(size):
            pos=[i,j]
            if board[i,j] == 1:
                pieces_loc = np.insert(pieces_loc, 0, pos, axis=0)
            elif board[i,j] == 2:
                pieces_loc = np.insert(pieces_loc, pieces_loc.shape[0]-1, pos, axis=0)
    
    pieces_loc=np.delete(pieces_loc,-1, 0)
    return pieces_loc

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
        return init_coord
    else:
        return new_pos

def move_piece(board, init_coord, final_coord ):
    if not np.array_equal(final_coord,init_coord):
        board[final_coord[0],final_coord[1]] = board[init_coord[0],init_coord[1]]
        board[init_coord[0],init_coord[1]]=0


#It is necessary to define the piece coordinates as an array
# coord = [1,2]
# print(b)

# move_piece(b, coord, legal(b, coord, 8))

# print(b) 

#Heuristics

def findPiece(board, coord, player, pieceNextTo):

    new_pos = coord[:]
    direction = 0
    empty = True
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=1
            return new_pos,direction
        elif new_pos[0]!=0 and board[new_pos[0],new_pos[1]] == 0: 
            new_pos[0] = new_pos[0]-1
        else:
            empty=False
            print('not found up')
    
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=2
            return new_pos,direction
        elif new_pos[0]!= size-1 and board[new_pos[0],new_pos[1]] == 0: 
            new_pos[0] = new_pos[0]+1
        else:
            empty=False
            print('not found down')
            
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=3
            return new_pos,direction
        elif new_pos[1]!= size-1 and board[new_pos[0],new_pos[1]] == 0:
            new_pos[1] = new_pos[1]+1
        else:
            empty=False
            print('not found right')
            
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=4
            return new_pos,direction
        elif new_pos[1]!=0 and board[new_pos[0],new_pos[1]] == 0:
            new_pos[1] = new_pos[1]-1
        else:
            empty=False
            print('not found left')
             
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=5
            return new_pos,direction
        elif (new_pos[0]!= 0 and new_pos[1]!= size-1) and board[new_pos[0],new_pos[1]] == 0:
            new_pos[0] = new_pos[0]-1
            new_pos[1] = new_pos[1]+1
        else:
            empty=False
            print('not found up right')
               
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=6
            return new_pos,direction
        elif (new_pos[0]!= 0 and new_pos[1]!= 0) and board[new_pos[0],new_pos[1]] == 0:
            new_pos[0] = new_pos[0]-1
            new_pos[1] = new_pos[1]-1
        else:
            empty=False
            print('not found up left')
            
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=7
            return new_pos,direction
        elif (new_pos[0]!= size-1 and new_pos[1]!= size-1) and board[new_pos[0],new_pos[1]] == 0:
            new_pos[0] = new_pos[0]+1
            new_pos[1] = new_pos[1]+1
        else:
            empty=False
            print('not found down right')        
            
    empty = True
    new_pos = coord[:]       
    while empty == True:
        if board[new_pos[0],new_pos[1]] == player and not np.array_equal(new_pos, pieceNextTo):
            direction=8
            return new_pos,direction
        elif (new_pos[0]!= size-1 and new_pos[1]!= 0) and board[new_pos[0],new_pos[1]] == 0:
            new_pos[0] = new_pos[0]+1
            new_pos[1] = new_pos[1]-1
        else:
            empty=False
            print('not found down left')
          
            
    new_pos = pieceNextTo[:] #caso não seja enontrado vem a coordenada da peça adjacente
    return new_pos,direction
            
    
           
def boundary(board,direction,coord):
    #tipos de boundary - limite do tabuleiro ou peça no sitio
    #a direção vai ser a oposta
    pieces_loc = locationOfPieces(board)
    bounded = False
    for pos in pieces_loc:
        if direction == 1:
            if coord[0]+1 == size or (pos[0]==coord[0]+1 and pos[1]==coord[1]):
                bounded = True
                print('the lower boundary is in place and piece coming from the top will stop')
        elif direction == 2:
            if coord[0]-1 == -1 or (pos[0]==coord[0]-1 and pos[1]==coord[1]):
                bounded = True
                print('the upper boundary is in place and piece coming from the bottom will stop')
        elif direction == 3:
            if coord[1]-1 == -1 or (pos[0]==coord[0] and pos[1]==coord[1]-1):
                bounded = True
                print("there's a boundary in the left side")
        elif direction == 4:
            if coord[1]+1 == size or (pos[0]==coord[0] and pos[1]==coord[1]+1):
                bounded = True
                print("there's a boundary in the right side")
        elif direction == 5:
            if  coord[0]+1 == size or coord[1]-1 == -1 or (pos[0]==coord[0]+1 and pos[1]==coord[1]-1):
                bounded = True
                print("coming from up right it will be stopped")
        elif direction == 6:
            if coord[0]+1 == size or coord[1]+1 == size or (pos[0]==coord[0]+1 and pos[1]==coord[1]+1):
                bounded = True
                print("coming from up left it will be stopped")
        elif direction == 7:
            if coord[0]-1 == -1 or coord[1]-1 == -1 or (pos[0]==coord[0]-1 and pos[1]==coord[1]-1):
                bounded = True
                print("coming from down right it will be stopped")
        elif direction == 8:
            if coord[0]-1 == -1 or coord[1]+1 == size or (pos[0]==coord[0]-1 and pos[1]==coord[1]+1):
                bounded = True
                print("coming from down left it will be stopped")
        else:
            bounded = False
                
    return bounded    
        
               

# print(b)               
# blank_coord=[3,3]
# posi, dire = findPiece(b,blank_coord,2,[3,2])
# print('the last piece pos is ', posi)
# if boundary(b,dire,blank_coord):
#     print('funcemina')
# else:
#     print('not bounded')


def evaluate(board,playerPiece):
    pieces_loc=locationOfPieces(board)
    piece_count=0
    
    
    if playerPiece == 1:
        play=pieces_loc[0:3]
        ind1 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind1]
    elif playerPiece == 2: 
        play=pieces_loc[3:6]
        ind2 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind2]
    
    points = 0
    
    for ind in range(0,2):
        for p in range(-1,2):
            for q in range(-1,2):
                if play[ind][0]+p==play[ind+1][0] and play[ind][1]+q==play[ind+1][1]: # it's beter
                    # if play[ind][0]+p >= 0 and play[ind][0]+p <= size-1 and play[ind][1]+q >= 0 and play[ind][1]+q <= size-1 and board[play[ind][0]+p,play[ind][1]+q] == board[play[ind][0],play[ind][1]]... tentava desnecessaria

                    #2 peças juntas
                    
                    if piece_count == 0 and ind == 0 and ( (play[ind][0]+p+p==play[ind+2][0] and play[ind][1]+q+q==play[ind+2][1]) or (play[ind][0]-p==play[ind+2][0] and play[ind][1]-q==play[ind+2][1]) ):
                        points = 100
                        #3 em linha - vitoria - 100pts
                        
                    elif piece_count == 0 and play[ind][0]+p+p != -1 and play[ind][1]+q+q !=-1 and play[ind][0]+p+p != size and play[ind][1]+q+q != size :
                        #função para encontrar peça e função para ver se está barrado 
                        blank_coord = [play[ind][0]+p+p,play[ind][1]+q+q]
                        nextToPiece = [play[ind][0]+p,play[ind][1]+q]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(b,blank_coord,player,nextToPiece)
                        if boundary(b,direction,blank_coord):
                            points=10
                            #temos 2 peças em linha e o espaço seguinte em branco, na proxima jogada, pode ser preenchido com a peça que falta
                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points = 5
                            #3 peças em conjunto em direcoes diferentes
                    
                    elif piece_count == 0 and play[ind][0]-p != -1 and play[ind][1]-q != -1 and play[ind][0]-p != size and play[ind][1]-q != size:
                        blank_coord = [play[ind][0]-p,play[ind][1]-q]
                        nextToPiece = [play[ind][0],play[ind][1]]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(b,blank_coord,player,nextToPiece)
                        if boundary(b,direction,blank_coord):
                            points=10
                            #temos 2 peças em linha e o espaço seguinte em branco, na proxima jogada, pode ser preenchido com a peça que falta
                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points=5
                            #3 peças em conjunto em direcoes diferentes
                    
                    piece_count=piece_count+1
                    if piece_count==2:
                        points=5 #3 peças em conjunto em direcoes diferentes, ex: canto
                    
                    if p==1 and q==1 and points==0: #se no ultimo quadrado que está a ser avaliado nao tiver surgido nada do que esta anterior
                        points=3
    return points       
             
print(b)
print(evaluate(b,1)-evaluate(b,2))                    

            
