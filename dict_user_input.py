Title = "this is the user input for the dictionary! "
print(Title.upper()) 
print(Title.center(90)) 
value_dict = {}
user_input = int(input("enter the number of county :-"))
if user_input == " ":
    print("please enter the some data")
for i in range(user_input):
    key = input("enter the county name :")
    value = input("enter the value:")
    value_dict[key] = value
print(value_dict)