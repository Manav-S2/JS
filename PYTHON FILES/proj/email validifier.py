email = input('Enter your Email: ')

#Rules for an email....
'''
1. Min number of characters 6.
2. first letter is an alphabet.
3. @ appears only one time.
4. '.'  appears at last 3 and 4 position .com .in
5. all letter in small case.

g@d.in g - name  @  d @ gmail/yahoo/outlook in/com 
'''
k = 0
l = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-3] == '.') ^ (email[-4] == '.'):
                for i in email:
                    if (i.isspace()) or (i.isupper()):
                        k = 1

                    elif i.isdigit() or i.isalpha() or i == '_' or i == '@' or i =='.':
                      pass
                      '''  print(k)
                        print(l)
                        continue
                    elif i == '_' or i == '@' or i =='.':
                        print(k)
                        print(l)
                        continue'''

                    else:
                        l = 1

                if k == 1 or l == 1:
                    print('wrong Email 5')
                else:
                    print('Right Email')
            else:
                print('wrong Email 4')
        else:
            print('wrong Email 3')
    else:
        print('wrong Email 2')

else:
    print('wrong Email 1')












