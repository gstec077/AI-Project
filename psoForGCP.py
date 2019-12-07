import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time

# Note that the majority of this code was NOT written by me. I modified it to be able to input a graph for the
# Particle Swarm Optimization algorithm


colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black','Green'] # Colours used to assign to the graph
target_error=1e-6 # target error for PSO
W= 0.5 # weight value
c1=0.8 # Constant 1
c2=0.9 # Constant 2

# For Graph 1 

states = ['1', '2', '3', '4'] # Nodes for graph 1
neighbors = {} # listing all the neighbours below
neighbors['1'] = ['2', '3']
neighbors['2'] = ['1', '3', '4']
neighbors['3'] = ['1', '2', '4']
neighbors['4'] = ['2','3']
    

n_particles=4


graph_colouring={} # Final tuple with colours assigned to each node

colors_of_states = {}


class Particle(): # Particle clas fore graph 1 
    
    def __init__(self,states):
        self.position=states
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])
       

    def __str__(self):
        for i in range(len(self.position)):            
            #print("I am at ", self.position[i], " meu pbest is ", self.pbest_position[i])        
            graph_colouring[self.position[i]] = self.get_color_for_state(self.position[i])

        print (graph_colouring)
    
    def move(self):
        self.position = self.position + self.velocity


      
    def promising(self,state, color):
        for neighbor in neighbors.get(state): 
            color_of_neighbor = graph_colouring.get(neighbor)
            if color_of_neighbor == color:
                return False

        return True

    def get_color_for_state(self,state):     
        
        for color in colors:
            if self.promising(state, color):               
                return color

                        
class Space(): # Space class for graph 1

    def __init__(self, target, target_error, states):
        self.target = target
        self.target_error = target_error
        self.states=states
        self.particles = states
        self.gbest_value = float('inf')
   
        self.gbest_position=np.array([self.particles ,self.particles ])
        
    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
            

    print (colors_of_states)

    def fitness(self, particle):
        for i in range(len(states)):
            if particle.position==states[i]:
                return particle.position[i+1]
        #return particle.position[len(particle.position)-1]
        #return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

  

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for i in range(len(self.particles)):
                       
       
            global W
            new_velocity = (W*particle.velocity) + (c1) * (particle.pbest_position[i] - particle.position) + \
                            (c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()




def main():   # printing graph 1
    print("Graph 1 Results",'\n')
    start= time.time()

    search_space = Space(1, target_error, states)
    particles_vector = [Particle(search_space.states)]
    search_space.particles = particles_vector
    search_space.print_particles()
    stop= time.time()
    
    duration= stop-start
    print(" ")
    print("The time to solve the solution is: "+str(duration))   





############################################################################################################################################

# For Graph 2

states2 = ['1','2','3','4','5','6','7','8'] # Graph 2 nodes
neighbors2 = {} # Listing each neighbours below
neighbors2['1'] = ['2', '3', '5']
neighbors2['2'] = ['1', '6', '5']
neighbors2['3'] = ['1', '4', '5','6']
neighbors2['4'] = ['3', '6','8']
neighbors2['5'] = ['2', '3', '1','7']
neighbors2['6'] = ['2', '3', '4','8']
neighbors2['7'] = ['5', '8',]
neighbors2['8'] = ['7','6','4']


graph_colouring2={} # Final tuple with a colour assigned to each node

colors_of_states2 = {}
n_particles2=8


class Particle2(): # Particle class for graph 2
    
    def __init__(self,states):
        self.position=states
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])
       

    def __str__(self):
        for i in range(len(self.position)):            
            #print("I am at ", self.position[i], " meu pbest is ", self.pbest_position[i])        
            graph_colouring2[self.position[i]] = self.get_color_for_state(self.position[i])

        print (graph_colouring2)
    
    def move(self):
        self.position = self.position + self.velocity


      
    def promising(self,state, color):
        for neighbor in neighbors2.get(state): 
            color_of_neighbor = graph_colouring.get(neighbor)
            if color_of_neighbor == color:
                return False

        return True

    def get_color_for_state(self,state):     
        
        for color in colors:
            if self.promising(state, color):               
                return color

                        
class Space2(): # Space class for graph 2 

    def __init__(self, target, target_error, states):
        self.target = target
        self.target_error = target_error
        self.states=states
        self.particles = states
        self.gbest_value = float('inf')
   
        self.gbest_position=np.array([self.particles ,self.particles ])
        
    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
            

    print (colors_of_states2)

    def fitness(self, particle):
        for i in range(len(states)):
            if particle.position==states[i]:
                return particle.position[i+1]
        #return particle.position[len(particle.position)-1]
        #return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

  

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for i in range(len(self.particles)):
                       
       
            global W
            new_velocity = (W*particle.velocity) + (c1) * (particle.pbest_position[i] - particle.position) + \
                            (c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()




def main2(): # printing graph 2
    print("Graph 2 Results",'\n')

    start= time.time()

    search_space = Space2(1, target_error, states2)
    particles_vector = [Particle2(search_space.states)]
    search_space.particles = particles_vector
    search_space.print_particles()
    stop= time.time()
    
    duration= stop-start
    print(" ")
    print("The time to solve the solution is: "+str(duration))





####################################################################################################################################

# For Graph 3

states3 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'] # graph 3 nodes
neighbors3 = {} # Listing all the neighbours below
neighbors3['1'] = ['6', '3', '2']
neighbors3['2'] = ['1', '4', '10']
neighbors3['3'] = ['1', '6', '4','5']
neighbors3['4'] = ['3', '2','16','8','5']
neighbors3['5'] = ['6','3','4','13','15','7']
neighbors3['6'] = ['1','3','5']
neighbors3['7'] = ['5', '9','19']
neighbors3['8'] = ['4','14','11','9','12']
neighbors3['9'] = ['8','12','7','18']
neighbors3['10'] = ['2','16']
neighbors3['11'] = ['14','8']
neighbors3['12'] = ['8','17','9']
neighbors3['13'] = ['5','15']
neighbors3['14'] = ['16','11','8']
neighbors3['15'] = ['13','5','20']
neighbors3['16'] = ['10','4','14']
neighbors3['17'] = ['12']
neighbors3['18'] = ['9','19']
neighbors3['19'] = ['20','7','18']
neighbors3['20'] = ['15','19']
graph_colouring3={} # Final tuple with a colour assigned to a node
colors_of_states3 = {}
n_particles3=20

class Particle3(): # Particle clas for graph 3 
    
    def __init__(self,states):
        self.position=states
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0])
       

    def __str__(self):
        for i in range(len(self.position)):            
            #print("I am at ", self.position[i], " meu pbest is ", self.pbest_position[i])        
            graph_colouring3[self.position[i]] = self.get_color_for_state(self.position[i])

        print (graph_colouring3)
    
    def move(self):
        self.position = self.position + self.velocity


      
    def promising(self,state, color):
        for neighbor in neighbors3.get(state): 
            color_of_neighbor = graph_colouring.get(neighbor)
            if color_of_neighbor == color:
                return False

        return True

    def get_color_for_state(self,state):     
        
        for color in colors:
            if self.promising(state, color):               
                return color

                        
class Space3():

    def __init__(self, target, target_error, states):
        self.target = target
        self.target_error = target_error
        self.states=states
        self.particles = states
        self.gbest_value = float('inf')
   
        self.gbest_position=np.array([self.particles ,self.particles ])
        
    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
            

    print (colors_of_states3)

    def fitness(self, particle):
        for i in range(len(states)):
            if particle.position==states[i]:
                return particle.position[i+1]
        #return particle.position[len(particle.position)-1]
        #return particle.position[0] ** 2 + particle.position[1] ** 2 + 1

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

  

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for i in range(len(self.particles)):
                       
       
            global W
            new_velocity = (W*particle.velocity) + (c1) * (particle.pbest_position[i] - particle.position) + \
                            (c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()




def main3():   #printing graph 3 
    print("Graph 3 Resultts",'\n')
    start= time.time()

    search_space = Space3(1, target_error, states3)
    particles_vector = [Particle3(search_space.states)]
    search_space.particles = particles_vector
    search_space.print_particles()
    stop= time.time()
    
    duration= stop-start
    print(" ")
    print("The time to solve the solution is: "+str(duration))   
    


main()
print(" ")
main2()
print(" ")
main3()





















