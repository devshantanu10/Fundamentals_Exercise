# class Car:
#     def __init__(self , color , model):
#         self.color = color
#         self.model = model


# car_1 = Car("Red" , "Toyota") # type: ignore
# car_2 = Car("Blue" , "Porsche") 

# print(car_1.model)
# print(car_2. model)


# print(car_1.color)
# print(car_2.color)


class dog:

    species = "French bull-dog"

    def __init__(self,name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof woof"

jack = dog("Jack")
jill = dog("Jill")

print(jack.bark())
print(jill.bark())


