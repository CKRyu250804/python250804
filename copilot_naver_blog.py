import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 뉴스 기사 제목 추출 (네이버 뉴스 영역의 구조에 맞게)
# titles = []
# for span in soup.select("span.sds-comps-text-type-body2"):
#     title = span.get_text(strip=True)
#     if title:
#         titles.append(title)

titles = soup.select('a.CZ2lJrtx8_tIIyyaEDkQ.IQnq6B4xVFZbhCOvK9Fy > span')

# 엑셀 파일 생성 및 데이터 저장
wb = Workbook()
ws = wb.active
ws.title = "네이버뉴스제목"
ws.append(["번호", "제목"])

for idx, t in enumerate(titles, 1):
    ws.append([idx, t.get_text(strip=True)])

wb.save("naverResult.xlsx")
print("신문기사 제목이 naverResult.xlsx 파일에 저장되었습니다.")



