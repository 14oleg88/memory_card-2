from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

app = QApplication([])

from window import*

def switch_screen():
    if answer_btn.text() == 'відповісти':
        group_box.hide
        result_box.show()
        answer_btn.setText('Наступне питання')
    else:
        result_box.hide()
        group_box.show()
        answer_btn.setText('відповісти')

answer_btn.clicked.connect(switch_screen)

window.show()
app.exec_()