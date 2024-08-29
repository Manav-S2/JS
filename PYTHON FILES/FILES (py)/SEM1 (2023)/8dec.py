# # import requests
# # from bs4 import BeautifulSoup
# # import re
# # # print("test")
# # page = requests.get("https://books.toscrape.com/")
# # b = BeautifulSoup(page.content, 'html.parser')
# # print(str(b))
# # George Danil Aswell
# # George Denks Aswell
# a = list(input().split())
# b = list(input().split())
# common = []
# cond = False
# vow = ['a','e','i', "o", "u"]
# for i in  a :
#     # for j in b:
#     #     if i == j:
#     if i in b:
#             common.append(i)
#
# common2 = []
# for i in common:
#     for j in i:
#         if j in vow:
#             cond = True
#             break
#         else:
#             cond = False
#     if cond:
#         common2.append(i)
#
# print(common2)




a = 5
b = 34
for i in range(5):
    for j in range(b):
        print(i , j)
        if j == 4:
            break

