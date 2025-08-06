#  demoOS.py

from os.path import *
from os import *
import glob

fName = "sample.txt"
print(abspath(fName))   # 절대경로 출력
print(basename(r"c:\work\test.txt"))   # 파일명 출력

if(exists(r"c:\python310\python.exe")):   # 파일 존재 여부 확인
    print(getsize(r"c:\python310\python.exe"))   # 파일 크기 출력
else:
    print("파일이 존재하지 않습니다.")

print("운영체제명:", name)   # 운영체제명 출력
print("환경변수:", environ)   # 환경변수 출력
system("notepad.exe")   # 메모장 실행

glob.glob("*.*")
print(glob.glob("*.py"))   # 현재 디렉터리의 모든 파이썬 파일 목록 출력
for item in glob.glob("*.py"):
    print(item) # 현재 디렉터리의 모든 파이썬 파일 목록 출력

