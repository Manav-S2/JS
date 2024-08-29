# class Newclass(Exception):
#     def __init__(self, message):
#         self.me = message
#
#
# try:
#     raise Newclass('error')
# except Newclass as m:
#     print(m.me)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import re

s = "I am in K23DC, I am in Btech"

z = re.findall(r"a", s)

print(z)