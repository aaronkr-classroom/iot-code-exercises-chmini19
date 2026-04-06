# 5_class.py

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"My name is {self.name}!")
        
    def setName(self, name:str):
        """
        set the Animal class's name.
        Animal 클래스의 이름을 재정의하는 함수.
        :param name:Animal의 이름
        """
        return self.name
        self.name = name
        
    def getName(self, name:str):
        """
        Return the Animal class's name.
        Animal 클래스의 이름을 반환하는 함수.
        :return:Animal의 이름
        """
        return self.name
    
class Dog(Animal):
    def __init__(self, name, age = 3):
        super().__init__(name)
        self.age = age
        
    def speak(self):
        print(f"(self.name) says woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"(self.name) says meow!")
        

#호출
my_dog = Dog("Spot")
my_cat = Cat("Headache")
my_dog.speak()
my_cat.speak()