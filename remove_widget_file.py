from info import *
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtGui import QPainter, QBrush, QColor,QPixmap,QPalette
import os
from all_dic import *
from  read_and_save import read,save,read_contrylist
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from functools import partial
from other_rs import *
from global_thing import mainwindow,remove_widget_list

def remove_widget(current_type=None):
	if remove_widget_list is not []:
		for widget,type in remove_widget_list:
			if current_type == type:
				if widget.delete_widget is not None:
					widget.delete_widget.close()
				if widget.delete_mainwidget is not None:
					mainwindow.removeDockWidget(widget.delete_mainwidget)




