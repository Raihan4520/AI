def DFS(adjList, start, goal):
    frontier = [start]
    exploredSet = []
    parent = {start : ''}
    
    print("Searching Sequence: ", end='')
    while True:
        if len(frontier) == 0:
            print("No Solution")
            return
        
        node = frontier.pop() # For DFS (Maintaining Stack)
        #node = frontier.pop(0) # For BFS (Maintaining Queue)
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
            
            return
        
        exploredSet.append(node)
        
        for adjNode in adjList[node]:
            if adjNode not in frontier and adjNode not in exploredSet:
                frontier.append(adjNode)
                parent[adjNode] = node
    
    #return


adjacencyList = {'A': ['B', 'C'],
                 'B': ['A', 'C', 'D'],
                 'C': ['A','B','D','E'],
                 'D': ['B','C','E','F'],
                 'E': ['C','D'],
                 'F': ['D']}


DFS(adjacencyList, 'A', 'F')


#print(adjacencyList['E'])
