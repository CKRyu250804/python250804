# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

f = open("todayhumor.txt", "a+", encoding="utf-8")
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for i in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(i)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        #title = span2.text 
                        title = item.find('a').text.strip()  # 문자열 양쪽 공백 제거
                        href = item.find('a')['href']  # <a> 태그의 href 속성 추출
                        if (re.search('윤', title)):
                        #         print(title)
                        #         f.write(title + "\n")
                        #         #print('https://www.clien.net'  + item['href'])
                            f.write(title + "\t" )
                            f.write('https://www.todayhumor.co.kr' + href + "\n")
                            print(title)
                except:
                        pass
        
f.close()  # 파일 닫기

#<td class="subject">
#<a href="/board/view.php?table=bestofbest&amp;no=480470&amp;s_no=480470&amp;page=1" target="_top">길바닥 낙서</a><span class="list_memo_count_span"> [6]</span>  <span style="margin-left:4px;"><img src="https://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span> <span style="color:#999">5일</span></td>
#<a href="/board/view.php?table=bestofbest&amp;no=480470&amp;s_no=480470&amp;page=1" target="_top">길바닥 낙서</a>