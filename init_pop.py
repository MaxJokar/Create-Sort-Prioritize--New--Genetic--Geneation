"""
To find/produce/sort  genius children by producing new chromosome ,
correct their parents genetic issue 
"""
import random as rnd

# Amount of parents
pop = 4
# each have 4 Choromosome
n = 4 

# Produce a population with their own accident Chromosome numbers
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
    
    
#================================CROSS OVER===============
#  we mix first 2 accident chromosome for   each person with another one as one  couple 
    print("="*50)
# TEST:
# To slice list 2 LAST  elements:
# print(population[0][2:]) OR
    print("-CROSS OVER...")
# print(population[0][len(population[0])//2:])
# [1, 2, 0]
# To slice 2 FIRST elements
# print(population[0][:len(population[0])//2])
# [1, 2]    


    for i in range(0,len(pop_list), 2):
        child1 = pop_list[i][:len(pop_list[0])//2] + pop_list[i+1][len(pop_list[0])//2:]    
        print("child1",child1)
        
        child2 = pop_list[i+1][:len(pop_list[0])//2] + pop_list[i][len(pop_list[0])//2:]
        print("child2",child2)   
        print("="*50)




# Driver code to test above method
# population = init_pop(pop, n )
# print("Population is :" , population)
# print()

init_pop(pop, n )