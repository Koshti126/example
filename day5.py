#STRING METHODS:


# print("lower to upper")
# low_char = "this is  the lower case"
# print(low_char.upper())

# print("upper to lower")
# upper_char = "THIS IS THE UPPER CASE"
# print(upper_char.lower()) 

# print("this is upper string".isupper())
# print("THIS IS UPPER STRING".isupper()) 

# print("this is lower string".islower())
# print("THIS IS UPPER STRING".islower()) 

#Multiple string method 

# lowee_str = "this is the minecraft game."
# # print(lowee_str.lower())
# # print(lowee_str.islower()) 
# print(lowee_str.isalpha()) 
# print(lowee_str.isalnum())
# print(lowee_str.isdecimal())
# print(lowee_str[1].isspace())
# print(lowee_str.title()) 
# print(lowee_str.istitle())   
# print(lowee_str.startswith("this")) 
# print(lowee_str.startswith("game."))
 
## join and split method...
# print(" ".join(["one", "two", "three", "four"])) 
# print("one, two, three, four".split(","))   


# # exercise for the string method related.
# mix_case = "A Song of Ice and Fire"
# print(mix_case.isupper()) 
# print(mix_case.islower()) 
# print(mix_case.upper())
# print(mix_case.lower()) 
# print(mix_case.istitle()) 
# print(mix_case.title())
# print(mix_case.startswith("A"))
# print(mix_case.endswith("e"))
# print("one, two, three ".split())
# print(", ".join(["one", "two", "theree"])) 



## String method -2 
# # print("hello world ".center(90)) 
# print("hello world".rjust(15))
# print("hello world".ljust(15))

# print("hello world".rjust(15,"-"))
# print("hello world".ljust(15,"*"))


#.strip, rstrip , lstrip

# print("juice, bread, cheese, breef, bread, juice".strip("juice,")) 
# print("juice, bread, cheese, breef, bread, juice".rstrip("juice,"))
# print("juice, bread, cheese, breef, bread, juice".lstrip("juice,"))  

# print("good morning.".replace("morning","afternoon")) 

# excercise 

# the_string = "North Dakot"
# print(the_string.rjust(17)) 
# print(the_string.ljust(17,"*")) 
# print(the_string.center(16) + "good morning") 
 
# print(the_string.replace("North","South")) 

#len  
# print(len(the_string)) 
 
# user_string = input("Please enter a string.")
# reversed = ""
 
# for item in range(len(user_string) - 1, -1, -1):
#     reversed += user_string[item]
 
# print(reversed) 
# user_string = input("enter the string")
# reversed = ""
# for iteam in range(len(user_string) -1, -1, -1):
#     reversed +=user_string[iteam]
# print(reversed)

 
# User_string = input("enter the string:")
# reversed = ""
# for iteam in range(len(User_string) -1, -1,-1):
#     reversed +=User_string[iteam]
#     print(reversed) 



# str_1 = "James Bond is 007."
# str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
# str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
# saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
# shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
# shrimp burger, shrimp sandwich. That- that's about it."
 
 

# def word_counter(words):
#     spaces_and_letters = ""
#     word_count = 1
#     for i in words:
#         if i.isalnum() or i.isspace() or i == "-" or i == "'":
#             spaces_and_letters += i
#     for j in spaces_and_letters:
#         if j == " ":
#             word_count += 1
#     return word_count
 
 
# print(word_counter(str_1))
# print(word_counter(str_2))
# print(word_counter(str_3)) 


# name = input("what is the job appplication name.?")
# degree = input("what did they major in a collage.?") 
# job = input("what did they current occupaction.?")
# experience = input("how many years you have they been working in their field.?")
# print("{} major in {} work as a {} and has {} year of a experience".format(name, degree, job, experience)) 


# list operations 

# list in or not in operations 

        # list_Checked = [1,2,3,4,5]    
        # print(4 in list_Checked) 
        # print(9 not in  list_Checked) 
# list_slice = [[0,2],[4,6],[8,10],[12,14]] 
# print(list_slice[3][1]) 
# list_slice2 = ["chair", "table", "desk", "lamp", "bed"] 
# print(list_slice2[-5]) 
# list_slice2[3] = "hello"  
# print(list_slice2)
# del list_slice2 [2]
# print(list_slice2)