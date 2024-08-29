try:
    def fun():
        try:
            a = int(input('Enter an integer: '))
            print(a)
        except:
            print("plz enter an integer")
            a = input("Enter an integer: ")
            raise Exception
    fun()


except Exception:
    print("plz enter an integer")
    fun()