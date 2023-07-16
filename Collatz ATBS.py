#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The Collatz Sequence
#Write a function named collatz() that has one parameter named number. 
#If number is even, then collatz() should print number // 2 and return this value. 
#If number is odd, then collatz() should print and return 3 * number + 1.

#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number 
#until the function returns the value 1. 

def collatz(number):                 #defining the function
    if number % 2 == 0:              #check for even numbers
        number = (number // 2)       #then compute this expression
    else:                            #check for odd numbers
        number = (3 * number + 1)    #then compute this expression
    return number

while True:
    try:
        print('Enter number:')       #keep asking the user to prompt an integer
        number = int(input())
    except ValueError:               #check for non-integer values
        print('Integer!')
        continue
    while True:                      #call the function until it reaches the value 1, then it exits the loop
        number = collatz(number)     
        print(number)                #print every value until it outputs 1
        if number == 1:
            break
            


        
    


# In[ ]:




