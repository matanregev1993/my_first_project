#define 2 student, find the higher avg
#define 1 drive calcoulate for his age and licsence level
from playwright_training.oop_university.object_driver  import Driver
from playwright_training.oop_university.student_object import Student


student_1 = Student("Leo", "Messi")
student_2 = Student("John", "Doe")
driver_1 = Driver("Eli Cohen", "a")
driver_1.age_alayzer(20)
student_2.age_alayzer(16)
grades_1= [90,50,65,40]
avg_1 = student_1.get_avg_grade(grades_1)
grades_2= [60,55,25,60]
avg_2 = student_2.get_avg_grade(grades_2)
student_1.is_pass(grades_1)
student_2.is_pass(grades_2, 70)

assert avg_1 > avg_2, "AVG2 is higher than AVG1"
print("AVG1 is higher that AVG2")



