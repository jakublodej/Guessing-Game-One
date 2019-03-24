
# coding: utf-8

# In[1]:


import random
a= int(random.randint(1,9))
print(a)
question=int(input('What number do i have ? Guess from 1 to 9 : '))
if question == a :
    print ('That is ok !')    
if question != a :
    count = 1
    while (question > a):
        count += 1
        question = int(input('Type the lower number: '))   
    while (question < a):
        count += 1
        question = int(input('Type the higher number: '))
    if question == a:
        print('Congrats. You have guessed the number using %d guesses'%count)

