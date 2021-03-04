# Neutreeko - This project was developed by Duarte Rodrigues and Jacinta Ferreira for IA_MECD course.

import numpy as np
import copy 
from game2dboard import Board
import easygui as eg
import random
import time


def init(board):
    board[0,1]=1
    board[0,3]=1
    board[3,2]=1
    board[1,2]=2
    board[4,1]=2
    board[4,3]=2

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
                        pos_piece3, direction = findPiece(board,blank_coord,player,nextToPiece)
                        if boundary(board,direction,blank_coord):
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
                        pos_piece3, direction = findPiece(board,blank_coord,player,nextToPiece)
                        if boundary(board,direction,blank_coord):
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

#Minimax Search

#All possible boards that can outcome in a player term
def children(board,player): #
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
                
    board_children=np.delete(board_children,0, 0) #delete the padding element
    
    #Sort the boards according to their evaluation (speeds the alpha-beta)
    eva=[]
    for child in board_children:
        ev=evaluate(child,1)-evaluate(child,2)
        eva.append(ev)
    
    eva=np.array(eva)
    new_index = eva.argsort()[::-1]
    board_children=board_children[new_index]
    
    # print(board_children.shape[0]) # Branching factor of that board
    return board_children

def gameover(board):
    result=False

    if evaluate(board,1) >= 90:
        #player 1 ganhou
        result = True
    elif evaluate(board,2) >= 90:
        #player2 ganhou
        result = True
    
    return result

def findMove(init_board,final_board):
    #return de tuple com coordenada inical e final da peça que se mexeu([,],[])
    for i in range(0,size):
        for j in range(0,size):
            if init_board[i,j] != 0 and final_board[i,j]==0:
                init_coord=[i,j]
            elif init_board[i,j] == 0 and final_board[i,j]!=0:   
                final_coord=[i,j]
    return (init_coord,final_coord)
       
def randomMove(board,player):
    board_children=children(board,player)
    random.seed()
    a=random.randint(0,board_children.shape[0]-1)
    
    eval=evaluate(board_children[a],1)-evaluate(board_children[a],2)
    return board_children[a],eval

def minimax(board,depth, maximizingPlayer):
    
    if depth == 0 or gameover(board):
        ev=evaluate(board,1)-evaluate(board,2)
        return (board,ev)
    
    best_play=np.zeros((size,size))
    if maximizingPlayer:
        maxEval = -1000000
        
        for child in children(board,1):
            _, eval = minimax(child,depth-1, False)
                   
            if eval > maxEval:
                maxEval = eval
                best_play = child
                
        return (best_play,maxEval)
    else:
        minEval=1000000
        for child in children(board,2):
            _, eval = minimax(child,depth-1, True) 
                       
            if eval < minEval:
                minEval = eval
                best_play = child

        return (best_play,minEval)

def minimaxAB(board,depth,alpha,beta, maximizingPlayer):
    if depth == 0 or gameover(board):
        ev=evaluate(board,1)-evaluate(board,2)
        return (board,ev)
    
    best_play=np.zeros((size,size))
    if maximizingPlayer:
        maxEval = -1000000
        for child in children(board,1):
            _, eval = minimaxAB(child,depth-1,alpha,beta, False)

            if eval > maxEval:
                maxEval = eval
                best_play = child

            alpha = max(eval,alpha)
            if beta < alpha:
                break
            
        return (best_play,maxEval)
    
    else:
        minEval=1000000
        for child in children(board,2):
            _, eval = minimaxAB(child,depth-1,alpha,beta, True)
            
            if eval < minEval:
                minEval = eval
                best_play = child
            
            beta = min(beta,eval)
            if beta < alpha:
                break
            
        return (best_play,minEval)
    
# Neutreeko GUI

def arrayToGUI(array_board,GUI_board):
    GUI_board.clear()
    for i in range(0,size):
            for j in range(0,size):
                if array_board[i,j] == 0:
                    GUI_board[i][j] = 0
                elif array_board[i,j] == 1:
                    GUI_board[i][j] = 1
                elif array_board[i,j] == 2:
                    GUI_board[i][j] = 2

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
    global winner
    global b
    
    if not gameover(b):
        
        if turn % 2 == 0:
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
            
    
        if gameover(b) and jog==1:
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, Black wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                turn=0
            else:
                bo.close()
            
        elif gameover(b) and jog==2:
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, White wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                turn=0
            else:
                bo.close()
    
def HumanVsComputer(btn,row,col):
    global click
    global origin
    global selected
    global turn
    global winner
    global level
    global b
    
    if not gameover(b):
        
        if turn % 2 == 0:
            jog=1

        pieces_loc=locationOfPieces(b)
    
        if jog == 1:
            play=pieces_loc[0:3]
            ind1 = np.lexsort((play[:,1], play[:,0])) #sort the pieces top left to bottom right
            play=play[ind1]
 
            for pos in play:
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
                
                
                if not gameover(b):
                    #The AI plays immediatelly after the human            
                    if turn % 2 == 0:
                        jog=1
                    else:
                        jog=2 #USAR A EVAL DO MINIMAX QUANDO TIVER o terminal
                        if level == "Greedy":
                            best_p,_=minimax(b,1,False) #Minimax com depth 1 é uma greedy search
                        elif level == "Minimax Depth = 3": #Minimax w/ Apha e Beta because it's faster 
                            #timer function - fazia print no terminal
                            bo.pause(10,change_cursor=False)
                            best_p,_=minimaxAB(b,3,-100000,100000,False)
                        elif level == "Minimax Depth = 5 (1,5 min to 3 min per move)":
                            eg.msgbox('\n\n                       Please wait for the Engine move (1,5 to 3 min)',ok_button='Go back to the board') 
                            #timer function - fazia print no terminal
                            best_p,_=minimaxAB(b,5,-100000,100000,False)
                        elif level == 'Random Positioning':
                            best_p,_ = randomMove(b,jog)
                        
                            
                        coord_init,coord_final=findMove(b,best_p)
                        move_piece_GUI(bo, coord_init,coord_final )
                        move_piece(b,coord_init,coord_final)
                        turn=turn+1                  
    
        if gameover(b) and jog==1:
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, Black wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                turn=0
            else:
                bo.close()   
        elif gameover(b) and jog==2:
            if eg.ccbox(msg='\n\n\n\n                           You will beat it next time!',title="Retry?",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                turn=0
            else:
                bo.close()

def ComputerVsComputer():
    global turn
    global winner
    global levelP1
    global levelP2
    
    eg.msgbox('\n\n\n\n          Center the window of the game board before you continue',ok_button='Continue')
    while not gameover(b):
        jog=3
        if turn % 2 == 0:
            jog=1
            if levelP1 == "Greedy":
                best_p,_=minimax(b,1,True) #Minimax com depth 1 é uma greedy search
                bo.pause(1500,change_cursor=False)
            elif levelP1 == "Minimax Depth = 3": #Minimax w/ Apha e Beta because it's faster 
                #timer function - fazia print no terminal
                best_p,_=minimaxAB(b,3,-100000,100000,True)
                bo.pause(10,change_cursor=False)
            elif levelP1 == "Minimax Depth = 5 (1,5 min to 3 min per move)":
                # eg.msgbox('\n\n                       Please wait for the Engine move (1,5 to 3 min)',ok_button='Go back to the board') 
                #timer function - fazia print no terminal
                best_p,_=minimaxAB(b,5,-100000,100000,True)
            elif levelP1 == 'Random Positioning':
                best_p,_ = randomMove(b,jog)
                bo.pause(1500,change_cursor=False)

        else:
            jog=2
            if levelP2 == "Greedy":
                best_p,_=minimax(b,1,False) #Minimax com depth 1 é uma greedy search
                bo.pause(1500,change_cursor=False)
            elif levelP2 == "Minimax Depth = 3": #Minimax w/ Apha e Beta because it's faster
                #timer function - fazia print no terminal
                best_p,_=minimaxAB(b,3,-100000,100000,False)
                bo.pause(10,change_cursor=False)
            elif levelP2 == "Minimax Depth = 5 (1,5 min to 3 min per move)":
                # eg.msgbox('\n\n                       Please wait for the Engine move (1,5 to 3 min)',ok_button='Go back to the board') 
                #timer function - fazia print no terminal
                best_p,_=minimaxAB(b,5,-100000,100000,False)
            elif levelP2 == 'Random Positioning':
                best_p,_ = randomMove(b,jog)
                bo.pause(1500,change_cursor=False)

                
        if not gameover(b):      
            coord_init,coord_final=findMove(b,best_p)
            move_piece_GUI(bo, coord_init,coord_final )
            move_piece(b,coord_init,coord_final)
            turn=turn+1     
                   
        if gameover(b) and jog==1:
            winner=eg.msgbox('\n\n\n\n                           The calculations do not Fail. Black won!')
        elif gameover(b) and jog==2:
            winner=eg.msgbox('\n\n\n\n                           The calculations do not Fail. White won!')

def hint(key):
    global turn
    
    if key == 'Right':
        
        if turn % 2 == 0:
            jog=1
            p=True
        else:
            jog=2
            p=False
            
        best_p,_=minimaxAB(b,3,-100000,100000,p)
        coord_init,coord_final=findMove(b,best_p)
        bo[coord_init[0]][coord_init[1]]=4
        bo[coord_final[0]][coord_final[1]]=5
        bo.pause(3000,change_cursor=True)
        bo[coord_init[0]][coord_init[1]]=jog
        bo[coord_final[0]][coord_final[1]]=0


if __name__ == "__main__":
    # Initialize a square board with a certain size and the 3 pieces for each player
    size=5
    b=np.zeros((size,size))
    init(b)        

    #Main Menu
    welcome="hello"
    rules=True
    mode="let's see"
    while not(rules==None or welcome==None or welcome == "PLAY!" or rules == False):
        welcome=eg.buttonbox(msg="\n\n\n\n                               Welcome to Neutreko", title="Neutreeko", choices=("PLAY!","Game Rules") )
        if welcome=="PLAY!":
            mode=eg.buttonbox(msg="\n\n\n                         Which mode would you like to play?\n                 To get a hint while playing press the right arrow", title="Let's Play!", choices=("Human VS Human","Human Vs Computer","Computer VS Computer"))
        elif welcome== "Game Rules":
            rules=eg.ccbox(msg="-Movement: A piece slides orthogonally or diagonally until stopped by \nan occupied square or the border of the board. Black always moves first.\n\n -Objective: To get three in a row, orthogonally or diagonally. The row must be connected.\n\nIf you need a Hint, click on the RIGHT ARROW on your keyboard (be aware it takes 2 secons do appear). The blue ball represents the piece you should move, and red ball is the suggested square to move.",
                        title="Neutreeko Game Rules",choices=("Go back to Main Menu","Cancel"))
        

    if mode == "Human VS Human":
        start_game(size)
        click=1
        origin=[-1,-1]
        selected = False
        turn=0    
        bo.on_mouse_click = HumanVsHuman
        bo.on_key_press = hint
        bo.show()
        
    elif mode=="Human Vs Computer":
        start_game(size)
        click=1
        origin=[-1,-1]
        selected = False
        turn=0 
        level=eg.buttonbox(msg="\n                           Human goes First \n\n                           What is the A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 5 (1,5 min to 3 min per move)"))
        bo.on_mouse_click = HumanVsComputer
        bo.on_key_press = hint
        bo.show()
        
    elif mode == "Computer VS Computer":
        start_game(size)
        turn=0
        levelP1=eg.buttonbox(msg="\n\n\n                       What is the Player 1 A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 5 (1,5 min to 3 min per move)"))
        levelP2=eg.buttonbox(msg="\n\n\n                       What is the Player 2 A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 5 (1,5 min to 3 min per move)"))

        eg.msgbox("                         The automatic Game will start!\n            Please account for the time each Engine Level takes to play",ok_button='Start')
        
        bo.on_start = ComputerVsComputer
        bo.show()

    
