# demoFile.py
# 파일 쓰기
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
#f = open("c\\work\\test.txt", "rt", encoding="utf-8")
f = open(r"c:\work\test.txt", "rt", encoding="utf-8")  # 이스케이프 문자 사용
print(f.read())  # 전체 읽기
f.close()

