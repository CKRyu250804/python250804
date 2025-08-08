# product_manager.py

import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)

DB_NAME = "products.db"

class ProductManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("전자제품 관리 프로그램")
        self.resize(500, 400)
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()
        self.init_ui()
        self.load_data()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MyProducts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def init_ui(self):
        layout = QVBoxLayout()

        # 입력창
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.price_input = QLineEdit()
        form_layout.addWidget(QLabel("이름:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("가격:"))
        form_layout.addWidget(self.price_input)
        layout.addLayout(form_layout)

        # 버튼
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("추가")
        self.update_btn = QPushButton("수정")
        self.delete_btn = QPushButton("삭제")
        self.search_btn = QPushButton("검색")
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.update_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.search_btn)
        layout.addLayout(btn_layout)

        # 테이블
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "이름", "가격"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.table, stretch=1)  # stretch 추가로 하단에 고정

        self.setLayout(layout)

        # 이벤트 연결
        self.add_btn.clicked.connect(self.add_product)
        self.update_btn.clicked.connect(self.update_product)
        self.delete_btn.clicked.connect(self.delete_product)
        self.search_btn.clicked.connect(self.search_product)
        self.table.cellClicked.connect(self.table_item_selected)

        self.selected_id = None

    def load_data(self, products=None):
        if products is None:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM MyProducts")
            products = cursor.fetchall()
        self.table.setRowCount(0)
        for row_data in products:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, data in enumerate(row_data):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

    def add_product(self):
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "이름과 가격(숫자)을 올바르게 입력하세요.")
            return
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO MyProducts (name, price) VALUES (?, ?)", (name, int(price)))
        self.conn.commit()
        self.load_data()
        self.clear_inputs()

    def update_product(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "선택 오류", "수정할 항목을 선택하세요.")
            return
        name = self.name_input.text().strip()
        price = self.price_input.text().strip()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "이름과 가격(숫자)을 올바르게 입력하세요.")
            return
        cursor = self.conn.cursor()
        cursor.execute("UPDATE MyProducts SET name=?, price=? WHERE id=?", (name, int(price), self.selected_id))
        self.conn.commit()
        self.load_data()
        self.clear_inputs()

    def delete_product(self):
        if self.selected_id is None:
            QMessageBox.warning(self, "선택 오류", "삭제할 항목을 선택하세요.")
            return
        reply = QMessageBox.question(self, "삭제 확인", "정말 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM MyProducts WHERE id=?", (self.selected_id,))
            self.conn.commit()
            self.load_data()
            self.clear_inputs()

    def search_product(self):
        name = self.name_input.text().strip()
        cursor = self.conn.cursor()
        if name:
            cursor.execute("SELECT * FROM MyProducts WHERE name LIKE ?", ('%' + name + '%',))
        else:
            cursor.execute("SELECT * FROM MyProducts")
        products = cursor.fetchall()
        self.load_data(products)

    def table_item_selected(self, row, column):
        self.selected_id = int(self.table.item(row, 0).text())
        self.name_input.setText(self.table.item(row, 1).text())
        self.price_input.setText(self.table.item(row, 2).text())

    def clear_inputs(self):
        self.name_input.clear()
        self.price_input.clear()
        self.selected_id = None

    def closeEvent(self, event):
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductManager()
    window.show()
    sys.exit(app.exec_())