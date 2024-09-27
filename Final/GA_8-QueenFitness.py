def fitness(board):
    board.insert(0, '')
    nonAttackingPair = 0
    #['',2,4,7,4,8,5,5,2]
    
    #Calculate the number of non attacking pair  
    
    column = 1
    while(column < 9):
        for row in board:
            if(row == ''):
                continue
            if(board[column]!=row and (abs(board[column] - row) != abs(column - board.index(row)))):
                nonAttackingPair += 1
        column += 1
            
    return int(nonAttackingPair/2)
 


def geneticAlgorithm():
    board = [2,4,7,4,8,5,5,2]
    print("Fitness: ", fitness(board)) #Fitness: 24
    
    
geneticAlgorithm()
