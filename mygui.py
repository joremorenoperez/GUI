from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(500,200,700,500) #Set geometry of window
        self.setWindowTitle('Interfaz') #Set title of window
        self.initUI() #When a window is created, it is already initialized

    def initUI(self):
        self.label = QtWidgets.QLabel(self) #Define a label called 'label' and show on 'MyWindow' (self/instance of QtMainWindow)
        self.label.setText('Etiqueta') #Set label text
        self.label.move(50,50) #Set position within window

        self.button = QtWidgets.QPushButton(self) #Define a button named 'button'
        self.button.setText('Púlsame')
        self.button.move(500,200)
        self.button.clicked.connect(self.click) #When 'button' recieves signal 'clicked' (PyQt object), function 'click' is called

    def click(self):
        self.label.setText('Se ha pulsado el botón') #Changes text on 'label' when 'button' is clicked
        self.label.adjustSize() #Adjusts label size to fit all text

def window():
    app = QApplication(sys.argv)
    win = MyWindow() #Retrieve previously created window (class) 

    win.show()
    sys.exit(app.exec_()) #Gives a clean exit

window()