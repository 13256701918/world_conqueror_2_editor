
from PySide2.QtGui import QPainter, QBrush, QColor,QPixmap,QPalette
import os
from all_dic import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from remove_widget_file import remove_widget,remove_widget_list
from country_changed_file import country_changed
from global_thing import mainwindow

class model_choosen(QWidget):
    def __init__(self,parent=None,delete_widget=None):
        super().__init__(parent)
        self.type = 'battle_axis'
        self.delete_mainwidget=delete_widget
        self.layout_one =None
        self.delete_widget = None
        self.label_img = None
        self.file_name = None
        self.old_file_name =None

        self.combobox_name = QComboBox()
        self.label_name = QLabel('模式')
        self.name = ['轴心国战役','盟军战役','北约战役','华约战役','征服']
        self.combobox_name.addItems(self.name)
        self.layout_name = QHBoxLayout()
        self.layout_name.addWidget(self.label_name)
        self.layout_name.addWidget(self.combobox_name)
        # self.combobox_name.activated.connect(self.choosen)
        self.combobox_id = QComboBox()
        self.label_id = QLabel('关卡')
        self.combobox_id.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.layout_id = QHBoxLayout()
        self.layout_id.addWidget(self.label_id)
        self.layout_id.addWidget(self.combobox_id)

        self.layout_one = QVBoxLayout()
        self.layout_one.addLayout(self.layout_name)
        self.layout_one.addLayout(self.layout_id)

        self.image = QPixmap('image.jpg')
        self.label_img = QLabel()
        # 设置标签起始位置和大小
        self.label_img.setGeometry(5, 5, 80, 80)
        # 用来设置图像
        self.label_img.setPixmap(self.image)

        self.label_img.setScaledContents(True)
        self.label_img.setMaximumSize(500,300)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layout_name)
        self.layout.addLayout(self.layout_one)
        self.layout.addWidget(self.label_img)

        self.setLayout(self.layout)

        self.combobox_name.activated.connect(self.get_file_name)
        self.combobox_id.activated.connect(self.get_file_name)
        self.combobox_name.activated.connect(self.change_id)

    def get_file_name(self):
        self.id=self.combobox_id.currentText() if self.combobox_id.currentText() is not '' else 1
        self.name =battle_dic[self.combobox_name.currentText()]
        if (self.name=='conquest'):
            self.file_name=self.name+'_%s.xml'%self.id
        else:
            self.file_name = self.name + '%s.xml'%self.id

        if self.file_name != self.old_file_name:
            self.select()
            self.change_img()
        self.old_file_name = self.file_name

    def change_img(self):
        if os.path.exists(self.file_name[:-3]+'jpg'):
            print('change_img')
            self.image = QPixmap(self.file_name[:-3]+'jpg')

            # 用来设置图像
            self.label_img.setPixmap(self.image)



    def change_id(self):
        self.type=battle_dic[self.combobox_name.currentText()]
        self.combobox_id.clear()
        if self.type == 'battle_axis':
            self.combobox_id.addItems(["1","2","3","4","5","6","7","8","9","10"])
        if self.type == 'battle_allies':
            self.combobox_id.addItems(["1","2","3","4","5","6","7","8","9","10"])
        if self.type == 'battle_nato':
            self.combobox_id.addItems(["1","2","3","4","5","6","7"])
        if self.type == 'battle_wto':
            self.combobox_id.addItems(["1","2","3","4","5","6","7"])
        if self.type == 'conquest':
            self.combobox_id.addItems(["1","2","3","4","5","6","7","8"])


    def select(self):
        remove_widget(current_type="model_choosen")
        self.delete_widget=country_changed(file_name=self.file_name)
        Qleftwidget = QDockWidget()
        Qleftwidget.setWidget(self.delete_widget)
        mainwindow.addDockWidget(Qt.LeftDockWidgetArea, Qleftwidget)
        self.delete_mainwidget = Qleftwidget
        remove_widget_list.append((self,"model_choosen"))




if __name__=='__main__':
    app = QApplication()
    window = model_choosen()
    window.show()
    app.exec_()
