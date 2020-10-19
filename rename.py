#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:37:51 2019

@author: jiuyang.wei
"""
from PySide2.QtWidgets import QPushButton,QApplication, QWidget,QLabel,QLineEdit ,QSpinBox, QListView, QVBoxLayout, QHBoxLayout,QItemDelegate
from PySide2.QtCore import QStringListModel
from PySide2.QtCore import Signal, Slot

def rename():
    class MyDelegate(QItemDelegate):
        def __init__(self, parent=None):
            super().__init__(parent)

        def createEditor(self, parent, option, index):
            string = QLineEdit(parent)
            return string

        def setEditorData(self, editor, index):
            value = index.model().data(index)
            editor.setText(value)

        def setModelData(self, editor, model, index):
            value = editor.text()
            model.setData(index, value)

        def updateEditorGeometry(self, editor, option, index):
            editor.setGeometry(option.rect)


    class rename_one(QWidget):

        def __init__(self,parent=None):
            super().__init__(parent)


            self.mydelegate = MyDelegate()

            self.listview = QListView()
            self.mymodel = QStringListModel()
            self.listview.setModel(self.mymodel)
            # 设置我们自己的delegate
            self.listview.setItemDelegate(self.mydelegate)
            self.battle_allies=r'battle_allies'
            self.battle_allies_list=[]
            for i in range (1,11):
                self.battle_allies_list.append(self.battle_allies+'%s.xml'%str(i))
            self.mymodel.setStringList(self.battle_allies_list)
            print(self.battle_allies_list)
            print(self.mymodel.index(2,0).data())



    app = QApplication()
    window = QWidget()
    print('s')
    window.setFixedSize(400, 300)
    setname1=rename_one()
    setname2=rename_one()
    layout=QVBoxLayout()
    layout.addWidget(setname1)
    # layout.addWidget(setname2)

    window.setLayout(layout)
    window.show()

    app.exec_()


if __name__ == '__main__':
    rename()