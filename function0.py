# function0.py

# 1) 함수 정의
def setValue(newValue):
    # 지역변수
    x = newValue
    print("함수 내부:", x)

# 2) 함수 호출
retValue = setValue(5)
print(retValue)

def swap(x, y):
    return y, x
result = swap(3,4)
print(result)

print("---함수 이름 해석---")

x = 5
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    x = 10
    return a+x
print(func2(1))

print("---기본 값---")

def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자
def connectURL(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

print(connectURL("multi.com","80"))
print(connectURL(port = "80", server = "test.com"))

