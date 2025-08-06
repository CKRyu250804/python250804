# # demoFile.py
# # 파일 쓰기
# f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
# f.write("첫번째\n두번째\n세번째\n")
# f.close()

# #파일 읽기
# #f = open("c\\work\\test.txt", "rt", encoding="utf-8")
# f = open(r"c:\work\test.txt", "rt", encoding="utf-8")  # 이스케이프 문자 사용
# print(f.read())  # 전체 읽기
# f.close()

# 문자열 처리
strA= "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))  # 문자열 길이
print(len(strB))  # 문자열 길이
print(strB.capitalize())    # 첫 글자 대문자
print(strB.upper())  # 대문자 변환
print("MBC2580".isalnum())  # 알파벳과 숫자만 있는지 확인
print("2580".isdecimal())  # 숫자만 있는지 확인
#data = " spam and ham "
#result = data.strip()  # 양쪽 공백 제거#
data = "<<< spam and ham >>>"
result = data.strip("<> ")      # 양쪽 공백과 특정 문자 제거  
print(data)
print(result)
result2 = result.replace("spam", "spam egg")  # 문자열 치환
print(result2)  # 치환된 문자열 출력
lst = result2.split()  # 공백을 기준으로 분리하여 리스트로 반환
print(lst)
print(":)".join(lst)) # 리스트를 문자열로 결합
print("".join(lst)) # 리스트를 문자열로 결합
print(lst)



# 정규표현식
import re

result = re.search("[0-9]*th", "35th") #뒤에 string에서 앞에 조건에맞는걸 찾음
print(result)
print(result.group())  # 검색된 문자열 출력

result2 = re.match("[0-9]*th", "35th")
print(result2)
print(result2.group())  # 검색된 문자열 출력

result3 = re.search("[0-9]*th", "  35th")
print(result3)
print(result3.group())  # 검색된 문자열 출력

# result4 = re.match("[0-9]*th", "  35th")
# print(result4)
# print(result4.group())  # 검색된 문자열 출력


result = re.search("apple", "this is apple") #뒤에 string에서 앞에 조건에맞는걸 찾음
print(result.group())  # 검색된 문자열 출력

result = re.search(r"\d{4}", "올해는 2025년 입니다.") #뒤에 string에서 앞에 조건에맞는걸 찾음
print(result.group())  # 검색된 문자열 출력

result = re.search("\d{5}", "우리동네는 51200입니다.") #뒤에 string에서 앞에 조건에맞는걸 찾음
print(result.group())  # 검색된 문자열 출력