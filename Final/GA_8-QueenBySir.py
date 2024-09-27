import random


def fitness(board):
    nonAttackingPair = 0
    for c1 in range(1,9):
        for c2 in range(1,9):
            if c1==c2:
                continue
            
            if board[c1]!=board[c2] and abs(board[c1]-board[c2])!=abs(c1-c2):
                nonAttackingPair=nonAttackingPair+1
    
    return nonAttackingPair/2
                

def printPopulation(population):
    for row in population:
        print(row)
        #print(fitness(row))

    
    
def eightQueenGA(intialPopulation, survivalRate, mutationRate, numberOfGeneration):
    #board = ['',3,2,7,5,2,4,1,1]
    #print(fitness(board))
    
    population = []
    for i in range(0,intialPopulation):
        board = random.sample([1,2,3,4,5,6,7,8],k=8)
        board.insert(0, '')
        population.append(board)
        
    printPopulation(population)
eightQueenGA(100, 70, 50, 500)

