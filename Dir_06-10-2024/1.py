class Cat:
    def __init__(self, energy, mood, hunger):
        self.__energy = energy
        self.__mood = mood
        self.__hunger = hunger

    def eat(self):
        self.__energy += 1
        self.__mood += 1
        self.__hunger -= 1

    def sleep(self):
        self.__energy += 1
        self.__hunger += 1

    def play(self):
        self.__energy -= 1
        self.__mood += 1
        self.__hunger += 1