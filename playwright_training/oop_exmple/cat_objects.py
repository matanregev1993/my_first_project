from playwright_training.oop_exmple.animal_parent_object import AnimalParentObject


class CatObject(AnimalParentObject):
    def __init__(self, legs_amount, age):
        self.legs_amount = legs_amount
        self.age = age


    def make_cat_noise(self):
        print ("Miao , Miao, Miao")

    # def calculate_distance (self,time,speed):
    #     distance = time * speed
    #     if distance <10 :
    #         print ("The animal is lazzy")
    #
    #     else:
    #         print("the animal is ok")
    #
    #     return distances lazy")
    #    else:
    #       print ("The animal is ok")