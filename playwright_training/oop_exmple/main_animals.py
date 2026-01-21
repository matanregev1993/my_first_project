from playwright_training.oop_exmple.dog_objects import DogObject


class MainAnimal:
    dog_1 = DogObject("Rexy",4)
    dog_2 = DogObject("Lucky",6)
    dog_1.make_noise()
    dog_2.make_noise()
    dog_1.calculate_distance(4,2)