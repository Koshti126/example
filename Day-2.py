# #introduction to function 
# def m1 (m1):
#     print(m1+3)


# m1(5)

# def m2(m2):
#     print(m2+98)

# m2(9) 

# first_string = "i am" 

# def concate(p1, p2, p3): 
#     print(p1 + p2 +str(p3)) 
# concate(first_string," " + "boarn",  2005)
 

# def introduction_name(name):
#     print(name)
# introduction_name("krsihan") 

# #Fucntion with multiple perameters

# def self_introduction(name, age, height):
#     print(name)
#     print(int(age))
#     print(int(height))
# self_introduction("krishna", 34, 7) 

#default perameters with no argument 

# def default_pera(a=89, b=89):
#     print(a * b)
#     print(a + b)
#     print(a - b)
#     print(a / b)
#     print(a % b)
#     print(a ** b)
#     print(a // b)
# default_pera()

# def d1(a=90, b=90):
#     return a * b 
# d1() 

# function with no parameters exercise

#1   
# Create a function called hello_world_printer()  
# which takes no parameters and prints the string "hello world" 

# def hello_world():
#     print("hello world")
# hello_world()
          
# #   function with 1 parameter exercise 
# #  Create a function called name_printer which takes 1 parameter and prints it
 
# def name_printer(name):
#     print(name)
# name_printer("krihsna") 
 

# #  Create a variable called name and assign it user input().   
# # input()'s message should ask the user to enter their name.
# name = input("please enter your name:-")
# def user_name():
#     print("your name is ", name)   
# user_name()  
          
#volum of rectange
# v=L*W*H 
# L = int(input("enter the length:"))
# W = int(input("enter the width:"))
# H = int(input("enter the height:")) 
# V = (L*W*H)
# def volum_of_rectangel(L,W,H):
#     print("The volum of rectange is the ",V)
# volum_of_rectangel(L,W,H) 

#convert the fehrenheit to celsius

# celsius = int(input("enter the value"))
# F = 1.8 * celsius + 32 
# def converter():
#     print("converting the value of the celsius:",F)
# converter() 
 
# def exploration(name="krishna", age=23, status="single"):
#     print("your name is ",name)
#     print("your age is ",age)
#     print("your status is ",status)
# exploration() 

#user define function with no argument and no perameters

# n1 = int(input("Enter the first number")) 
# n2 = int(input("Enter the secound number"))
# n3 = int(input("Enter the third number"))
# n4 = int(input("Enter the fourth number"))
# n5 = int(input("Enter the fifth number"))  
# avg = (n1+n2+n3+n4+n5)/5
# def calculation():
#     print(avg)
# calculation()
    
# import module 
# import random 
# print(random.randint(1,120)) 
# print(random.randint(121,200))  

#function import

# from random import randint 
# print(randint(1,20))
# from random import * 
# print(random()) 


# flow control 
#Comparision operator
# print(34<90)
# print(89<45)
# print(1<2)
# print(1>2)
# print(1!=3)
# print(1==3)
# print(1<=2)
# print(2>=4)
