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
    
    
# -Create a new Population...
# this is pop list : [[2, 2, 4, 4, 0], [2, 2, 1, 4, 0], [2, 3, 3, 2, 0], [3, 2, 1, 1, 0]]  
# this is population : [[2, 2, 4, 4, 0], [2, 2, 1, 4, 0], [2, 3, 3, 2, 0], [3, 2, 1, 1, 0]]
    
    

#2.CROSS OVER
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
        
        pop_list.append(child1)
        pop_list.append(child2)
        
        print("="*50)
        # we add children to  population list , the population increases !
        
# -CROSS OVER...
# child1 [2, 2, 1, 4, 0]
# child2 [2, 2, 4, 4, 0]
# ==================================================
# child1 [2, 3, 1, 1, 0]
# child2 [3, 2, 3, 2, 0]      

    print("Total amount of people is : ",pop_list)
# Total amount of people is :  [[2, 2, 4, 4, 0], [2, 2, 1, 4, 0], [2, 3, 3, 2, 0], [3, 2, 1, 1, 0], [2, 2, 1, 4, 0], [2, 2, 4, 4, 0], [2, 3, 1, 1, 0], [3, 2, 3, 2, 0]]





    print("Mutaion: ")
# 3. Mutation Part
    m_r = 0.8   # Mutation Rate 
    choosen_ones = [i for i in range(len(pop_list)//2)] # from only children part
    for i in range(len(pop_list)//2):
        new_element = 1
        choosen_ones[new_element],choosen_ones[i] = choosen_ones[i] ,choosen_ones[new_element]
    # print("choosen ones are  :" , choosen_ones)
    choosen_ones = choosen_ones[:int(len(choosen_ones)*m_r)]
    
    for i in choosen_ones:
        new_ch = rnd.randint(0,n-1)
        # new_value = rnd.randint(1,n)
        new_value = 5
        pop_list[i][new_ch] = new_value
        if pop_list[0][n] == 0:
            print("best Future Children  , " , pop_list[0][0:n])
    print(pop_list) 

# 4. choose the best child (a child having all attribute is the best option , here is the condition )
    i = 0
    length = len(pop_list)
    conflict = 0 
    while i < length:
        j = 0 
        conflict = 0 
        while j < n:
            l = j +1
            while l<n:
                if pop_list[i][j] == pop_list[i][l]:
                    conflict+=1
                if abs(j-l) ==abs(pop_list[i][j] - pop_list[i][l]): 
                    conflict+=1
                l+=1
            j+=l
        pop_list[i][len(pop_list[j])-1] = conflict
        i+=1
          
    for i in range(len(pop_list)):
        _min = i
        for j in range(i, len(pop_list)):
            if pop_list[j][n] < pop_list[_min][n]:
                _min = j
        pop_list, pop_list[_min] = pop_list[_min] , pop_list[i]   
    print("this is the best child " , pop_list)















# Driver code to test above method
init_pop(pop, n )



