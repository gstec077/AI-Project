import time
import random

#Graph 1
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black','Green']

states = ['1', '2', '3', '4']
neighbors = {}
neighbors['1'] = ['2', '3']
neighbors['2'] = ['1', '3', '4']
neighbors['3'] = ['1', '2', '4']
neighbors['4'] = ['2','3']

colors_of_states={}

def promising(state, color):
    #Original Graph Colouring Problem Code
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    #Original Graph Colouring Problem Code
    for color in colors:
        if promising(state, color):
            return color
        
def brightness(states):
    #The method takes a list of vertices, assigns a random level of brightness (integer between 1-10)
    #and reorders the vertices based on the level of brightness highest-lowest. It returns a list of the key values
    #in order of their brightness value.
        x = []
        for state in states:
            x.append(state)
            num = random.randint(1,10)
            x.append(num)
        lst = {x[i]: x[i+1] for i in range(0, len(x), 2)}
        lst_sort = dict(sorted(lst.items(), key = lambda kv:(kv[1],kv[0]), reverse = True))
        return lst_sort.keys()

def main():
    print("Graph 1 Results:")
    start = time.time() #Starts the timer to determine how long the algorithm takes
    FFA = brightness(states) #Applies the brightness levels to the vertices
    for state in FFA: #Colours each vertice in order of the level of brightness
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states, "\n")
    stop = time.time() #Stops the timer
    
    duration = stop - start #Determines how long it took to solve the solution
    print("The time it took to solve the solution:", str(duration),'\n')


main()


###########################################################################

#Graph 2
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black','Green']

states = ['1','2','3','4','5','6','7','8']
neighbors = {}
neighbors['1'] = ['2', '3', '5']
neighbors['2'] = ['1', '6', '5']
neighbors['3'] = ['1', '4', '5','6']
neighbors['4'] = ['3', '6','8']
neighbors['5'] = ['2', '3', '1','7']
neighbors['6'] = ['2', '3', '4','8']
neighbors['7'] = ['5', '8',]
neighbors['8'] = ['7','6','4']

colors_of_states={}

def promising(state, color):
    #Original Graph Colouring Problem Code
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    #Original Graph Colouring Problem Code
    for color in colors:
        if promising(state, color):
            return color
        
def brightness(states):
    #The method takes a list of vertices, assigns a random level of brightness (integer between 1-10)
    #and reorders the vertices based on the level of brightness highest-lowest. It returns a list of the key values
    #in order of their brightness value.
        x = []
        for state in states:
            x.append(state)
            num = random.randint(1,10)
            x.append(num)
        lst = {x[i]: x[i+1] for i in range(0, len(x), 2)}
        lst_sort = dict(sorted(lst.items(), key = lambda kv:(kv[1],kv[0]), reverse = True))
        return lst_sort.keys()

def main2():
    print("Graph 2 Results:")
    start = time.time() #Starts the timer to determine how long the algorithm takes
    FFA = brightness(states) #Applies the brightness levels to the vertices
    for state in FFA: #Colours each vertice in order of the level of brightness
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states, "\n")
    stop = time.time() #Stops the timer
    
    duration = stop - start #Determines how long it took to solve the solution
    print("The time it took to solve the solution:", str(duration),'\n')


main2()


#################################################################################


#Graph 3
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black','Green']

states = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
neighbors = {}
neighbors['1'] = ['6', '3', '2']
neighbors['2'] = ['1', '4', '10']
neighbors['3'] = ['1', '6', '4','5']
neighbors['4'] = ['3', '2','16','8','5']
neighbors['5'] = ['6','3','4','13','15','7']
neighbors['6'] = ['1','3','5']
neighbors['7'] = ['5', '9','19']
neighbors['8'] = ['4','14','11','9','12']
neighbors['9'] = ['8','12','7','18']
neighbors['10'] = ['2','16']
neighbors['11'] = ['14','8']
neighbors['12'] = ['8','17','9']
neighbors['13'] = ['5','15']
neighbors['14'] = ['16','11','8']
neighbors['15'] = ['13','5','20']
neighbors['16'] = ['10','4','14']
neighbors['17'] = ['12']
neighbors['18'] = ['9','19']
neighbors['19'] = ['20','7','18']
neighbors['20'] = ['15','19']

colors_of_states={}

def promising(state, color):
    #Original Graph Colouring Problem Code
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    #Original Graph Colouring Problem Code
    for color in colors:
        if promising(state, color):
            return color
        
def brightness(states):
    #The method takes a list of vertices, assigns a random level of brightness (integer between 1-10)
    #and reorders the vertices based on the level of brightness highest-lowest. It returns a list of the key values
    #in order of their brightness value.
        x = []
        for state in states:
            x.append(state)
            num = random.randint(1,10)
            x.append(num)
        lst = {x[i]: x[i+1] for i in range(0, len(x), 2)}
        lst_sort = dict(sorted(lst.items(), key = lambda kv:(kv[1],kv[0]), reverse = True))
        return lst_sort.keys()

def main3():
    print("Graph 3 Results:")
    start = time.time() #Starts the timer to determine how long the algorithm takes
    FFA = brightness(states) #Applies the brightness levels to the vertices
    for state in FFA: #Colours each vertice in order of the level of brightness
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states, "\n")
    stop = time.time() #Stops the timer
    
    duration = stop - start #Determines how long it took to solve the solution
    print("The time it took to solve the solution:", str(duration),'\n')


main3()
