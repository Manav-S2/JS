# # class Shape:
# #     def noOFsides(self, sides):
# #         self.sides = sides
# #
# # class Square(Shape):
# #     def noOFsides(self, sides):
# #         self.sides = sides
# #         self.name = 'square'
# #
# # s = Square()
# # s.noOFsides(4)
# # print(s.sides)
# # print(s.name)
# #
#
#
# class Car:
#     def __init__(self, name, model, regno):
#         self.name = name
#         self.model = model
#         self.regno = regno
#
#     def getcar(self):
#         print(self.name)
#         print(self.model)
#         print(self.regno)
#
#
# mycar = Car('Honda Civic', 'ZM12', 1223)
# mycar.getcar()
#
# class Abstract(Object):
#     def foo(self):
#         raise


class Animal:
    def __init__(self, name = 'This Animal'):
        self.name = name
    def eat(self, food = 'Grass'):
        self.food = food
        print(self.name, 'eats', food)
class Mammal(Animal):
    def eat(self):
        print(self.name, 'does not eat. It only Drinks')
