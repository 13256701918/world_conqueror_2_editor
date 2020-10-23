#inlet
from PySide2.QtWidgets import QApplication, QLabel,QMainWindow,QDockWidget,QWidget
from PySide2.QtCore import Qt
from all_dic import *
from other_rs import get_armydef
global mainwindow

global remove_widget_list
remove_widget_list=[]



app=QApplication()
mainwindow = QMainWindow()
mainwindow.setWindowTitle('world conqueror 2')
# Qmcwidget = QDockWidget()
# Qmcwidget.setWidget(model_choosen())

# ainwindow.addDockWidget(Qt.LeftDockWidgetArea,Qmcwidget)
mainwindow.show()
# app.exec_()
