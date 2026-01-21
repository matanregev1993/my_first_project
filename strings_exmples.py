full_name = "Leo messi"
len_full_name=len(full_name)
print(len_full_name)
full_name_new = full_name.replace("leo", "leonid")
full_name = "Eli Cohen"
index = full_name.index(" ")
first_name = full_name[:index]
last_name = full_name[index + 1:]
random_name = full_name[1:6]
count_from_last = full_name[-5:]
single_char = full_name[4]
print(f"first name is {first_name} last name is {last_name}, random name is {random_name}")
print(full_name_new)



statement = "Hi My name is Leo Messi"
for i in range(1, len(statement)+1):
    if statement[0:i] == "Hi My name is Leo Mes":
        print(statement[0:i])
        break
    else:
        print(statement[0:i])
