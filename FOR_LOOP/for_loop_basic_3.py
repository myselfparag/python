##Looping over a dict

user_accounts = {"Chirag" : "plusminuschirag", "Parag" : "iamparagsharma", "Chintu" : "inderjeetbhardwaj"}
#Key, Value

# print(user_accounts.keys())
# print(type(user_accounts.keys()))

for key_realname, value_username in user_accounts.items():
    print(f"Real Name : {key_realname}, Username : {value_username}")