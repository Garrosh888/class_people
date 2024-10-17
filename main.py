class chelovek():
    def __init__(self,name = None,last_name = None,age = None):
        self.name = ""
        if name is not None:
            self.name = name
        self.last_name = ""
        if last_name is not None:
            self.last_name = last_name
        self.age = 0
        if age is not None:
            self.age = age
    def info(self):
        print("введите имя")
        self.name = str(input())
        print("введите фамилию.")
        self.last_name = str(input())
        print("tell me your age")
        self.age = int(input())
    def printer(self):
        print(f"my name is {self.name} {self.last_name} and I am {self.age} years old")
    def calculator(self):
        print("I can sum ")
        x = int(input("введите число \n "))
        y = int(input("введите число \n "))
        print(x + y)
    def umnoshat(self):
        print("привет я умею умножать скажи мне число")
        x = int(input("введите число \n "))
        y = int(input("введите число \n "))
        print(x * y)

aziz = chelovek()
aziz.info()
aziz.printer()
#aziz.calculator()
#aziz.umnoshat()
nady = chelovek("Nady","ushkurova",31)
nady.printer()
rushuk = chelovek("rushuk")
rushuk.printer()

