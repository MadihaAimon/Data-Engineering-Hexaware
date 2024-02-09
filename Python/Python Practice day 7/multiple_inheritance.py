class Animal:
    def speak(self):
        print("Animal speaks")


class Pet:
    def cuddle(self):
        print("Pet cuddles")


class Dog(Animal, Pet):
    def bark(self):
        print("Dog barks")


dog1 = Dog()
dog1.speak()
dog1.cuddle()
dog1.bark()
