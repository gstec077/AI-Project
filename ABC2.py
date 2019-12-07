from random import seed
from random import random
import numpy
import time

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']

states = ['1', '2', '3', '4']

neighbors = {}
neighbors['1'] = ['2', '3']
neighbors['2'] = ['1', '3', '4']
neighbors['3'] = ['1', '2', '4']
neighbors['4'] = ['2','3']

colors_of_states = {}

#color_and_fitness=numpy.empty((range(states),2))

fitness_and_state = {}
fitness = {}

    #code sampled from a java implementation of ABC
    #control parameters of ABC algorithm
np = 20 #len(states) # 20 # the number of the colony size (employed bees + onlooker bees
            # might need to have this to be changed based on the nodes that
            # are given into the problem
foodNumber = np/2 # the number of food sources, it equals half of
                      # the colony size
limit = 100 # if a food source can't be improved by this limit we abandon
maxCycle = 2500 # the number of cycles the bee can make

#problem specific variables
D = 100 # the number of parameters of the problem to be optimized
lb = -5.12 #lower bound of the parameters
up = 5.12 # upper bound of the parameters

runtime = 30


#fitness ={} #numpy.empty(foodNumber,1) #vector that holds values of fitness associated with food source "states"
prob = {} #numpy.empty(foodNumber,1) #vector that holds the probabilities of a food sources to be chosen

class beeColony():
    

    def __init__(self, states):
        self.states=states
        #for state in self.states:
            #self.set(state)
        
    def __str__(self):
         
        for i in range(len(self.states)):
             
            #print("I am at ", self.position[i], " meu pbest is ", self.pbest_position[i])        
            colors_of_states[self.states[i]] = self.get_color_for_state(self.states[i])

        print (colors_of_states)
            
    def set2(self,state):
        for states in state:
            
            d=self.calculateFitness(state)    
            #fitness[state]= d
            self.calculateFitness(state)
        #fitness_and_state.append([d, state])
        

    def calculateFitness(self,state): # im finding the fitness of a node based on 
                                 # the Degree of it so how many neighbours
        h = 0
        for nieghbor in neighbors: # this calculates the fitness for 
            h+1                               # the problem im tryna solve
       # numpy.append(color_and_fitness, [state, i])  
        return h
        
    def sortSecond(self,val): #code from https://www.geeksforgeeks.org/python-list-sort/
        return val[1]       # used to help sort an arrayed list
    
   # def memorizeBestSource(self): # this should hold the highest number at all time
                              # or it should hold from the node the least amount
                              # colors it hasn't taken to colour from this point
        
        #fitness.sort(reverse =True) # s
        #fitness_and_state.sort(self,key =sortSecond, reverse =True) #orders the list from most nodes to least 
        

    def sendEmployedBees(self,state): # generate a random number from 0 to the # of states

        colors_of_states[state] = colors_of_states.get(state)
        fitness[state] = 0      # making the fitness now 0 so that if it selected in
                                # the future it will already have been assigned a color


    def calculateProbilities(self): # find the probility that this state chosen is
                                # better then the ones before or not
                                # or can have this assign the colours
        maxfit = fitness[0]
        for state in states:
            if (fitness[state]>maxfit):
                maxfit = fitness[i]

       # for state in states:
        #    prob[state]=(0.9*(fitness[state]/maxfit))+0.1
            #equation taken from a java code, using it make the probabilities
            # probability is calculated using fitness                         

    def sendOnlookerBees(self,state):
       # def get_color_for_state(state):
        for color in colors:
            if self.promising(state, color):
                return colors

    #def sendScoutBees(self):
       # null
        
    def get_color_for_state(self,state):
        for color in colors:
            if self.promising(state, color):
                return color
            
    def promising(self,state, color):
        print(state)
        for states2 in states:
            for neighbor in neighbors.get(states2): 
                color_of_neighbor = colors_of_states.get(neighbor)
                if color_of_neighbor == color:
                    return False

        return True




def main():
    start=time.time()
   # for state in states:
    #    colors_of_states[state] = get_color_for_state(state)
    bees =beeColony(states)
    #graph=bees.set2(bees.states)
   # bees.sendEmployedBees(states)
    #bees.calculateProbilities()
    bees.sendOnlookerBees(states)
    bees.__str__()
    #bees.memorizeBestSource()
   # bees.sendScoutBees()
   
    stop = time.time()
    duration = stop-start
    print (colors_of_states)
    print("\n","The time to solve the solution is: "+str(duration))
   



main()  




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




def main2():
    start=time.time()
   # for state in states:
    #    colors_of_states[state] = get_color_for_state(state)
    bees =beeColony(states)
    #graph=bees.set2(bees.states)
   # bees.sendEmployedBees(states)
    #bees.calculateProbilities()
    bees.sendOnlookerBees(states)
    bees.__str__()
    #bees.memorizeBestSource()
   # bees.sendScoutBees()
   
    stop = time.time()
    duration = stop-start
    print (colors_of_states)
    print("\n","The time to solve the solution is: "+str(duration))
   



main2()




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





def main3():
    start=time.time()
   # for state in states:
    #    colors_of_states[state] = get_color_for_state(state)
    bees =beeColony(states)
    #graph=bees.set2(bees.states)
   # bees.sendEmployedBees(states)
    #bees.calculateProbilities()
    bees.sendOnlookerBees(states)
    bees.__str__()
    #bees.memorizeBestSource()
   # bees.sendScoutBees()
   
    stop = time.time()
    duration = stop-start
    print (colors_of_states)
    print("\n","The time to solve the solution is: "+str(duration))
   



main3()

