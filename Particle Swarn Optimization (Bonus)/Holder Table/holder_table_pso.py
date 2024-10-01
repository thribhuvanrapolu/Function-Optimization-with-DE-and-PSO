import matplotlib.pyplot as plt
import random
import numpy as np


def holder_table_function(x):
  return -1*abs((np.sin(x[0]))*(np.cos(x[1]))*(np.exp(abs(1-(np.sqrt((x[0]*x[0])+(x[1]*x[1]))/np.pi)))))


particle_size_set=[20,50,100,200]
iteration_set=[50,100,200]

c1=2
c2=2 # crossover probability c1+c2=4
k=0.5
for iterations in iteration_set:
    for particle_size in particle_size_set:
        f=random.uniform(-2,2)# (between -2 to 2)
        
        particles=np.random.uniform(-10,10, (particle_size, 2))
        global_best_arr = []
        global_best=particles[np.argmin(holder_table_function(particles))]

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
                    if(-10<=new_particle[0] and new_particle[0]<=10 and -10<=new_particle[1] and new_particle[1]<=10):
                        new_particles.append(particles[i]+velocity)
                        if(holder_table_function(local_best[i])>holder_table_function(new_particles[i])):
                            local_best[i]=new_particles[i]

                        if(holder_table_function(global_best)>holder_table_function(new_particles[i])):
                            global_best=new_particles[i]
                        
                        break
                    temp+=1
                if(temp>=20):
                    new_particles.append(particles[i])


            global_best_arr.append(global_best)

            particles=list(new_particles)

        x=np.arange(0, iterations)
        plt.plot(x,np.array([holder_table_function(x) for x in global_best_arr]),color='blue', linestyle='-', label="Global Minimum")
        plt.xlabel("Iteration")
        plt.ylabel("Global Best Minimum")
        plt.title('Holder Table Function | Population= '+str(particle_size)+' | Iterations= '+str(iterations)+' | Global Minimum= '+str(holder_table_function(global_best)),fontsize=8)
        plt.savefig("Holder Table Function-Population"+str(particle_size)+"_Iterations_"+str(iterations)+".png",dpi=500)
        plt.clf()
