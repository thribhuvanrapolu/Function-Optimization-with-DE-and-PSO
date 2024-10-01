import matplotlib.pyplot as plt
import random
import numpy as np


def eggholder_function(k):
    """The eggholder_function function."""
    x=k[0]
    y=k[1]
    return -(y + 47) * np.sin(np.sqrt(abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(abs(x - (y + 47))))


particle_size_set=[20,50,100,200]
iteration_set=[50,100,200]

c1=2
c2=2 # crossover probability c1+c2=4
k=0.5

for iterations in iteration_set:
    for particle_size in particle_size_set:
        f=random.uniform(-2,2)# (between -2 to 2)
        
        particles=np.random.uniform(-512, 512, (particle_size, 2))
        global_best_arr = []
        global_best=particles[np.argmin(eggholder_function(particles))]

        local_best = list(particles)

        
        for i in range(iterations):
            new_particles=[]
            for i in range(particle_size):
                temp=0
                # print(i)

                while(temp<20):
                    #Step1: generate velocity
                    velocity=[]
                    r1=random.random()
                    r2=random.random()

                    velocity.append(particles[i][0]+c1*(r1)*(local_best[i][0]-particles[i][0])+c2*(r2)*(global_best[0]-particles[i][0]))
                    velocity.append(particles[i][1]+c1*(r1)*(local_best[i][1]-particles[i][1])+c2*(r2)*(global_best[1]-particles[i][1]))

                    #Step2: Generate new particle
                    new_particle=[]
                    new_particle.append(particles[i][0]+velocity[0])
                    new_particle.append(particles[i][1]+velocity[1])
                    # print(r1,r2,velocity,new_particle)
                    if(-512<=new_particle[0] and new_particle[0]<=512 and -512<=new_particle[1] and new_particle[1]<=512):
                        new_particles.append(particles[i]+velocity)
                        if(eggholder_function(local_best[i])>eggholder_function(new_particles[i])):
                            local_best[i]=new_particles[i]

                        if(eggholder_function(global_best)>eggholder_function(new_particles[i])):
                            global_best=new_particles[i]
                        
                        break
                    temp+=1
                if(temp>=20):
                    new_particles.append(particles[i])


            global_best_arr.append(global_best)

            particles=list(new_particles)

        # print(global_best_arr)
        x=np.arange(0, iterations)
        plt.plot(x,np.array([eggholder_function(x) for x in global_best_arr]),color='blue', linestyle='-', label="Global Minimum")
        plt.xlabel("Iteration")
        plt.ylabel("Global Best Minimum")
        plt.title('Eggholder Function | Population= '+str(particle_size)+' | Iterations= '+str(iterations)+' | Global Minimum= '+str(eggholder_function(global_best)),fontsize=8)
        plt.savefig("Eggholder Function-Population"+str(particle_size)+"_Iterations_"+str(iterations)+".png",dpi=500)
        plt.clf()
