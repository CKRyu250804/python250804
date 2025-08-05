class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 코드
def test_person():
    p = Person(1, "홍길동")
    assert p.id == 1
    assert p.name == "홍길동"

def test_person_printInfo(capsys):
    p = Person(2, "김철수")
    p.printInfo()
    captured = capsys.readouterr()
    assert "ID: 2, Name: 김철수" in captured.out

def test_manager():
    m = Manager(3, "이영희", "팀장")
    assert m.id == 3
    assert m.name == "이영희"
    assert m.title == "팀장"

def test_manager_printInfo(capsys):
    m = Manager(4, "박민수", "부장")
    m.printInfo()
    captured = capsys.readouterr()
    assert "ID: 4, Name: 박민수, Title: 부장" in captured.out

def test_employee():
    e = Employee(5, "최지우", "Python")
    assert e.id == 5
    assert e.name == "최지우"
    assert e.skill == "Python"

def test_employee_printInfo(capsys):
    e = Employee(6, "정우성", "Java")
    e.printInfo()
    captured = capsys.readouterr()
    assert "ID: 6, Name: 정우성, Skill: Java" in captured.out

def test_inheritance_manager():
    m = Manager(7, "김유신", "이사")
    assert isinstance(m, Person)

def test_inheritance_employee():
    e = Employee(8, "유관순", "C++")
    assert isinstance(e, Person)

def test_manager_title_change():
    m = Manager(9, "장보고", "팀장")
    m.title = "본부장"
    assert m.title == "본부장"

def test_employee_skill_change():
    e = Employee(10, "이순신", "Go")
    e.skill = "Rust"

# 추가 테스트 코드
def test_person_str_output(capsys):
    p = Person(11, "강감찬")
    p.printInfo()
    captured = capsys.readouterr()
    assert "ID: 11, Name: 강감찬" in captured.out

def test_manager_str_output(capsys):
    m = Manager(12, "윤봉길", "차장")
    m.printInfo()
    captured = capsys.readouterr()
    assert "ID: 12, Name: 윤봉길, Title: 차장" in captured.out

def test_employee_str_output(capsys):
    e = Employee(13, "안중근", "C#")
    e.printInfo()
    captured = capsys.readouterr()
    assert "ID: 13, Name: 안중근, Skill: C#" in captured.out

def test_manager_inheritance_fields():
    m = Manager(14, "신사임당", "팀장")
    assert hasattr(m, "id")
    assert hasattr(m, "name")
    assert hasattr(m, "title")

def test_employee_inheritance_fields():
    e = Employee(15, "허준", "SQL")
    assert hasattr(e, "id")
    assert hasattr(e, "name")
    assert hasattr(e, "skill")

def test_manager_change_name():
    m = Manager(16, "유재석", "부장")
    m.name = "강호동"
    assert m.name == "강호동"

def test_employee_change_name():
    e = Employee(17, "이광수", "JavaScript")
    e.name = "하하"
    assert e.name == "하하"

def test_manager_printInfo_change_title(capsys):
    m = Manager(18, "박지성", "코치")
    m.title = "감독"
    m.printInfo()
    captured = capsys.readouterr()
    assert "감독" in captured.out

def test_employee_printInfo_change_skill(capsys):
    e = Employee(19, "손흥민", "축구")
    e.skill = "골키퍼"
    e.printInfo()
    captured = capsys.readouterr()
    assert "골키퍼" in captured.out

def test_manager_and_employee_are_person():
    m = Manager(20, "정몽주", "대표")
    e = Employee(21, "이성계", "경영")
    assert isinstance(m, Person)
    assert isinstance(e, Person)

if __name__ == "__main__":
    # Person 인스턴스 생성 및 출력
    p = Person(1, "홍길동")
    p.printInfo()

    # Manager 인스턴스 생성 및 출력
    m = Manager(2, "김철수", "팀장")
    m.printInfo()

    # Employee 인스턴스 생성 및 출력
    e = Employee(3, "이영희", "Python")
    e.printInfo()