import  re
pattern = r'[A-Z]+yclone'
text = "Browsing?Please Cyclone Dyclone use the search box at the top of this page or the links to the right. Feel free to subscribe to our syndicated feeds.Using?To fulfill the free license requirements, please read our Reuse guide. You can also request a file.Identifying?Have a browse through Category:Unidentified subjects. If you find something you can identify, write a note on the item's talk page.Creating?Check out all you need to know at our Contributing your own work guide.and more!To explore more ways you can contribute to this project, ch"

match = re.finditer(pattern, text)
for i in match:
    print(i.span())
    print(text[i.span()[0]:i.span()[1]])