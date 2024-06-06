# ## if statement
# fruit = input("enter the fruit name:")
# if fruit == "apple": 
#     print("the fruit is apple") 

## program 
# password = input("enter the password:")
# if password =="krishna@#123":
#     print("Password is correct \t\nThank You!") 
# else:
#     print("sorry! \n Try again") 

# gpa = float(input("enter the your gpa mark"))
# insti_app = input("is the student going to educational appprove  institution.? ") 
# if gpa >=3.9: 
#     if insti_app == "yes":
#         print("the application qualifier low apr student loan")
#     else:
#         print("application does not qualify since they have not be accepted into an approved institution") 
# else:
#     print("the application is did not have high school enough to qualify")  

# gpa = float(input("enter the GPA."))
# ins_app = input("is the institute will be approved your application for loan.? \n") 
# if gpa >=3.7:
#     if ins_app =="yes":
#         print("the application will be qualify:")
#     else:
#         print("please firstly approved for the institude approvement for the loan approver")
# else:
#     print("not enough GPA.")
        
#exercise for the grede distribution::-  
# maths = int(input("enter the student score"))
# if maths >=90:
#     print("Your Grade is A") 
# else:
#     if maths >=80:
#         print("B")
#     else:
#         if maths >=70:
#             print("C")
#         else:
#             if maths>=60:
#                 print("D")
#             else:
#                 print("F") 

# score = int(input("what is student score.?"))
# if score >=90:
#     print("A")
# else:
#     if score >=80:
#         print("B")
#     else:
#         if score >=70:
#             print("C")
#         else:
#             if score >=60:
#                 print("D")
#             else:
#                     print("F")

#ELIF STATEMENT
# traffic_light = input("which colour you will enter")
# if traffic_light =="red":
#     print("stop")
# elif traffic_light =="green":
#     print("Go")
# elif traffic_light =="blue":
#     print("please wait")
# else:
#     print("insufficient input") 


# traffic_light = input("which colour you will enter")
# if traffic_light =="red":
#     print("stop")
# elif traffic_light =="green":
#     print("Go")
# elif traffic_light =="blue":
#     print("please wait")
# else:
#     print("insufficient input")  

# from random import randint
# one_to_ten = randint(1, 10)
 
# if one_to_ten == 1:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
# elif one_to_ten == 2:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
# elif one_to_ten == 3:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
# elif one_to_ten == 4:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
# elif one_to_ten == 5:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
# elif one_to_ten == 6:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
# elif one_to_ten == 7:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
# elif one_to_ten == 8:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
# elif one_to_ten == 9:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
# else:
#     print("The roman numeral equivalent of " + str(one_to_ten) + " is X.") 
  

#While Loop Infinite loops 
# counter = 0
# while counter <10:
#     print(counter) 
#     counter+=1


# #While Loops 
# counter = 0
# while counter <2:
#     print("koshti")
#     counter +=1


#decline number generator:
# dec_int = 10
# while dec_int !=0:
#     print(dec_int)
#     dec_int -=1 

# world = "hello world"
# for  latter in world:
#     print(latter) 

# # exercise
    
# user = input("enter the word")
# counter = 0
# for char in user:
#     user+=1
# print(user)
# print(counter) 

# user_str = input("Please enter a string.")
 
# count = 0  # This variable will be used to hold the number of characters in the string.
# # This for loop adds 1 to count for each character in user_str.
# for char in user_str:
#     count += 1
 
# print(user_str)  
# print(count) 


# user_string = input("enter the string:")
# counter = 0 
# for char in user_string:
#     counter +=1

# print(user_string)
# print(counter) 
 
# user_input = input("enter the string")
# count = 0 
# for char in user_input:
#     count +=1
# print(user_input)
# print(count)
 


# #range
# one_input = range(7)
# for num in one_input:
#     print(num) 
# two_input = range(0, 10)
# for num in two_input:
#     print(num) 

# for num in range (1, 51):
#     if num %3 == 0 and num %5 ==0: 
#         print("fizzbuzz") 
#     elif num %3 ==0:
#         print("fizz")
#     elif num %5 ==0:
#         print("buzz")
#     else:
#         print(num) 



for num in range (1, 51):
    if num %3 ==0 and num %5 ==0:
        print("fizzbuzz")
    elif num %3 ==0:
        print("fizz")
    elif num %5 ==0:
        print("buzz")
    else:
        print(num)

