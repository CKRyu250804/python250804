# db1.py
import sqlite3

#연결객체를 return
#con = sqlite3.connect(":memory:")
con = sqlite3.connect(r"c:\work\sample.db")  # 데이터베이스 파일 연결
#커서객체 return
cur = con.cursor()
#table 생성
#cur.execute("create table PhoneBook(name text, phone text);")
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook(
    name TEXT,
    phone TEXT
);
""")
# data insert (중복 방지)
cur.execute("""
INSERT INTO PhoneBook(name, phone)
SELECT ?, ?
WHERE NOT EXISTS (
    SELECT 1 FROM PhoneBook WHERE name = ? AND phone = ?
);
""", ('홍길동', '123-4567', '홍길동', '123-4567'))

# 입력 parameter 처리 (중복 방지)
name = "이순신"
phone = "987-6543"
cur.execute("""
INSERT INTO PhoneBook(name, phone)
SELECT ?, ?
WHERE NOT EXISTS (
    SELECT 1 FROM PhoneBook WHERE name = ? AND phone = ?
);
""", (name, phone, name, phone))

# 여러건 입력 (중복 방지)
datalist = [("김길동", "010-111"), ("전우치", "001-333")]
for name, phone in datalist:
    cur.execute("""
    INSERT INTO PhoneBook(name, phone)
    SELECT ?, ?
    WHERE NOT EXISTS (
        SELECT 1 FROM PhoneBook WHERE name = ? AND phone = ?
    );
    """, (name, phone, name, phone))

#data 조회
cur.execute("select * from PhoneBook;")
lst_name = []
lst_phone = []
for row in cur:
    lst_name.append(row[0])
    lst_phone.append(row[1])
    print(row)

print("name :",lst_name)
print("phone:", lst_phone)

cur.execute("""
DELETE FROM PhoneBook
WHERE ROWID NOT IN (
    SELECT MIN(ROWID)
    FROM PhoneBook
    GROUP BY name, phone
);
""")
# commit
con.commit()
con.close()  # 연결 종료

