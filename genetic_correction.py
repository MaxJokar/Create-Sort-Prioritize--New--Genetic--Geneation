"""
To find/produce/sort  genius children by producing new chromosome ,
correct their parents genetic issue 
"""
import random as rnd

# Amount of parents
pop = 4
# each have 4 Choromosome
n = 4 

#1. Produce a population with their own accident Chromosome numbers======================================
# [2, 4, 1, 3], [2, 3, 3, 1], [3, 3, 4, 4]...

def init_pop(pop,n):
    """ we produce a initial population with their accident chromosome  for each person"""
    print("="*50)
    print("-Create a new Population...")
    pop_list = []
    for i in range(1,pop+1):       
        new_member = []
        for j in range(n):
            new_member.append(rnd.randint(1,4))
        new_member.append(0) # used for filtering priority of genius children from 1 best ones ==> to 5 
        pop_list.append(new_member)  
    
    print("this is pop list :",pop_list)
    population = pop_list
    print("this is population :",population )
    
    

    

#2.CROSS OVER
def corss_over(pop_list):
    # Amount of parents
    pop_list = 4
    # each have 4 Choromosome
    n = 4 

    print("-CROSS OVER...")
    for i in range(0,len(pop_list), 2):
        child1 = pop_list[i][:len(pop_list[0])//2] + pop_list[i+1][len(pop_list[0])//2:]    
        print("child1",child1)
        
        child2 = pop_list[i+1][:len(pop_list[0])//2] + pop_list[i][len(pop_list[0])//2:]
        print("child2",child2)   
        
        pop_list.append(child1)
        pop_list.append(child2)
        
        print("="*50)
        # we add children to  population list , the population increases !
    return pop_list


# 3. Mutation Part
m_r = 0.8   # Mutation Rate 
def mutation(pop_list , mutation_rate): 
    choosen_ones = [i for i in range(len(pop_list)//2)] # from only children part
    for i in range(len(pop_list)//2):
        new_element = 2
        choosen_ones[new_element],choosen_ones[i] = choosen_ones[i] ,choosen_ones[new_element]
    choosen_ones = choosen_ones[:int(len(choosen_ones)*mutation_rate)]    
    # print("choosen ones are  :" , choosen_ones)
    for i in choosen_ones:
        new_ch = rnd.randint(0,n-1)
        # new_value = rnd.randint(1,n)
        new_value = 5
        pop_list[i][new_ch] = new_value
    return pop_list










population= init_pop(pop, n )
population = corss_over(population)
population = mutation(population)