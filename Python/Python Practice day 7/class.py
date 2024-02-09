class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_value(self):
        print(f" name  =  {self.name}")
        print(f" age  =  {self.age}")


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
