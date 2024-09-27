import random

# Global variables

adj = {'WA' : ['NT', 'SA' ],
       'NT' : ['WA', 'SA' , 'Q'  ],
       'SA' : ['WA', 'NT' , 'Q'  , 'NSW', 'V'],
       'Q'  : ['NT', 'SA' , 'NSW'],
       'NSW': ['Q' , 'SA' , 'V'  ],
       'V'  : ['SA', 'NSW'],
       'T'  : []}

assignment = {}

def select_unassigned_variable():
    unassigned_var = []
    
    for node in adj:
        if node not in assignment:    
            unassigned_var.append(node)
    
    return random.choice(unassigned_var)
    

def ordered_domain_value():
    return ['R', 'G', 'B']


def value_is_consistent(variable, value):
    for adNode in adj[variable]:
        if adNode in assignment:
            if assignment[adNode] == value:
                return False
    
    return True


def recursive_backtracking():
    if len(adj) == len(assignment):
        return assignment
    var = select_unassigned_variable()
    for value in ordered_domain_value():
        if value_is_consistent(var, value):
            assignment[var] = value
            result = recursive_backtracking()
            if result != 'failure':
                return result
            del assignment[var]
            
    return 'failure'


print(recursive_backtracking())

