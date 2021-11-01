import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
import face_capture as fc
import train as tr
import faces as fa
import dbutilityfunctions as du
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login.ui", self)
        self.faceid.clicked.connect(self.gotofaceid)
        self.register_2.clicked.connect(self.gotoregister)
        self.login.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    

    def gotoregister(self):

        t = self.user_name.text()
        password = self.password.text()
        t_value = du.validate_login(t, password)
        if(t_value):
            fc.username(t)
            tr.training()
        else:
            self.error.setText("Invalid Login-Id or Password!!!!")
    
    def gotofaceid(self):

        x = fa.faces()
        print(x)
        
    def gotologin(self):
        u = self.user_name.text()
        p = self.password.text()
        t_value = du.validate_login(u, p)
        if(len(u)==0 or len(p)==0):
            self.error.setText("Please input all fields!!!!")
        elif(not t_value):
            self.error.setText("Incorrect Password!!!!")
        else:
            self.error.setText("Logged In")
            print("Loggedin")
        
        


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