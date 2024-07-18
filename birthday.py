import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice


class BirthdayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # .ui 파일 로드
        self.ui = self.load_ui()
        self.setWindowTitle("생일자 정렬")
        self.setCentralWidget(self.ui)

        # 버튼 클릭 이벤트 연결
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

    def load_ui(self):
        loader = QUiLoader()
        file = QFile("birthday.ui")
        file.open(QIODevice.ReadOnly)
        ui = loader.load(file)
        file.close()
        return ui

    def on_button_clicked(self):
        # 버튼 클릭 시 실행할 로직
        pass

    def run(self):
        self.ui.show()
        
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def main():
    app = QApplication(sys.argv)
    birthday_app = BirthdayApp()
    birthday_app.run()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


# with open('birthday.txt', 'r', encoding='UTF8') as f:
#         list_name =  list(f.read().split())
#         list_name.sort()
#         list_A, list_B = split_list(list_name)
        
#     with open('birthday.txt', 'w', encoding='UTF8') as f:
#         text = ''
#         cnt = 0
    
#         for name in list_A:
#             text += name + ' '
#             cnt += 1
#             if cnt==len(list_A)//2:
#                 text = text.rstrip()
#                 text += '\n'
        
#         text = text.rstrip()
#         text += '\n\n'
#         cnt = 0
        
#         for name in list_B:
#             text += name + ' '
#             cnt += 1
#             if cnt==len(list_B)//2:
#                 text = text.rstrip()
#                 text += '\n'
            
#         text = text.rstrip()
#         f.write(text)