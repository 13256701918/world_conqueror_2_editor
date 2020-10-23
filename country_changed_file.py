from functools import partial
from country_model_file import country_model
from info import *
from PySide2.QtWidgets import QApplication, QLabel,QMainWindow,QDockWidget,QWidget
from  read_and_save import read,save,read_contrylist
from global_thing import mainwindow
from remove_widget_file import remove_widget,remove_widget_list

class country_changed(QWidget):
    def __init__(self,parent=None, test_widget=None,file_name="battle_axis1.xml"):
        super().__init__(parent)
        self.setMinimumSize(500, 300)
        self.file_name=file_name
        self.defult = read_contrylist(self.file_name)

        self.open_test = None
        self.test_widget = test_widget
        self.layout = QGridLayout()
        self.btn_list=[]

        for i in range(0,len(self.defult)):
            btn_temp=QPushButton('第%s个战斗方'%i)
            self.btn_list.append(btn_temp)
            self.btn_list[i].clicked.connect(partial(self.change_combat,i))
            self.layout.addWidget(btn_temp,i/5,i%5)
        self.setLayout(self.layout)

    @Slot()
    def change_combat(self,i):
        remove_widget(current_type="country_changed")
        self.delete_widget = country_model(self.test_widget,file_name=self.file_name,Number_Id=i)
        Qrightwidget = QDockWidget()
        Qrightwidget.setWidget(self.delete_widget)
        mainwindow.addDockWidget(Qt.RightDockWidgetArea, Qrightwidget)
        self.delete_mainwidget = Qrightwidget
        remove_widget_list.append((self,"country_changed"))
