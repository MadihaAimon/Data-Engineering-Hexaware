class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Puppy(Dog):
    def wag_tail(self):
        print("Puppy wags tail")


puppy1 = Puppy()
puppy1.speak()
puppy1.bark()
puppy1.wag_tail()
