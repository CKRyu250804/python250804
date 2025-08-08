# demoForm.py
# demoForm.ui (화면) + demoForm.py (로직) 파일을 연결하는 코드입니다.
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("demoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # UI 설정
        self.label.setText("첫번째 문자열 출력") # label 위젯에 문자열 출력

if __name__ == "__main__": #직접 모듈을 실행할 경우만
    app = QApplication(sys.argv) #QApplication 객체 생성
    demoWindow = DemoForm() # DemoForm 클래스의 인스턴스 생성
    demoWindow.show() # DemoForm 창을 화면에 표시
    app.exec_() # 이벤트 루프 실행
