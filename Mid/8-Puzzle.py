import random
import copy


def initialStateGenarator():
    elements = [1, 2, 3, 4, 5, 6, 7, 8, '']
    elements = random.sample(elements, 9)
    #print(elements)
    #initialBoard = [[elements[0], elements[1], elements[2]],
    #                [elements[3], elements[4], elements[5]],
    #                [elements[6], elements[7], elements[8]]]          
    
    #List slicing (listName[start:end] always ends at end-1)
    initialBoard = [elements[:3],
                    elements[3:6],
                    elements[6:]]
    
    return initialBoard


def actions(state):
    setOfAction = ['u', 'd', 'l', 'r']
    for row in range(3):
        for col in range(3):
            if state[row][col] == '':
                #if row == 0 and col == 0:
                #    setOfAction = ['u', 'l']
                #elif row == 0 and col == 1:
                #    setOfAction = ['u', 'l', 'r']
                #elif row == 0 and col == 2:
                #    setOfAction = ['u', 'r']
                #elif row == 1 and col == 0:
                #    setOfAction = ['u', 'd', 'l']
                #elif row == 1 and col == 1:
                #    setOfAction = ['u', 'd', 'l', 'r']
                #elif row == 1 and col == 2:
                #    setOfAction = ['u', 'd', 'r']
                #elif row == 2 and col == 0:
                #    setOfAction = ['d', 'l']
                #elif row == 2 and col == 1:
                #    setOfAction = ['d', 'l', 'r']
                #elif row == 2 and col == 2:
                #    setOfAction = ['d', 'r']
                
                # Easier and fewer logics
                if row == 0:
                    setOfAction.remove('d')
                if col == 0:
                    setOfAction.remove('r')
                if row == 2:
                    setOfAction.remove('u')
                if col == 2:
                    setOfAction.remove('l')
                
                return setOfAction
    

# By default in python: List is transfered to a function by reference
def transitions(state, action):
    #lst = state (It does not copy it sents reference)
    #lst.copy() (It works on one dimentional list only)
    resultantState = copy.deepcopy(state) #Used to copy multi-dimentional list
    for row in range(3):
        for col in range(3):
            if resultantState[row][col] == '':
                if action == 'u':
                    resultantState[row][col] = resultantState[row+1][col]
                    resultantState[row+1][col] = ''
                elif action == 'd':
                    resultantState[row][col] = resultantState[row-1][col]
                    resultantState[row-1][col] = ''
                elif action == 'l':
                    resultantState[row][col] = resultantState[row][col+1]
                    resultantState[row][col+1] = ''
                elif action == 'r':
                    resultantState[row][col] = resultantState[row][col-1]
                    resultantState[row][col-1] = ''
                
                return resultantState



def goalTest(state): 

    return True

def printState(state):
    for row in state:
        print(row)

def eight_puzzle_solver():
    initialState = initialStateGenarator()
    printState(initialState)
    actionSet = actions(initialState)
    print("Possible Actions: ",actionSet)
    #print("Resultant State")
    #printState(transitions(initialState, actionSet[0]))
    #print(goalTest(initialState))
    



eight_puzzle_solver()


