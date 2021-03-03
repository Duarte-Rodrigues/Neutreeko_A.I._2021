# Neutreeko - This project was developed by Duarte Rodrigues and Jacinta Ferreira for IA_MECD course.

import numpy as np
import copy 
from game2dboard import Board
size=5

b=np.zeros((size,size))

def inic(b):
    b[4,1]=2
    b[3,2]=2
    b[2,3]=2
    b[3,0]=1
    b[0,0]=1
    b[2,0]=1

def init(b):
    b[0,1]=1
    b[0,3]=1
    b[3,2]=1
    b[1,2]=2
    b[4,1]=2
    b[4,3]=2
    # pieces_loc=np.array([[0,1],[0,3],[3,2],[1,2],[4,1],[4,3]])
    # return pieces_loc

init(b)
# inic(b)
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
        # print("Move not possible")
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
            # print('not found up')
    
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
            # print('not found down')
            
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
            # print('not found right')
            
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
            # print('not found left')
             
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
            # print('not found up right')
               
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
            # print('not found up left')
            
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
            # print('not found down right')        
            
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
            # print('not found down left')
          
            
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
                # print('the lower boundary is in place and piece coming from the top will stop')
        elif direction == 2:
            if coord[0]-1 == -1 or (pos[0]==coord[0]-1 and pos[1]==coord[1]):
                bounded = True
                # print('the upper boundary is in place and piece coming from the bottom will stop')
        elif direction == 3:
            if coord[1]-1 == -1 or (pos[0]==coord[0] and pos[1]==coord[1]-1):
                bounded = True
                # print("there's a boundary in the left side")
        elif direction == 4:
            if coord[1]+1 == size or (pos[0]==coord[0] and pos[1]==coord[1]+1):
                bounded = True
                # print("there's a boundary in the right side")
        elif direction == 5:
            if  coord[0]+1 == size or coord[1]-1 == -1 or (pos[0]==coord[0]+1 and pos[1]==coord[1]-1):
                bounded = True
                # print("coming from up right it will be stopped")
        elif direction == 6:
            if coord[0]+1 == size or coord[1]+1 == size or (pos[0]==coord[0]+1 and pos[1]==coord[1]+1):
                bounded = True
                # print("coming from up left it will be stopped")
        elif direction == 7:
            if coord[0]-1 == -1 or coord[1]-1 == -1 or (pos[0]==coord[0]-1 and pos[1]==coord[1]-1):
                bounded = True
                # print("coming from down right it will be stopped")
        elif direction == 8:
            if coord[0]-1 == -1 or coord[1]+1 == size or (pos[0]==coord[0]-1 and pos[1]==coord[1]+1):
                bounded = True
                # print("coming from down left it will be stopped")
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
    for ind in range(0,2): # esperando que so se joga com 3 peças
        for p in range(-1,2):
            for q in range(-1,2):
                if play[ind][0]+p==play[ind+1][0] and play[ind][1]+q==play[ind+1][1]: # it's beter
                    # if play[ind][0]+p >= 0 and play[ind][0]+p <= size-1 and play[ind][1]+q >= 0 and play[ind][1]+q <= size-1 and board[play[ind][0]+p,play[ind][1]+q] == board[play[ind][0],play[ind][1]]... tentava desnecessaria
                    
                    #2 peças juntas
                    
                    if piece_count == 0 and ind == 0 and ( (play[ind][0]+p+p==play[ind+2][0] and play[ind][1]+q+q==play[ind+2][1]) or ( play[ind][0]-p==play[ind+2][0] and play[ind][1]-q==play[ind+2][1]) ):
                        points = 100
                        return points
                        #3 em linha - vitoria - 100pts
                        
                    if piece_count == 0 and play[ind][0]+p+p != -1 and play[ind][1]+q+q !=-1 and play[ind][0]+p+p != size and play[ind][1]+q+q != size :
                        #função para encontrar peça e função para ver se está barrado 
                        blank_coord = [play[ind][0]+p+p,play[ind][1]+q+q]
                        nextToPiece = [play[ind][0]+p,play[ind][1]+q]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(b,blank_coord,player,nextToPiece)
                        if boundary(b,direction,blank_coord):
                            points=10
                            return points
                            #temos 2 peças em linha e o espaço seguinte em branco, na proxima jogada, pode ser preenchido com a peça que falta
                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points = 5
                            return points
                            #3 peças em conjunto em direcoes diferentes
                    
                    if piece_count == 0 and play[ind][0]-p != -1 and play[ind][1]-q != -1 and play[ind][0]-p != size and play[ind][1]-q != size:
                        blank_coord = [play[ind][0]-p,play[ind][1]-q]
                        nextToPiece = [play[ind][0],play[ind][1]]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(b,blank_coord,player,nextToPiece)
                        if boundary(b,direction,blank_coord):
                            points=10
                            return points
                            #temos 2 peças em linha e o espaço seguinte em branco, na proxima jogada, pode ser preenchido com a peça que falta
                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points=5
                            return points
                            #3 peças em conjunto em direcoes diferentes
                    
                    piece_count=piece_count+1
                    if piece_count==2:
                        points=5 #3 peças em conjunto em direcoes diferentes, ex: canto
                        return points
                        
                    
                    if points==0: #se no ultimo quadrado que está a ser avaliado nao tiver surgido nada do que esta anterior    
                        points=3
                        
                        
                elif ind == 0 and play[ind][0]+p==play[ind+2][0] and play[ind][1]+q==play[ind+2][1]: # we know we are dealing with 0 and 2, por isso falta ver onde esta o 1 em relacao!
                    
                    if points==0: #se no ultimo quadrado que está a ser avaliado nao tiver surgido nada do que esta anterior    
                        points=3
                        
                       
             
    return points       
             
# print(b)
# print(evaluate(b,2))                    


#Minimax Search

#All possible boards that can outcome from a player moving a piece
def children(board,player):
    pieces_loc=locationOfPieces(board)
    board_children=np.array([np.zeros((size,size))])
    
    if player == 1:
        play=pieces_loc[0:3]
        ind1 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind1]
    elif player == 2: 
        play=pieces_loc[3:6]
        ind2 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind2]
     
    test = board.copy()
    for pos in play:
        for direction in range(1,9):
            move_piece(test, pos, legal(board,pos,direction) )
            # concatenar os boards filhos que advem do movimento das peças de um jogador
            if not np.array_equal(test,board):
                Test3D = np.array([test])
                board_children=np.concatenate( (board_children,Test3D) )
                test = board.copy()
                
    
    board_children=np.delete(board_children,0, 0)
    return board_children

# print(children(b,1).shape[0]) # Branching factor of that board

def gameover(board):
    #por a margem como noventa
    if evaluate(board,1) >= 90:
        #player 1 ganhou
        return True
    elif evaluate(board,2) <= -90:
        #player2 ganhou
        return True
    else:
        return False

def minimax(board,depth,init_d, maximizingPlayer):
    
    if depth == 0 or gameover(board):
        ev=evaluate(board,1)-evaluate(board,2)
        return ev
    
    if maximizingPlayer:
        maxEval = -1000000
        for child in children(board,1):
            eval = minimax(child,depth-1,init_d, False)
            # print('board: \n',child,'\n\n eval: ',eval, ' maxEval: ', maxEval)
            
            if depth==init_d and eval > maxEval: #definida como 3 pq é o valor razoavel
                save = child.copy()
                
            maxEval = max(maxEval,eval)    
            if depth == init_d and np.array_equal(child,children(board,1)[children(board,1).shape[0]-1]): # se tivermos a avaliar a ultima child
                return maxEval, save
        
        return maxEval
    else:
        minEval=1000000
        for child in children(board,2):
            eval = minimax(child,depth-1,init_d, True)
            # print('board: \n',child,'\n\n eval: ',eval,  ' minEval: ', minEval)
            
            if depth==init_d and eval < minEval: #definida como 3
                save = child.copy()
                   
            minEval=min(minEval,eval)    
            if depth == init_d and np.array_equal(child,children(board,1)[children(board,1).shape[0]-1]): # se tivermos a avaliar a ultima child
                return minEval, save
              
        return minEval
        
def minimaxAB(board,depth,init_d,alpha,beta, maximizingPlayer):
    if depth == 0 or gameover(board):
        return evaluate(board,1)-evaluate(board,2)
    
    if maximizingPlayer:
        maxEval = -1000000
        for child in children(board,1):
            eval = minimaxAB(child,depth-1,init_d,alpha,beta, False)
            # print('board: \n',child,'\n\n eval: ',eval, ' maxEval: ', maxEval)
            
            if depth==init_d and eval > maxEval: #definida como 3 pq é o valor razoavel
                save = child.copy()
            
            maxEval = max(maxEval,eval)
            
            
            
            alpha = max(eval,alpha)
            if beta <= alpha:
                break
            
        if depth == init_d and np.array_equal(child,children(board,1)[children(board,1).shape[0]-1]): # se tivermos a avaliar a ultima child
            return maxEval, save
            
        return maxEval
    
    else:
        minEval=1000000
        for child in children(board,2):
            eval = minimaxAB(child,depth-1,init_d,alpha,beta, True)
            # print('board: \n',child,'\n\n eval: ',eval,  ' minEval: ', minEval)
            
            if depth==init_d and eval < minEval: #definida como 3
                save = child.copy()
            
            minEval=min(minEval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
            
        if depth == init_d and np.array_equal(child,children(board,1)[children(board,1).shape[0]-1]): # se tivermos a avaliar a ultima child
            return minEval, save
            
        return minEval
    
    
# print(minimax(b,3,3,True))
# print(minimaxAB(b,3,3,-100000,100000,True))



import ctypes 

def Mbox(title,text,style):
    return ctypes.windll.user32.MessageBoxW(0,text,title,style)

answer=Mbox("   Welcome to Neutreeko",'      Do you want to play against the computer?\n        For computer VS computer game press:\n                                     -Cancel-', 3)
#6 - yes / 7 - No/ 2 - Cancel


# Neutreeko GUI 

def arrayToGUI(array_board,GUI_board):
    pieces_loc=locationOfPieces(array_board)
    a=0
    for pos in pieces_loc:
        if a <3:
            value=1
        else:
            value=2
            
        GUI_board[pos[0]][pos[1]]=value
        a=a+1

def start_game(size):
    global bo 
    bo = Board(size, size)       
    arrayToGUI(b,bo)
    bo.title = "Neutreeko"
    bo.cell_size = 120       
    bo.cell_color = "LightGreen"
    bo.margin = 25
    bo._margin_color = "MediumSeaGreen"
    bo.create_output(background_color="MediumSeaGreen", color="black", font_size=12)
    
def move_piece_GUI(board, init_coord, final_coord ):
    if not np.array_equal(final_coord,init_coord):
        board[final_coord[0]][final_coord[1]] = board[init_coord[0]][init_coord[1]]
        board[init_coord[0]][init_coord[1]]=0        
        
def HumanVsHuman(btn,row,col):
    global click
    global origin
    global selected
    global turn
    
    if turn % 2 ==0:
        jog=1
    else:
        jog=2

    pieces_loc=locationOfPieces(b)
    
    if jog == 1:
        play=pieces_loc[0:3]
        ind1 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind1]
    elif jog == 2: 
        play=pieces_loc[3:6]
        ind2 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
        play=play[ind2]
 
    for pos in play:
        # print(click == 1 and np.array_equal(pos,[row,col]) and selected == False)
        # print(click == 2 and np.array_equal(origin,[row,col]) and selected == True)
        if click == 1 and np.array_equal(pos,[row,col]) and selected == False:
            for dir in range(1,9):
                legal_coord = legal(b,[row,col],dir) #resolver a questão do size
                if not np.array_equal(legal_coord,[row,col]):
                    bo[legal_coord[0]][legal_coord[1]]=3       
            click=2
            selected = True
            origin=[row,col]
            break
        elif click == 2 and np.array_equal(origin,[row,col]) and selected == True :
            for dir in range(1,9):
                legal_coord = legal(b,[row,col],dir) #resolver a questão do size
                if not np.array_equal(legal_coord,[row,col]):
                    bo[legal_coord[0]][legal_coord[1]]=0
            click=1
            selected = False
            origin=[-1,-1]
            break
        
    if selected == True and bo[row][col]==3:
        move_piece_GUI(bo, origin, [row,col])
        move_piece(b,origin,[row,col])
        turn=turn+1
        selected = False
        click=1
        for i in range(0,size):
            for j in range(0,size):
                if bo[i][j]==3:
                    bo[i][j]=0


#Human vs Human Check basic

if answer == 7:
    start_game(size)
    click=1
    origin=[-1,-1]
    selected = False
    turn=0    
    bo.on_mouse_click = HumanVsHuman
    bo.show()



