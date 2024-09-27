import math
def A_Star_Search(adjList, heuValue, start, goal):
    frontier = [start]
    exploredSet = []
    parent = {start : ''}
    pathCost = {start:0}
    
    print("Searching Sequence: ", end='')
    while True:
        if len(frontier) == 0:
            print("No Solution")
            return
        
        #***************************************************************
        #Find the minimum node from the frontier
        node=''
        minValue = math.inf
        for item in frontier:
            if pathCost[item] + heuValue[item] < minValue:
                minValue=pathCost[item] + heuValue[item]
                node = item
        
        #Remove the minimum node from the frontier
        frontier.remove(node)
        #***************************************************************
        
        print(node, end="-->")
        
        if node == goal:
            print()
            print("Goal Found")
            print("Solution Sequence: ", end='')
            sol = []
            n = goal
            while n!='':
                sol.append(n)
                #print(n, end="<--")
                n = parent[n]
            
            while len(sol) != 0:
                print(sol.pop(), end="-->")
            
            print("\nPath cost = ", pathCost[goal])
            return
        
        exploredSet.append(node)
        
        #***************************************************************
        #At first:
        #adjList['A'] --> [('B',3), ('J',4), ('G',1)]
        #adjNode, weight = ('B',3) #Unpacking of tuple
        for adjNode, weight in adjList[node]:
            if adjNode not in frontier and adjNode not in exploredSet:
                frontier.append(adjNode)
                parent[adjNode] = node
                pathCost[adjNode] = pathCost[node] + weight
            elif adjNode in frontier:
                if pathCost[adjNode]>pathCost[node] + weight:
                    parent[adjNode] = node
                    pathCost[adjNode] = pathCost[node] + weight
        #***************************************************************
    
    #return

'''
adjacencyList = {'A': ['B', 'C'],
                 'B': ['A', 'C', 'D'],
                 'C': ['A','B','D','E'],
                 'D': ['B','C','E','F'],
                 'E': ['C','D'],
                 'F': ['D']}
'''

adjacencyList = {'A':[('B',3),('J',4),('G',1)],
                 'B':[('A',3),('D',10)],
                 'C':[('H',3)],
                 'D':[('B',10),('J',3),('H',11)],
                 'E':[('G',14),('F',2), ('I',1)],
                 'F':[('E',2),('G',8),('H',4),('I',2)],
                 'G':[('A',1),('J',6),('F',8),('E',14)],
                 'H':[('C',3),('F',4),('I',6),('D',11)],
                 'I':[('E',1),('F',2),('H',6)],
                 'J':[('A',4),('D',3),('G',6)]}

heuristicValue = {'A':12, 'B':10, 'C':0, 'D':6, 'E':8, 'F':5, 'G':9, 'H':3, 'I':4, 'J':8}


A_Star_Search(adjacencyList, heuristicValue, 'A', 'C')


#print(adjacencyList['E'])
