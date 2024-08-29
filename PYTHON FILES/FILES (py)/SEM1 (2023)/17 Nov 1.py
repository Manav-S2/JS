# # # # #PUBLIC
# # # # #PRIVATE
# # # #
# # # # class Employee:
# # # #     __salary = 23554
# # # #     empID = 'defe'
# # # #     def __display(self):
# # # #         print("This is a private method")
# # # # class Person(Employee):
# # # #     aadhaarID = '1111 2222 3333 4444'
# # # #
# # # #
# # # # person_one = Person()
# # # # print(person_one.aadhaarID)
# # # # print(person_one.empID)
# # # # print(person_one.__salary)
# # # #
# # # # person_one.__display()
# # # class a:
# # #     pass
# # #
# # # b = a()
# # # class b():
# # #     c = 'sdf'
# # #
# # # print(type(b))
# # # print(type(type(b.c)))
# # #
# #
# #
# #
# #
# #
# #
# # class S1:
# #
# #     def a(self):
# #         print('fd')
# #
# #     def a(self):
# #         print('fef')
# #         print(int)
# # #
# #     b = 'ref'
# # # a1 = s()
# # # a1.a()
# #
# # class S2:
# #     def a(self):
# #         print('s2fdf')
# #     b = 'fr'
# # class S3(S1,S2):
# #     pass
# #
# # d = S3()
# # d.a()
# # print(d.b)
#
#
# """Super"""
#
# class Emp:
#     def __init__(self, id , name, Add):
#         self.id = id
#         self.name = name
#         self.Add = Add
#
# class Freelance(Emp):
#     def __init__(self, id, name, Add, Emails):
#         super().__init__(id, name, Add)
#         self.email = Emails
# Emp_1 = Freelance(103, 'Suraj kr gupta', 'Noida', 'dksld@dnk')
# print(Emp_1.id, Emp_1.name, Emp_1.Add, Emp_1.email)
#
#
#
#
#
#
#
#
# class Furniture:
#     def legs(x):
#         print('has %s legs'%x)
#
# Furniture.legs(4)



# class A:
#     a = input('cef')
#     b = input('fef')
#     att = b
#
# print(A.att)

