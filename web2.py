# web2.py

from bs4 import BeautifulSoup  #크롤링
import urllib.request   #웹 페이지 요청
import re    #정규 표현식, filtering용

url = "https://www.clien.net/service/board/sold"

data = urllib.request.urlopen(url).read()  #웹 페이지 요청
soup = BeautifulSoup(data, "html.parser")  #HTML 파싱

for tag in soup.find_all('span', attrs={'data-role': 'list-title-text'}):
    title = tag.text.strip()  # 문자열 양쪽 공백 제거
    #title = title.replace('\n', '')  # 줄바꿈 제거
    if re.search(r'아이폰', title):  # '아이폰'이 포함된 제목만 출력
        print(title)
# <span class="subject_fixed" data-role="list-title-text" title="아이폰 13미니 256 팝니다">
#     아이폰 13미니 256 팝니다
# </span>

