import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
import face_capture as fc
import train as tr
import faces as fa

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login.ui", self)
        self.faceid.clicked.connect(self.gotofaceid)
        self.register_2.clicked.connect(self.gotoregister)
    

    def gotoregister(self):

        t = self.user_name.text()
        fc.username(t)
        tr.training()
    
    def gotofaceid(self):

        x = fa.faces()
        print(x)
        


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting app")