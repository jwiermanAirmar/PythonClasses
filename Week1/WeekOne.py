# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:02:41 2022

@author: jwierman
"""

#print("Hello World!")

"""

This is a docstring

"""
import random

#variables
value_one = 3    #int
value_two = 1.1  #float
str_val = "josh" #string 


string_one = "This is a test "
string_two ="of the emergency broadcast system "

#Functions
def multiply(first_value, second_value):
    """This is how we do the documentatin for hovering"""
    
    result = first_value * second_value
    print(result)
    
def divide(first_value, second_value):
    
    result = first_value / second_value
    print(result)
    
    
def random_num(start_num, stop_num):
    
    new_num = random.randint(start_num, stop_num)
    return new_num
    
def num_6D_rolls(num_rolls):
    
    for dice_count in range(num_rolls):
      
        
        print(random_num(1, 6))
        
       # new_list = ["a", 1, 9.8]# we can mismatch data types

def append_rolls(num_rolls):
    
    rolls = []
    
    for dice_count in range(num_rolls):
        
        rolls.append(random_num(1, 6))
    print (rolls)
    return rolls
       
def tryList():

      new_list = ["a", 1, 9.8]# we can mismatch data types
      print (new_list)
      
      for value in new_list:
          print(value)
          
          
def print_sixes(rolls):
    
    for roll in rolls:
        if roll == 6:
            print("six!")
            
        else:
           
           print ("not six")
#main    
#multiply(value_one, value_two)
#divide(value_one, value_two)
#print (string_one + "\n" + string_two)
#random_num(1, 6)

#append_rolls(10)
print_sixes(append_rolls(10))

#tryList()

#print (r"some_string") # this will show the chars displayed