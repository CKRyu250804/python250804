strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스가 쓰는 멤버변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #버그
        print(strName)
        #맞게 된거
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
