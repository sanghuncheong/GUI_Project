import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI('Ready')

    def initUI(self, status_msg):

        self.statusBar().showMessage(status_msg)
        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    import time
    app = QApplication(sys.argv)
    ex = MyApp()

    in_msg_status = 'in put 1!!'
    MyApp.initUI(ex, status_msg=in_msg_status)

    time.sleep(1)
    in_msg_status = 'in put 2!!'
    MyApp.initUI(ex, status_msg=in_msg_status)

    time.sleep(1)
    in_msg_status = 'in put 3!!'
    MyApp.initUI(ex, status_msg=in_msg_status)
    sys.exit(app.exec_())

