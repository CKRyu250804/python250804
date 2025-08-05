# demoIndex.py

strA = '파이썬은 강력해'
strB = 'python is very powerful'

print(len(strA))
print(len(strB))
print(strA[:2])
print(strB[:6])
print(strB[-3:])

strC = """이번에는
다중의 라인을
저장합니다.
"""

print(strC)


print("---리스트 형식---")
lst = [10,20,30]
print(len(lst))
print(lst[0])
lst.append(40)
print(lst)
lst.insert(1, 5)
print(lst)
lst.remove(20)
print(lst)

lst.remove(5)
print(lst)

lst.reverse()
print(lst)

lst.sort()
print(lst)


print("---Tuple---")
tp = (100, 200, 300)
print(len(tp))
print(tp[1])
print(tp.index(300))

#함수를 정의
def calc(a, b):
    return a+b, a*b

#함수를 호출
print(calc(3, 4))

print("id : %s, name : %s"% ("kim", "김유신"))

args = (5,6)
print(calc(*args))


print("---set---")
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(len(a))
print(len(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))

print("---형식변환---")
a = set((1,2,3))
print(a)
b = list(a)
b.append(10)
print(b)
c = tuple(b)
print(c)

print("---Dict---")
color = {"apple":"red", "banana":"yellow"}
print(color)
color["cherry"] = "red"
print(color)
for item in color.items():
    print(item)

for k, v in color.items():
    print(k, v)

print(color["apple"])
del color["apple"]
print(color)

color.clear()
print(color)

#장비모음
devices = {"아이폰":5, "아이패드":10, "윈도우타블렛":15}
print(devices)
devices["맥북"] = 20
print(devices)
devices["아이폰"] = 6
print(devices)
del devices["맥북"]
print(devices)
for item in devices.items():
    print(item)

for k, v in devices.items():
    print(k, v)    

globals()
dir()

