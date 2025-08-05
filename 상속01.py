# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # Overriding
        #self.name = name
        #self.phoneNumber = phoneNumber
        #부모의 초기화 메서드 호출
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
        # Overriding
    def printInfo(self):
        #print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))  
        #print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))
        print(f"Info(Name:{self.name}, Phone Number: {self.phoneNumber},"
              f" Subject:{self.subject}, StudentID: {self.studentID})")
       


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "24001")
print(p.__dict__)
print(s.__dict__)
p.printInfo()
s.printInfo()


