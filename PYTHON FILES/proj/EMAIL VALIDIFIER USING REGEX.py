import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

''' / - to search a character in regex use backslash
    ? - input given should be present atmost 1 time, more than 1 gives false condition
    [a-z] - range
    \w - searches the character or string
    
'''


user_email = input('Enter your Email : ')


if re.search(email_condition, user_email):
    print('Right Email')

else:
    print('wrong Email')