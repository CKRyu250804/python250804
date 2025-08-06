import sqlite3
import random

class ProductDB:
    def __init__(self, db_path=r"c:\work\electronics.db"):
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS ElectronicProduct(
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
        );
        """)
        self.con.commit()

    def insert_product(self, product_id, name, price):
        self.cur.execute(
            "INSERT INTO ElectronicProduct (product_id, name, price) VALUES (?, ?, ?);",
            (product_id, name, price)
        )
        self.con.commit()

    def update_product(self, product_id, name=None, price=None):
        if name is not None:
            self.cur.execute(
                "UPDATE ElectronicProduct SET name=? WHERE product_id=?;",
                (name, product_id)
            )
        if price is not None:
            self.cur.execute(
                "UPDATE ElectronicProduct SET price=? WHERE product_id=?;",
                (price, product_id)
            )
        self.con.commit()

    def delete_product(self, product_id):
        self.cur.execute(
            "DELETE FROM ElectronicProduct WHERE product_id=?;",
            (product_id,)
        )
        self.con.commit()

    def select_all(self):
        self.cur.execute("SELECT * FROM ElectronicProduct;")
        return self.cur.fetchall()

    def select_by_id(self, product_id):
        self.cur.execute("SELECT * FROM ElectronicProduct WHERE product_id=?;", (product_id,))
        return self.cur.fetchone()

    def close(self):
        self.con.close()

# 샘플 데이터 100개 생성 및 입력
def generate_sample_products(n=100):
    products = []
    for i in range(1, n+1):
        name = f"전자제품{i}"
        price = random.randint(10000, 1000000)
        products.append((i, name, price))
    return products

if __name__ == "__main__":
    db = ProductDB()
    # 기존 데이터 삭제
    db.cur.execute("DELETE FROM ElectronicProduct;")
    db.con.commit()
    # 샘플 데이터 입력
    sample_products = generate_sample_products(100)
    for pid, name, price in sample_products:
        db.insert_product(pid, name, price)

    # 데이터 조회 예시
    print("전체 제품 목록:")
    for row in db.select_all():
        print(row)

    # 제품 수정 예시
    db.update_product(1, name="수정된제품", price=55555)
    print("\n수정 후 1번 제품:", db.select_by_id(1))

   # 제품 삭제 예시
    db.delete_product(2)
    print("\n2번 제품 삭제 후 전체 목록 일부:")
    for row in db.select_all()[:5]:
        print(row)

    db.close()