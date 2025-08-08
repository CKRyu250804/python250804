# demoForm2.py
# demoForm2.ui (화면) + demoForm2.py (로직) 파일을 연결하는 코드입니다.
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup  #크롤링
import urllib.request   #웹 페이지 요청
import re    #정규 표현식, filtering용

form_class = uic.loadUiType("demoForm2.ui")[0]  #design한 파일 loading

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # UI 설정
    def firstClick(self):
        # self.label.setText("첫번째 버튼 클릭")
        # f = open("todayhumor.txt", "a+", encoding="utf-8")
        # #User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
        # hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

        # for i in range(1,11):
        #         #오늘의 유머 베스트 게시판
        #         data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(i)
        #         #웹브라우져 헤더 추가 
        #         req = urllib.request.Request(data, \
        #                                     headers = hdr)
        #         data = urllib.request.urlopen(req).read()
        #         #한글이 깨지는 경우
        #         page = data.decode('utf-8', 'ignore')
        #         soup = BeautifulSoup(page, 'html.parser')
        #         list = soup.find_all('td', attrs={'class':'subject'})

        #         for item in list:
        #                 try:
        #                         #<a class='list_subject'><span>text</span><span>text</span>
        #                         # span = item.contents[1]
        #                         # span2 = span.nextSibling.nextSibling
        #                         #title = span2.text 
        #                         title = item.find('a').text.strip()  # 문자열 양쪽 공백 제거
        #                         href = item.find('a')['href']  # <a> 태그의 href 속성 추출
        #                         if (re.search('윤', title)):
        #                         #         print(title)
        #                         #         f.write(title + "\n")
        #                         #         #print('https://www.clien.net'  + item['href'])
        #                             f.write(title + "\t" )
        #                             f.write('https://www.todayhumor.co.kr' + href + "\n")
        #                             print(title)
        #                 except:
        #                         pass
                
        # f.close()  # 파일 닫기
        # HTML 파일로 저장
        f = open("todayhumor.html", "w", encoding="utf-8")
        # HTML 기본 구조 작성
        f.write("""
        <html>
        <head>
            <meta charset='utf-8'>
            <title>오늘의 유머 검색결과</title>
        </head>
        <body>
        """)
        
        #User-Agent를 조작하는 경우
        hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

        for i in range(1,11):
            data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(i)
            req = urllib.request.Request(data, headers = hdr)
            data = urllib.request.urlopen(req).read()
            page = data.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all('td', attrs={'class':'subject'})

            for item in list:
                try:
                    title = item.find('a').text.strip()
                    href = item.find('a')['href']
                    if (re.search('윤', title)):
                        full_url = 'https://www.todayhumor.co.kr' + href
                        # HTML 링크 형식으로 저장
                        f.write(f'<p><a href="{full_url}" target="_blank">{title}</a></p>\n')
                        print(title)
                except:
                    pass
        
        # HTML 문서 닫기
        f.write("""
        </body>
        </html>
        """)
        f.close()
        self.label.setText("오늘의 유머 베오베 저장 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")

if __name__ == "__main__": #직접 모듈을 실행할 경우만
    app = QApplication(sys.argv) #QApplication 객체 생성
    demoWindow = DemoForm() # DemoForm 클래스의 인스턴스 생성
    demoWindow.show() # DemoForm 창을 화면에 표시
    app.exec_() # 이벤트 루프 실행
