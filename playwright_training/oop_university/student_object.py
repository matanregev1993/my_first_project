from playwright_training.oop_university.person_parent import PersonParent


class Student(PersonParent):

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_avg_grade(self, grades: list)->float:
        summery = 0
        for grade in grades:
            summery += grade

        avg = summery / len(grades)
        return avg

    def is_pass(self,grades : list, ref_value: int = 60) -> bool:
        summery = 0
        for grade in grades:
            summery += grade

        self.avg = summery / len(grades)

        print (f"the average grade of student {self.first_name} {self.last_name} is {self.avg}")
        if self.avg>ref_value :
            return True
        else:
            return False

