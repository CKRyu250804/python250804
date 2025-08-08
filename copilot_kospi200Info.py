import requests
from bs4 import BeautifulSoup

def get_kospi200_top_stocks():
    # 네이버 금융 코스피200 페이지 URL
    url = "https://finance.naver.com/sise/entryJongmok.naver?&type=KPI200"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    
    stocks = []
    page = 1
    
    while True:
        # 각 페이지별 URL
        page_url = f"{url}&page={page}"
        res = requests.get(page_url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # 테이블 찾기
        table = soup.find("table", class_="type_1")
        if not table:
            break

        # 종목 정보 추출
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if len(cols) != 7:  # 헤더와 빈 행 제외
                continue
                
            # 종목코드 추출
            code = ""
            if cols[0].find("a"):
                code = cols[0].find("a")["href"].split("code=")[1]
            
            # 상승/하락 여부 확인
            change_class = cols[2].find("span")["class"][1] if cols[2].find("span") else ""
            is_up = "red" in change_class if change_class else False
            
            # 데이터 추출 및 정제
            name = cols[0].get_text(strip=True)
            if name:
                stocks.append({
                    "code": code,
                    "name": name,
                    "price": cols[1].get_text(strip=True).replace(",", ""),
                    "change": ("+" if is_up else "-") + cols[2].find("span").get_text(strip=True).replace(",", ""),
                    "rate": cols[3].get_text(strip=True),
                    "volume": cols[4].get_text(strip=True).replace(",", ""),
                    "amount": cols[5].get_text(strip=True).replace(",", ""),
                    "market_cap": cols[6].get_text(strip=True).replace(",", "")
                })
        
        # 다음 페이지 확인
        if not soup.find("td", class_="pgR"):
            break
            
        page += 1

    return stocks

if __name__ == "__main__":
    stocks = get_kospi200_top_stocks()
    for stock in stocks:
        print(stock)