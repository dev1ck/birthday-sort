
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon
from birthday_ui import Ui_widget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.__initUI()

    def __initUI(self):
        icon_path = os.path.join(os.path.dirname(os.path.abspath(sys.executable)), "resources", "icon.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.resize(662, 482)
        self.setWindowTitle("생일자 정렬기")
        self.ui.pushButton.clicked.connect(self.__push_button_clicked)

    def __push_button_clicked(self):
        birthday_sorter = BirthdaySorter(self.ui.inputPlainText.toPlainText())
        string_list = birthday_sorter.get_string_list()
        self.ui.outputPlainText.setPlainText("\n".join(string_list))
        
class BirthdaySorter:
    def __init__(self, str_name):
        self.__list_name = list(str_name.split())
    
    def __sort(self):
        self.__list_name.sort()
        
    def __split_list(self):
        def split_half(lst):
            mid = len(lst) // 2
            return lst[:mid], lst[mid:]

        half = len(self.__list_name) // 2
        first_half, second_half = split_half(self.__list_name)
        first_half_1, first_half_2 = split_half(first_half)
        second_half_1, second_half_2 = split_half(second_half)

        return first_half_1, first_half_2, second_half_1, second_half_2

        
    def get_string_list(self):
        self.__sort()
        list_A, list_B, list_C, list_D = self.__split_list()
        return [
            ' '.join(list_A),
            ' '.join(list_B),
            "",
            ' '.join(list_C),
            ' '.join(list_D)
        ]
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())