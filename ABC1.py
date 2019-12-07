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



class beeColony():
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

    def __init__(self, states):
        
        for state in states:
            set(state)
            
    def set(state): 
        d=calculatefitness(state)    
        fitness[state]= d
        calculatefitness(state)
        fitness_and_state.append([d, state])
        

    def calculateFitness(state): # im finding the fitness of a node based on 
                                 # the Degree of it so how many neighbours
        h = 0
        for nieghbor in neighbors.get(state): # this calculates the fitness for 
            h+1                               # the problem im tryna solve
       # numpy.append(color_and_fitness, [state, i])  
        return h
        
    def sortSecond(val): #code from https://www.geeksforgeeks.org/python-list-sort/
        return val[1]       # used to help sort an arrayed list
    
    def memorizeBestSource(): # this should hold the highest number at all time
                              # or it should hold from the node the least amount
                              # colors it hasn't taken to colour from this point
        
        #fitness.sort(reverse =True) # s
        fitness_and_state.sort(key =sortSecond, reverse =True) #orders the list from most nodes to least 
        

    def sendEmployedBees(state): # generate a random number from 0 to the # of states

        colors_of_states[state] = colors_of_states.get(state)
        fitness[state] = 0      # making the fitness now 0 so that if it selected in
                                # the future it will already have been assigned a color


    def calculateProbilities(): # find the probility that this state chosen is
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

    def sendOnlookerBees(state):
       # def get_color_for_state(state):
        for color in colors:
            if promising(state, color):
                return colors

    def sendScoutBees():
        null
        
    def get_color_for_state(state):
        for color in colors:
            if promising(state, color):
                return color
            
    def promising(state, color):
        for neighbor in neighbors.get(state): 
            color_of_neighbor = colors_of_states.get(neighbor)
            if color_of_neighbor == color:
                return False

        return True




def main():
    start=time.time()
   # for state in states:
    #    colors_of_states[state] = get_color_for_state(state)
    bees =beeColony(states) 
    bees.sendEmployedBees()
    bees.calculateProbilities()
    bees.sendOnlookerBees(state)
    bees.memorizeBestSource()
    bees.sendScoutBees()
    stop = time.time()
    duration = stop-start
    print (colors_of_states)
    print("\n","The time to solve the solution is: "+str(duration)) 



main()  


