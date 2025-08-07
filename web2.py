# web2.py

from bs4 import BeautifulSoup  #크롤링
import urllib.request   #웹 페이지 요청
import re    #정규 표현식, filtering용

# 파일로 저장
f = open("clien.txt", "a+", encoding="utf-8")
#url = "https://www.clien.net/service/board/sold"
#page 번호 생성
for i in range(0,10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    #print(url)
    data = urllib.request.urlopen(url).read()  #웹 페이지 요청
    soup = BeautifulSoup(data, "html.parser")  #HTML 파싱

    for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
        title = tag.text.strip()  # 문자열 양쪽 공백 제거
        #title = title.replace('\n', '')  # 줄바꿈 제거
        if re.search(r'맥북|아이패드', title):  # '아이폰'이 포함된 제목만 출력
            print(title)
            f.write(title + "\n")

f.close()  # 파일 닫기
# <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
#     아이폰 13미니 256 팝니다
# </span>

