
from PySide2.QtWidgets import QApplication, QLabel,QMainWindow,QDockWidget,QWidget,QCalendarWidget
from PySide2.QtCore import Qt
from all_dic import *
from other_rs import get_armydef
from model_choosen_file import model_choosen
from global_thing import mainwindow,app

# app = QApplication()
# print(type(mainwindow))
Qmcwidget = QDockWidget()
Qmcwidget.setWidget(model_choosen())
# Qmdwidget = QDockWidget()
# Qmdwidget.setWidget(QCalendarWidget())
# print(type(mainwindow))
mainwindow.addDockWidget(Qt.LeftDockWidgetArea,Qmcwidget)
# mainwindow.addDockWidget(Qt.RightDockWidgetArea,Qmdwidget)

mainwindow.show()
app.exec_()