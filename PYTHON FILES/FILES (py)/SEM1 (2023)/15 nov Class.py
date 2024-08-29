# # # class Person():
# # #     name = 'aditya'
# # #     aadhaarno = '0000 1111 2222 3333'
# # #
# # # class Employee(Person):
# # #     empID = 43478
# # #
# # # emp1 = Employee()
# # # print(emp1.empID)
# # # print(emp2)
# #
# #
# # class Car():
# #     def setenginemodel(self, engine):
# #         self.engine = engine
# #     def getenginemodel(self):
# #         print(self.engine)
# #
# # class Honda(Car):
# #     def setcarmodel(self, model):
# #         self.model = model
# #     def getcarmodel(self):
# #         print(self.model)
# #
# # mycar = Honda()
# # mycar.setenginemodel('Ek-1')
# # mycar.setcarmodel('Vs')
# # mycar.getenginemodel()
# # mycar.getcarmodel()
#
# class Employee:
#     empId = 1233
#     salary = 35999
#
# class Citizen:
#     aadhaarID = '1111 2222 3333 4444'
#     phoneno = 1243232332
#
# class Person(Employee, Citizen):
#     car = 'Nano'
#
# person_one = Person()


# print(person_one.aadhaarID)




class Alpha:
    def __init__(self, color, height):
        self.color = color
        self.height = height

    def zam(self):
        print(self.color)
        print(self.height)
gamma = Alpha(12,34)

gamma.zam()

'''    Method Overriding'''

class Shape:
    def noOFsides(self, name):
        self.name = name

class Square(Shape):
    def noOFsides(self,name):
        self.name = name
        self.shape = 'square'

        # print( self.shape, self.name)



a = Square()
a.noOFsides('as')
print(a.name)
print(a.shape)