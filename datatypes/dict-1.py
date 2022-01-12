names = {"Chirag" : 10, "Parag" : 22, "Chintu" : 50}


#Show the value of the name if name is not in dict, show the value as 5
user_name = "Chirago@@"

if user_name in names.keys():
    print(names[user_name])
else:
    print("5")


##Alternative
print(names.get(user_name, 5))


###If user_name is in keys: 500 multiply otherwise 100

if names.get(user_name):
    print(names[user_name] * 500)
else:
    print("100")