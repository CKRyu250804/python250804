# demoClass.py

# 1) 클래스 정의

class Person:
    #초기화 method
    def __init__(self):
        self.name = "default name"
        self.name2 = "default name2"
    def print(self):
        #f-string문번 : 포매스트링
        #print("My name is {1}, {0}".format(self.name, self.name2))
        print(f"My name is {self.name2}, rival is {self.name}")

# 2) 인스턴스 생성
p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.name2 = "화담선생"
p1.print()
p2.print()
