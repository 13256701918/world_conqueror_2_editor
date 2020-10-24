
from PySide2.QtWidgets import QApplication, QLabel,QMainWindow,QDockWidget,QWidget,QCalendarWidget
from PySide2.QtCore import Qt
from model_choosen_file import model_choosen
from global_thing import mainwindow,app


Qmcwidget = QDockWidget()
Qmcwidget.setWidget(model_choosen())


mainwindow.addDockWidget(Qt.LeftDockWidgetArea,Qmcwidget)

mainwindow.show()
app.exec_()