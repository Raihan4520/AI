import random
import copy


def fitness(board):
    nonAttackingPair = 0
    for c1 in range(1,9):
        for c2 in range(1,9):
            if c1==c2:
                continue
            
            if board[c1]!=board[c2] and abs(board[c1]-board[c2])!=abs(c1-c2):
                nonAttackingPair=nonAttackingPair+1
    
    return nonAttackingPair/2
                

    
def selection(population, survivalRate):
    
    fitnessList = []
    for b in population:
        fitnessList.append(fitness(b))
        
    
    for i in range(0,int(len(population)*survivalRate/100)):
        maxIndex = i
        for j in range(i+1,len(population)):
            if fitnessList[j]>fitnessList[maxIndex]:
                maxIndex = j
                
        temp = population[i]
        population[i]=population[maxIndex]
        population[maxIndex]=temp
        
        temp= fitnessList[i]
        fitnessList[i]=fitnessList[maxIndex]
        fitnessList[maxIndex] = temp
    
    return population[0:int(len(population)*survivalRate/100)]


def crossOver(population):
    
    for i in range(0,len(population),2):
        cp = random.randint(2, 7)
        print("Pair")
        print(population[i])
        print(population[i+1])
        print('Crossover Point: ',cp)
        temp = population[i][cp:]
        population[i][cp:]=population[i+1][cp:]
        population[i+1][cp:]=temp
  
    return population

def printPopulation(population):
    for row in population:
        print(row)
        #print(fitness(row))
        
        
def mutation(population, mutationRate):
    #Implement this function only
    #print(mutationRate)
    #print(len(population))
    randomPopulationList = random.sample(range(len(population)), int(len(population) * (mutationRate/100)))
    #print(randomPopulationList)
    for i in randomPopulationList:
        population[i][random.randint(1,8)] = random.randint(1,8)
    return population
        
def eightQueenGA(intialPopulation, survivalRate, mutationRate, numberOfGeneration):
    
    population = []
    for i in range(0,intialPopulation):
        board = random.sample([1,2,3,4,5,6,7,8],k=8)
        board.insert(0, '')
        population.append(board)
        
    printPopulation(population)
    print(len(population))
    population = selection(population, survivalRate)
    print("****** New Population ******")
    population = random.sample(population, len(population))
    population.extend(copy.deepcopy(random.sample(population, len(population)-int(len(population)*survivalRate/100))))
    printPopulation(population)
    print(len(population))
    
    
    population = crossOver(population)
    print("***** After Crossover ******")
    printPopulation(population)
    population = mutation(population, mutationRate)
    print('***** After Mutation ******')
    printPopulation(population)
    
eightQueenGA(10, 70, 50, 500)





