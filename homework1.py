grade = 60
if grade < 50:
    grade = grade * 1.1
elif (grade < 80) and (grade > 50):
    print("the grade is between 50 and 80")
elif grade <= 100:
    grade = grade + 20
    print("the grade is more than 80 , the student get 20 points")

else:
    print(f"not valide grade define the value is {grade}")

first_name_length = 0
last_name_length = 0
full_name = "Matan_Regev"

# split to first and last name
# option1
for i in range(len(full_name)):
    if full_name[i] != "_":
        first_name = full_name[:i + 1]
    else:
        first_name_length = len(first_name)
        last_name_length = len(full_name) - first_name_length - 1
        break
# option 2
index = full_name.index("_")
first_name = full_name[:index]
last_name = full_name[index + 1:]

# check for longest word

for i in range(0,11):
    Number = 3*i
    print(Number)
