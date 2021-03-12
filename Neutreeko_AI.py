# Neutreeko - This project was developed by Duarte Rodrigues and Jacinta Ferreira for IA_MECD course.

import numpy as np
from game2dboard import Board
import easygui as eg
import copy 
import random
import time
import math


def init(board):

    if size%2==0: #Invented position for even square board
        board[0,0]=1
        board[0,2]=1
        board[1,1]=2
        
        board[size-1,size-1]=2
        board[size-1,size-3]=2
        board[size-2,size-2]=1
        
    elif size%2==1:
        odd_middle=math.floor(size/2)
        
        board[0,odd_middle-1]=1
        board[0,odd_middle+1]=1
        board[1,odd_middle]=2
        
        board[size-1,odd_middle-1]=2
        board[size-1,odd_middle+1]=2
        board[size-2,odd_middle]=1
        
def locationOfPieces(board):
    #Sets an array with the position of the board pieces [1 1 1 2 2 2]
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

def legal(board, coord, direction):
    #Checks legal moves
    init_coord = np.array(coord)
    empty = True
    new_pos= np.array(coord)
    
    
    if direction == 1: #UP
        #It evaluates the square and checks if it is 0 and if it not out of the board.
        #If everything is okay it tries the square above it (row-1)
        #It keeps going untill it finds another piece or untill the edge of the board
        #The process is the same for the other directions
        while empty == True:
            if new_pos[0]!=0 and board[new_pos[0]-1,new_pos[1]] == 0:
                new_pos[0] = new_pos[0]-1
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
                new_pos[1] = new_pos[1]-1
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
        return init_coord #if there's no possible move, the function returns the initial coordinate given
    else:
        return new_pos

def move_piece(board, init_coord, final_coord ):
    if not np.array_equal(final_coord,init_coord):
        board[final_coord[0],final_coord[1]] = board[init_coord[0],init_coord[1]]
        board[init_coord[0],init_coord[1]]=0

def clearHistory():
    global history
    
    erase=[]
    for ind in range(1, history.shape[0]):
        erase.append(ind)
    
    history=np.delete(history,erase,0)


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
    #checks if there is a boundary (limit of the board or oponent piece) to stop the third piece in the right place to make a 3-in-a-row
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
    for ind in range(0,2):
        for p in range(-1,2):
            for q in range(-1,2):
                if play[ind][0]+p==play[ind+1][0] and play[ind][1]+q==play[ind+1][1]:                   
                    #2 pieces together
                    
                    if piece_count == 0 and ind == 0 and ( (play[ind][0]+p+p==play[ind+2][0] and play[ind][1]+q+q==play[ind+2][1]) or ( play[ind][0]-p==play[ind+2][0] and play[ind][1]-q==play[ind+2][1]) ):
                        points = 100
                        return points
                        #3-in-a-row: victory - 100pts
                        
                    if piece_count == 0 and play[ind][0]+p+p != -1 and play[ind][1]+q+q !=-1 and play[ind][0]+p+p != size and play[ind][1]+q+q != size :
                        # Checks the first extrimity of the 2 piece line. In the square of that extrimity, checks all direction to try and find
                        #the third missing piece. If it does, then checks the boundary to see if the pice can slide and stop in the right place
                        blank_coord = [play[ind][0]+p+p,play[ind][1]+q+q]
                        nextToPiece = [play[ind][0]+p,play[ind][1]+q]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(board,blank_coord,player,nextToPiece)
                        if boundary(board,direction,blank_coord):
                            points=10 # pre-win move: 10 points
                            return points

                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points = 5 #3 pieces in a cluster in different directions: 5 points - better than having only 2
                            return points
                            
                    
                    if piece_count == 0 and play[ind][0]-p != -1 and play[ind][1]-q != -1 and play[ind][0]-p != size and play[ind][1]-q != size:
                       # Same thinking, but for the other extremity
                        blank_coord = [play[ind][0]-p,play[ind][1]-q]
                        nextToPiece = [play[ind][0],play[ind][1]]
                        player = board[play[ind][0],play[ind][1]]
                        pos_piece3, direction = findPiece(board,blank_coord,player,nextToPiece)
                        if boundary(board,direction,blank_coord):
                            points=10 # pre-win move: 10 points
                            return points

                        elif not np.array_equal(pos_piece3,nextToPiece) and ( (pos_piece3[0]-nextToPiece[0])**2 == 0 or (pos_piece3[0]-nextToPiece[0])**2 == 1 ) and ( (pos_piece3[1]-nextToPiece[1])**2 == 0 or (pos_piece3[1]-nextToPiece[1])**2 == 1 ):
                            points=5 #3 pieces in a cluster in different directions: 5 points - better than having only 2
                            return points
                            
                    
                    piece_count=piece_count+1
                    if piece_count==2:
                        points=5 #3 pieces in a cluster in different directions: 5 points (completes the missing cluster cases)
                        return points
                        
                    
                    if points==0: #only 2 pieces together, because no other points were given
                        points=3
                        
                        
                elif ind == 0 and play[ind][0]+p==play[ind+2][0] and play[ind][1]+q==play[ind+2][1]: #the previous case was for the relation between piece index 0 and 1. Now let's see if indexes 0 and 2 are together
                    
                    if points==0: #only 2 pieces together for now, we don't return because some other points can still be attributed
                        points=3
                        

    return points #or 0 - pieces all scattered or 3 - only 2 pieces together     

#Minimax Search

def children(board,player):
    #All possible boards that can outcome in a player term
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
            if not np.array_equal(test,board):
                Test3D = np.array([test])
                board_children=np.concatenate( (board_children,Test3D) )
                test = board.copy()
                
    board_children=np.delete(board_children,0, 0) #delete the padding element
    
    # Sort the boards according to their evaluation (speeds the alpha-beta pruning)
    # If it was not sorted the level of accuracy is lower - would be a lower level A.I.
    eva=[]
    for child in board_children:
        ev=evaluate(child,1)-evaluate(child,2)
        eva.append(ev)
    
    eva=np.array(eva)
    new_index = eva.argsort()[::-1]
    board_children=board_children[new_index]
    
    # print(board_children.shape[0]) # Branching factor of that board - the mean branching factor is 15
    return board_children

def gameover(board):
    result=False

    if evaluate(board,1) >= 90:
        #player 1 wins
        result = True
    elif evaluate(board,2) >= 90:
        #player2 wins
        result = True
    
    return result

def findMove(init_board,final_board):
    #Finds the move that user did, taking as input the previous board and current one
    for i in range(0,size):
        for j in range(0,size):
            if init_board[i,j] != 0 and final_board[i,j]==0:
                init_coord=[i,j]
            elif init_board[i,j] == 0 and final_board[i,j]!=0:   
                final_coord=[i,j]
    return (init_coord,final_coord)
       
def randomMove(board,player):
    #Level 0 A.I.: Random piece move, within the rules
    board_children=children(board,player)
    random.seed()
    a=random.randint(0,board_children.shape[0]-1)
    
    eval=evaluate(board_children[a],1)-evaluate(board_children[a],2)
    return board_children[a],eval

def minimax(board,depth, maximizingPlayer):
    #Implementing the standard minimax algorithm
    
    #When it reaches the end of the tree or when it is game over
    if depth == 0 or gameover(board):
        ev=evaluate(board,1)-evaluate(board,2)
        return (board,ev)
    
    #Recursive call of the minimax, lowering the depth each iteration
    best_play=np.zeros((size,size))
    if maximizingPlayer:
        maxEval = -1000000
        
        for child in children(board,1):
            _, eval = minimax(child,depth-1, False)#The next depth children is player 2
                   
            if eval > maxEval:
                maxEval = eval
                best_play = child
                
        return (best_play,maxEval)
    else:
        minEval=1000000
        for child in children(board,2):
            _, eval = minimax(child,depth-1, True)#The next depth children is player 1
                       
            if eval < minEval:
                minEval = eval
                best_play = child

        return (best_play,minEval)

def minimaxAB(board,depth,alpha,beta, maximizingPlayer):
    #Implementing the minimax algorithm with Alpha-Beta pruning 
    
    #When it reaches the end of the tree or when it is game over
    if depth == 0 or gameover(board):
        ev=evaluate(board,1)-evaluate(board,2)
        return (board,ev)
    
    #Recursive call of the minimax, lowering the depth each iteration
    #Takes into consideration alpha and beta terms. It breaks out of the loop if the conditions are met.
    best_play=np.zeros((size,size))
    if maximizingPlayer:
        maxEval = -1000000
        for child in children(board,1):
            _, eval = minimaxAB(child,depth-1,alpha,beta, False)#The next depth children is player 2

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
            _, eval = minimaxAB(child,depth-1,alpha,beta, True)#The next depth children is player 1
            
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
    bo.cell_size = 69
    bo.cell_color = "LightSeaGreen"
    bo.margin = 15
    bo._margin_color = "#001f35"
    bo.create_output(background_color="#001f35", color="#ffff70", font_size=12)
    bo.print('          Black (Player 1) Moves First')
    
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
    global history
    
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
            
            if click == 1 and np.array_equal(pos,[row,col]) and selected == False:#No piece selected
                
                if jog == 1:
                    bo[row][col]=11
                elif jog ==2:
                    bo[row][col]=22
                
                for dir in range(1,9):
                    legal_coord = legal(b,[row,col],dir)
                    if not np.array_equal(legal_coord,[row,col]):
                        bo[legal_coord[0]][legal_coord[1]]=3 
                      
                click=2
                selected = True
                origin=[row,col]
                break
            elif click == 2 and np.array_equal(origin,[row,col]) and selected == True :#Deselecting the previous selected piece
                
                if jog == 1:
                    bo[row][col]=1
                elif jog ==2:
                    bo[row][col]=2
                
                for dir in range(1,9):
                    legal_coord = legal(b,[row,col],dir)
                    if not np.array_equal(legal_coord,[row,col]):
                        bo[legal_coord[0]][legal_coord[1]]=0
                        
                click=1
                selected = False
                origin=[-1,-1]
                break
        
        if selected == True and bo[row][col]==3: #if the mouse clicked a legal square, moves the piece and calculate heuristics
            
            if jog == 1:
                bo[origin[0]][origin[1]]=1
            elif jog ==2:
                bo[origin[0]][origin[1]]=2
            
            move_piece_GUI(bo, origin, [row,col])
            move_piece(b,origin,[row,col])
            nextBoard = np.array([b])
            history=np.concatenate( (history,nextBoard) )
            turn +=1
            bo.print('Player',(turn % 2)+1,'to move! ','Heuristic Evaluation - Player 1:',evaluate(b,1),'\nPlayer 2:',-evaluate(b,2),' Total Evaluation: ',evaluate(b,1)-evaluate(b,2) )
            selected = False
            click=1
            for i in range(0,size):
                for j in range(0,size):
                    if bo[i][j]==3:
                        bo[i][j]=0
            
        #cheks if any of the player won
        if gameover(b) and jog==1:
             
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, Black wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                clearHistory()
                turn=0
                bo.print('          Black (Player 1) Moves First')
            else:
                bo.close()
            
        elif gameover(b) and jog==2:
             
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, White wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                clearHistory()
                turn=0
                bo.print('          Black (Player 1) Moves First')
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
    global history
    
    if not gameover(b):
        
        if turn % 2 == 0:
            jog=1

        pieces_loc=locationOfPieces(b)
        
        #Player one is always the human
        if jog == 1:
            play=pieces_loc[0:3]
            ind1 = np.lexsort((play[:,1], play[:,0])) #sort the pieces from the top left to bottom right
            play=play[ind1]
 
            for pos in play:
                if click == 1 and np.array_equal(pos,[row,col]) and selected == False: # No piece selected
                    
                    if jog == 1:
                        bo[row][col]=11
                    
                    for dir in range(1,9):
                        legal_coord = legal(b,[row,col],dir)
                        if not np.array_equal(legal_coord,[row,col]):
                            bo[legal_coord[0]][legal_coord[1]]=3       
                    click=2
                    selected = True
                    origin=[row,col]
                    break
                elif click == 2 and np.array_equal(origin,[row,col]) and selected == True : #Deselecting the previous selected piece
                    if jog == 1:
                        bo[row][col]=1

                    for dir in range(1,9):
                        legal_coord = legal(b,[row,col],dir)
                        if not np.array_equal(legal_coord,[row,col]):
                            bo[legal_coord[0]][legal_coord[1]]=0
                    click=1
                    selected = False
                    origin=[-1,-1]
                    break
        
            if selected == True and bo[row][col]==3: #if the mouse clicked a legal square, moves the piece and calculate heuristics
                
                if jog == 1:
                    bo[origin[0]][origin[1]]=1
                
                move_piece_GUI(bo, origin, [row,col])
                move_piece(b,origin,[row,col])
                nextBoard = np.array([b])
                history=np.concatenate( (history,nextBoard) )
                turn=turn+1
                bo.print('A.I. Engine to move!','Heuristic Evaluation - Player 1:',evaluate(b,1),'\nPlayer 2:',-evaluate(b,2),' Total Evaluation: ',evaluate(b,1)-evaluate(b,2) )
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
                        jog=2
                        #Level 1
                        if level == "Greedy":
                            best_p,eval=minimax(b,1,False) #Standard Minimax com depth 1 is a greedy search
                        
                        #Level 2    
                        elif level == "Minimax Depth = 3": #Minimax w/ Apha-Beta Pruning because it's faster 
                            bo.pause(10,change_cursor=False)
                            best_p,eval=minimaxAB(b,3,-100000,100000,False)
                        
                        #Level 3    
                        elif level == "Minimax Depth = 4":
                            bo.print('Please wait for the Engine move (30 sec to 1 min)') 
                            best_p,eval=minimaxAB(b,4,-100000,100000,False)
                        
                        #Level 0    
                        elif level == 'Random Positioning':
                            best_p,eval = randomMove(b,jog)
                        
                        #Plays the best move that the A.I. decided
                        coord_init,coord_final=findMove(b,best_p)
                        move_piece_GUI(bo, coord_init,coord_final )
                        move_piece(b,coord_init,coord_final)
                        nextBoard = np.array([b])
                        history=np.concatenate( (history,nextBoard) )
                        bo.print('Player1 to move!  Predicted «',level,'» evaluation:',eval, '\nCurrent Board Eval:',evaluate(b,1)-evaluate(b,2) )

                        turn=turn+1                  
    
        #Checks if there is a winner
        if gameover(b) and jog==1:
             
            if eg.ccbox(msg='\n\n\n\n                           Congratulations, Black wins!',title="Congratulations",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                clearHistory()
                turn=0
                bo.print('          Black (Player 1) Moves First')
            else:
                bo.close()   
        elif gameover(b) and jog==2:
             
            if eg.ccbox(msg='\n\n\n\n                           You will beat it next time!',title="Retry?",choices=("Play again?","Quit!")):     # show a Continue/Cancel dialog
                b=np.zeros((size,size))
                init(b)
                arrayToGUI(b,bo)
                clearHistory()
                turn=0
                bo.print('          Black (Player 1) Moves First')
            else:
                bo.close()

def ComputerVsComputer():
    global turn
    global winner
    global levelP1
    global levelP2
    global history
    
    
    while not gameover(b):
        jog=3 # Initialization of the variable
        if turn % 2 == 0:
            jog=1
            
            #Level 1
            if levelP1 == "Greedy":#Standard Minimax com depth 1 is a greedy search
                best_p,eval=minimax(b,1,True)
                bo.pause(1500,change_cursor=False) #1,5 sec for the human to see what happened
            
            #Level 2    
            elif levelP1 == "Minimax Depth = 3":#Minimax w/ Apha-Beta Pruning because it's faster 
                best_p,eval=minimaxAB(b,3,-100000,100000,True)
                bo.pause(10,change_cursor=False)
            
            #Level 3    
            elif levelP1 == "Minimax Depth = 4":
                if turn==0:
                    bo.print('Please wait for the Engine move (30 sec to 1 min)')
                bo.pause(10,change_cursor=False)
                best_p,eval=minimaxAB(b,4,-100000,100000,True)
                bo.pause(10,change_cursor=False)
            
            #Level 4    
            elif levelP1 == 'Random Positioning':
                best_p,eval = randomMove(b,jog)
                bo.pause(1500,change_cursor=False) #1,5 sec for the human to see what happened
                

        else:
            jog=2
            
            if levelP2 == "Greedy":
                best_p,eval=minimax(b,1,False)
                bo.pause(1500,change_cursor=False)#1,5 sec for the human to see what happened
                
            elif levelP2 == "Minimax Depth = 3":
                best_p,eval=minimaxAB(b,3,-100000,100000,False)
                bo.pause(10,change_cursor=False)
                
            elif levelP2 == "Minimax Depth = 4":
                if turn==1:
                    bo.print('Please wait for the Engine move (30 sec to 1 min)')
                bo.pause(10,change_cursor=False)
                best_p,eval=minimaxAB(b,4,-100000,100000,False)
                bo.pause(10,change_cursor=False)
                
            elif levelP2 == 'Random Positioning':
                best_p,eval = randomMove(b,jog)
                bo.pause(1500,change_cursor=False)#1,5 sec for the human to see what happened
                

        #Plays the move each engine decided
        if not gameover(b):      
            coord_init,coord_final=findMove(b,best_p)
            move_piece_GUI(bo, coord_init,coord_final )
            move_piece(b,coord_init,coord_final)
            nextBoard = np.array([b])
            history=np.concatenate( (history,nextBoard) )
            
            if jog ==1:
                bo.print('Player2 to move! Predicted P1«',levelP1,'» evaluation:',eval,'\nCurrent Board Eval:',evaluate(b,1)-evaluate(b,2) )
            elif jog==2:
                bo.print('Player1 to move! Predicted P2«',levelP2,'» evaluation:',eval,'\nCurrent Board Eval:',evaluate(b,1)-evaluate(b,2) )

            turn=turn+1     
            
        #Checks if a player won           
        if gameover(b) and jog==1:
             
            winner=eg.msgbox('\n\n\n\n                    The calculations do not Fail. Black won!\n                     Dont forget to close the board window!')
        elif gameover(b) and jog==2:
             
            winner=eg.msgbox('\n\n\n\n                    The calculations do not Fail. White won!\n                     Dont forget to close the board window!')

def rightHint_leftHistory(key):
    global turn
    
    #The right arrow key in the keyboardshows a suggested move for 3 secons
    #The blue ball is the piece you should move
    # The red ball is the suggested place
    if key == 'Right':
        
        if turn % 2 == 0:
            jog=1
            p=True
        else:
            jog=2
            p=False
            
        best_p,_=minimaxAB(b,3,-100000,100000,p)
        coord_init,coord_final=findMove(b,best_p)
        #Appears sugestion
        bo[coord_init[0]][coord_init[1]]=4
        bo[coord_final[0]][coord_final[1]]=5
        bo.pause(3000,change_cursor=True)
        #Back to normal game
        bo[coord_init[0]][coord_init[1]]=jog
        bo[coord_final[0]][coord_final[1]]=0
        
    if key == 'Left':
        print('\n####################################  History of Moves  ####################################\n')
        print(turn,' rounds played.\n')
        print(history)
        print('##########################################  End  ##########################################\n')

    

if __name__ == "__main__":
    # Initialize a square board with a certain size and the 3 pieces for each player
          
    #Main Menu
    welcome="hello"
    rules=True
    mode="let's see"
    while not(rules==None or welcome==None or welcome == "PLAY!" or rules == False):
        welcome=eg.buttonbox(msg="\n\n\n\n                               Welcome to Neutreeko", title="Neutreeko", choices=("PLAY!","Game Rules") )
        if welcome=="PLAY!":
            size = eg.integerbox(msg='Enter a number between 4 and 9 to specify the size of the square board.\n (Default = 5)',title='Size of the Board',default=5,lowerbound=4,upperbound=9)
            if size == None or size==False:
                break
            b=np.zeros((size,size))
            init(b)  
            history = np.array([b])
            mode=eg.buttonbox(msg="\n\n\n                         Which mode would you like to play?\n                 To get a hint while playing press the right arrow.\n To see the history of moves press the left arrow, it appears in the terminal.", title="Let's Play!", choices=("Human VS Human","Human Vs Computer","Computer VS Computer"))
        elif welcome== "Game Rules":
            rules=eg.ccbox(msg="-Movement: A piece slides orthogonally or diagonally until stopped by \nan occupied square or the border of the board. Black always moves first.\n\n -Objective: To get three in a row, orthogonally or diagonally. The row must be connected.\n\nIf you need a Hint, click on the RIGHT ARROW on your keyboard (be aware it takes 2 secons to appear). The blue ball represents the piece you should move, and red ball is the suggested square to move.\n\nIf you want to see the history of the moves, click the LEFT ARROW KEY, and it will appear the move sequence played in the game.",
                        title="Neutreeko Game Rules",choices=("Go back to Main Menu","Cancel"))
        
        
    #Declaration of the different mouse events depending on the game modes
    if mode == "Human VS Human":
        start_game(size)
        click=1
        origin=[-1,-1]
        selected = False
        turn=0    
        bo.on_mouse_click = HumanVsHuman
        bo.on_key_press = rightHint_leftHistory
        
        bo.show()
        
    elif mode=="Human Vs Computer":
        
        click=1
        origin=[-1,-1]
        selected = False
        turn=0 
        level=eg.buttonbox(msg="\n                           Human goes First \n\n                           What is the A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 4"))
        if level != None:
            start_game(size)
            bo.on_mouse_click = HumanVsComputer
            bo.on_key_press = rightHint_leftHistory            
            bo.show()
        
    elif mode == "Computer VS Computer":
        
        turn=0
        levelP1=eg.buttonbox(msg="\n\n\n                       What is the Player 1 A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 4"))
        levelP2=eg.buttonbox(msg="\n\n\n                       What is the Player 2 A.I. Level?", title="Engine Level", choices=("Random Positioning","Greedy","Minimax Depth = 3","Minimax Depth = 4"))
        if not (levelP1 == None or levelP2 == None):
            eg.msgbox("                         The automatic Game will start!\n            Please account for the time each Engine Level takes to play",ok_button='Start')
            
            start_game(size)
            bo.on_start = ComputerVsComputer
            bo.on_key_press = rightHint_leftHistory
            bo.show()

    
