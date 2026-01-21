nums = [1,2,3,4,5,6,7,8,9,10]
sum_even = 0
sum_odd = 0
for num in nums:
    if num % 2 == 0:
        print (f"{num} is even")
        sum_even = sum_even + num
        print (f"sum_even is {sum_even}")
    else:
        print (f"{num} is odd")
        sum_odd = sum_odd + num
        print (f"sum_odd is {sum_odd}")

list = ["old", "new-york"]
if list[0] in list[1]:
    print (f"{list[0]} is in {list[1]}")
else:
    print (f"{list[0]} is not in {list[1]}")

list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
list_num2 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
for num1 in list_num:
    if num1 % 7 == 0:
        print (num1)
for num2 in list_num2:
    if "7" in num2:
        print(num2)
