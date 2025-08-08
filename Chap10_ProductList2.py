import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# UI 파일 로드
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # DB 연결
        self.connect_db()
        
        #초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        #QTableWidget 설정
        self.setup_table_widget()
        
        #시그널 연결
        self.setup_signals()

    def connect_db(self):
        """DB 연결 및 초기화"""
        try:
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
            if not os.path.exists("ProductList.db"):
                self.cur.execute(
                    "CREATE TABLE Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Price INTEGER NOT NULL);"
                )
                self.con.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"DB 연결 오류: {str(e)}")
            sys.exit(1)

    def setup_table_widget(self):
        """테이블 위젯 초기 설정"""
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        self.tableWidget.setRowCount(30)  # 행 수 설정
        self.tableWidget.setTabKeyNavigation(False)

    def setup_signals(self):
        """시그널 설정"""
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        """제품 추가"""
        try:
            name = self.prodName.text().strip()
            price = self.prodPrice.text().strip()
            
            if not name or not price:
                QMessageBox.warning(self, "입력 오류", "제품명과 가격을 모두 입력하세요.")
                return
                
            try:
                price = int(price)
                if price < 0:
                    raise ValueError("가격은 0보다 커야 합니다.")
            except ValueError as e:
                QMessageBox.warning(self, "입력 오류", "올바른 가격을 입력하세요.")
                return

            self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", 
                (name, price))
            self.con.commit()
            self.getProduct()
            self.clear_inputs()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"추가 중 오류 발생: {str(e)}")
            self.con.rollback()

    def updateProduct(self):
        """제품 수정"""
        try:
            id = self.prodID.text().strip()
            name = self.prodName.text().strip()
            price = self.prodPrice.text().strip()
            
            if not all([id, name, price]):
                QMessageBox.warning(self, "입력 오류", "모든 필드를 입력하세요.")
                return
                
            try:
                id = int(id)
                price = int(price)
                if price < 0:
                    raise ValueError("가격은 0보다 커야 합니다.")
            except ValueError:
                QMessageBox.warning(self, "입력 오류", "올바른 ID와 가격을 입력하세요.")
                return

            self.cur.execute("UPDATE Products SET name=?, price=? WHERE id=?;", 
                (name, price, id))
            if self.cur.rowcount == 0:
                QMessageBox.warning(self, "수정 오류", "해당 ID의 제품이 존재하지 않습니다.")
                return
                
            self.con.commit()
            self.getProduct()
            self.clear_inputs()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"수정 중 오류 발생: {str(e)}")
            self.con.rollback()

    def removeProduct(self):
        """제품 삭제"""
        try:
            id = self.prodID.text().strip()
            if not id:
                QMessageBox.warning(self, "입력 오류", "삭제할 제품의 ID를 입력하세요.")
                return

            reply = QMessageBox.question(self, '삭제 확인', 
                '정말로 이 제품을 삭제하시겠습니까?',
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.cur.execute("DELETE FROM Products WHERE id=?;", (id,))
                if self.cur.rowcount == 0:
                    QMessageBox.warning(self, "삭제 오류", "해당 ID의 제품이 존재하지 않습니다.")
                    return
                    
                self.con.commit()
                self.getProduct()
                self.clear_inputs()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"삭제 중 오류 발생: {str(e)}")
            self.con.rollback()

    def getProduct(self):
        """제품 목록 조회"""
        try:
            self.tableWidget.clearContents()
            self.cur.execute("SELECT * FROM Products;")
            
            for row, item in enumerate(self.cur):
                self.tableWidget.setItem(row, 0, self.create_right_aligned_item(str(item[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
                self.tableWidget.setItem(row, 2, self.create_right_aligned_item(str(item[2])))
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"조회 중 오류 발생: {str(e)}")

    def create_right_aligned_item(self, text):
        """우측 정렬된 테이블 아이템 생성"""
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        return item

    def clear_inputs(self):
        """입력 필드 초기화"""
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()

    def doubleClick(self, index):
        """더블클릭 이벤트 처리"""
        row = index.row()
        self.prodID.setText(self.tableWidget.item(row, 0).text())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())

    def closeEvent(self, event):
        """프로그램 종료 시 리소스 정리"""
        if hasattr(self, 'con'):
            self.cur.close()
            self.con.close()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()