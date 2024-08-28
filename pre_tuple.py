""" x = 5
y = 10
z = 15

x, y, z = y, z, x 


print("x =", x)
print("y =", y)
print("z =", z)


def swap_variables(x, y):
    temp = x
    x = y
    y = temp
    return x, y

x, y = swap_variables(x, y)
print("x =", x,"y =", y)
 """



""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person1 = Person("John", 23)
person2 = Person("Sam", 25)
person3 = Person("Tom", 33)

class_room = [person1, person2, person3]
    
person1.age = 26

print(person1.age)  """



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)