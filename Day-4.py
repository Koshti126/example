# ##exercise for the list ## 
# artic_animal = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"] 
# # artic_animal.remove("tiger") 
# # artic_animal.remove("elephant") 
# # artic_animal.append("artic_fox") 
# # artic_animal.insert("snow_owl") 
# # artic_animal.insert("raindear") 
# # artic_animal.sort()
# # print(artic_animal) 
# import copy 
# ex_12 = [1,2,3,4,5,6,7]
# ex_13 = copy.deepcopy(ex_12)
# ex_12[1] = 3
# print(ex_12)
# print(ex_13) 
# list_val = ["k"
#             "r"
#             "i"
#             "s"
#             "h"
#             "n"
#             "a"]
# print(list_val)

# ex_5 = 3 + 6 + 90
# print(ex_5)


# console = {"name" : "krishna", "personality": "student "}
# print("Name" in console) 


#Excercise for the dictionary: 
# dictionary_access = {"name":"krishna", "surname":"koshti", "colification":"student", "gender": "male","age": 18}
# print(dictionary_access["gender"]) 
# print("gender" in dictionary_access) 
# print("result" not in dictionary_access) 

# print(dictionary_access.keys())

# for keys in dictionary_access.keys():
#     print(keys) 

# for values in dictionary_access.values():
#     print(values)  

# print(dictionary_access.keys()) 
# print(dictionary_access.values())  
# dictionary_access = {"name":"krishna", 
#                      "surname":"koshti", 
#                      "colification":"student", 
#                      "gender": "male",
#                         "age": 18} 

# if "age" in dictionary_access:
#     print(dictionary_access["age"])  
# else:
#     print("age is not found") 
# if "gender" in dictionary_access:
#     print(dictionary_access["gender"])
# else:
#     print("gender is not found")

# people = dictionary_access
# people =[9398]
# print(dictionary_access) 

dic_ex = {"Queen": "Bohemian Rhapsody", 
          "Bee Gees": "Stayin' Alive", 
          "U2": "One", 
          "Michael Jackson": "Billie Jean", 
          "The Beatles": "Hey Jude", 
          "Bob Dylan": "Like A Rolling Stone"
}
# print(len(dic_ex)) 

# for keys in dic_ex.keys():
#     print(keys) 
# print(dic_ex.values())

# for iteams in dic_ex.items():
#     print(iteams)
# print(dic_ex.get("Promise of the Real","That is not a key that appears in the dictionary.")) 
# if "Queen" in dic_ex:
#     print(dic_ex["Queen"])
# else:
#     print("Queen not found") 
# ex_12 = {}.fromkeys(["address"],"126,sec-2 nirnaynagar")
# ex_13 = {}.fromkeys(["name","koshti krishna"]) 
# ex_12.update(ex_13) 
# print(ex_13) 
 
# d1 ={}.fromkeys(["value"],123)
# print(d1) 
# my_dict = {'Name': 'Sean', 'Age': 24, 'Hobby': 'Dancing', 'City': 'NY'}
# my_dict.popitem()
# print(my_dict) 


##Dictionary key excercise -2:
# Ex_2 = {}.fromkeys("bcd","consonant")
# print(Ex_2) 

# Ex_2_Q2 = fast_food_items = {"McDonald's": "Big Mac", 
#                            "Burger King": "Whopper", 
#                            "Chick-fil-A": "Original Chicken Sandwich"
# }
# # popped = Ex_2_Q2.pop("McDonald's") 
# # print(popped) 
# Ex_2_Q2.popitem()  ##Q-3
# print(Ex_2_Q2) 

# Dictionary method -3 
# hisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# } 
# ### Update method (concate the dictinary,modify)
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }
# # hisdict.clear()
# # print(hisdict) 
# # hisdict.copy()
# # print(hisdict) 
# hisdict.update(country_capitals)
# print(hisdict)  


# Ex_3_Q1= {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# Ex_3_q1= {"shroud": "Twitch"} 
# # Ex_3_Q1.update(Ex_3_q1)
# # print(Ex_3_Q1) 
# Ex_3_Q1.clear()
# print(Ex_3_Q1) 
# Ex_3_Q1.copy()
# print(Ex_3_q1) 

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# } 
# # if "America" not in country_capitals:
# #     country_capitals["America"] = "county"
# #     print(country_capitals) 
# country_capitals.setdefault("America","asia") 
# print(country_capitals) 