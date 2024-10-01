import matplotlib.pyplot as plt
import random
import numpy as np


def holder_table_function(x):
    """The holder_table_function."""
    return -1*abs((np.sin(x[0]))*(np.cos(x[1]))*(np.exp(abs(1-(np.sqrt((x[0]*x[0])+(x[1]*x[1]))/np.pi)))))

def gen_random(i,population_size):
    while(True):
        x=random.randint(0,population_size-1)
        if(x!=i):
            return x


population_size_set=[20,50,100,200]
generation_set=[50,100,200]
Cr=0.8 # crossover probability
k=0.5

for generation in generation_set:
    for population_size in population_size_set:
        population=np.random.uniform(-10, 10, (population_size, 2))
        
        avg=[]
        mini=[]

        for g in range(generation):
            f=random.uniform(-2,2)# (between -2 to 2)
            new_population=[]
            crossover=[]
            for i in range(population_size):
                while(True):
                    #Step1: generate mutant vector
                    mutant=[]
                    r1=population[gen_random(i,population_size)]
                    r2=population[gen_random(i,population_size)]
                    r3=population[gen_random(i,population_size)]

                    mutant.append(population[i][0]+k*(r1[0]-population[i][0])+f*(r2[0]-r3[0]))
                    mutant.append(population[i][1]+k*(r1[1]-population[i][1])+f*(r2[1]-r3[1]))

                    trial_vec=[]
                    #Step2: Crossover
                    # generate trial vector
                    # j is different for x and y
                    j=random.random()
                    if(j<=Cr):
                        trial_vec.append(mutant[0])
                    else:
                        trial_vec.append(population[i][0])

                    j=random.random()
                    if(j<=Cr):
                        trial_vec.append(mutant[1])
                    else:
                        trial_vec.append(population[i][1])

                    #Constraint Check
                    if(-10<=trial_vec[0] and trial_vec[0]<=10 and -10<=trial_vec[1] and trial_vec[1]<=10):
                    #Step3: Selection
                        if(holder_table_function(trial_vec)<=holder_table_function(population[i])):
                            new_population.append(trial_vec)
                        else:
                            new_population.append(population[i])
                        break

            
            population=list(new_population)
            fitness = np.array([holder_table_function(x) for x in population])
            avg.append(np.average(fitness))
            mini.append(np.min(fitness))


        x=np.arange(0, generation)
        plt.plot(x,mini,color='blue', linestyle='-', label="Global Minimum")
        plt.plot(x,avg,color='red', linestyle='-', label="Average")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title('Holder Table Function | Population= '+str(population_size)+' | Generations= '+str(generation)+' | Global Minimum= '+str(np.min(mini)),fontsize=8)
        plt.savefig("Holder Table Function-Population"+str(population_size)+"_Genereration_"+str(generation)+".png",dpi=500)
        plt.clf()
