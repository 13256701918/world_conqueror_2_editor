

from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from  read_and_save import read

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def enterEvent(self, event):
        print('我进到widget里面啦')

    def closeEvent(self, event):
        print('我要消失啦')

    def moveEvent(self, event):
        print('别动我')

    def showEvent(self, event):
        print('我马上出现')

class country(QWidget):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.window1 = MyWidget()

		# self.window.setFixedSize(400, 300)
		self.btn_dialog01 = QPushButton('第一个战役方')
		self.btn_dialog01.clicked.connect(self.openMessageBox01)
		self.btn_dialog02 = QPushButton('打开非模式对话框02')
		self.btn_dialog02.clicked.connect(self.openMessageBox02)
		self.btn_dialog03 = QPushButton('打开模式对话框03')
		self.btn_dialog03.clicked.connect(self.openMessageBox03)

		self.layout = QGridLayout()
		self.layout.addWidget(self.btn_dialog01, 1, 1)
		self.layout.addWidget(self.btn_dialog02, 1, 2)
		self.layout.addWidget(self.btn_dialog03, 1, 3)
		self.setLayout(self.layout)

		self.defult= read()
		print(self.defult)
		print(self.defult['commander'])

		self.combobox_id = QComboBox()
		self.label_id = QLabel('势力')
		self.id = ['de1', 'de2', 'de3', 'ru1', 'ru2','am']
		self.combobox_id.addItems(self.id)
		self.combobox_id.setCurrentText(self.defult['id'])
		# self.combobox_id.setCurrentText('ru2')
		self.layout_id=QHBoxLayout()
		self.layout_id.addWidget(self.label_id)
		self.layout_id.addWidget(self.combobox_id)

		print(self.combobox_id.currentText())

		self.combobox_name = QComboBox()
		self.label_name = QLabel('国家')
		self.name = ['gb','am','fr','ca','de','it','ru','ro','bg','hu','fl','tr','es','pt','se','ch']
		self.combobox_name.addItems(self.name)
		self.combobox_name.setCurrentText(self.defult['name'])
		self.layout_name=QHBoxLayout()
		self.layout_name.addWidget(self.label_name)
		self.layout_name.addWidget(self.combobox_name)

		print(self.combobox_id.currentText())

		self.combobox_commander = QComboBox()
		self.label_commander = QLabel('指挥官')
		self.commander = ['common1', 'Rommel', 'Guderian', 'Zhukov', 'Rokossovsky', 'common2', 'common2','Patton']
		self.combobox_commander.addItems(self.commander)
		self.combobox_commander.setCurrentText(self.defult['commander'])
		self.layout_commander=QHBoxLayout()
		self.layout_commander.addWidget(self.label_commander)
		self.layout_commander.addWidget(self.combobox_commander)

		self.combobox_ai = QComboBox()
		self.label_ai = QLabel('电脑或玩家控制')
		self.ai = ['0', '1', '1', '1', '1', '1', '1']
		self.combobox_ai.addItems(self.ai)
		self.combobox_ai.setCurrentText(self.defult['ai'])
		self.layout_ai=QHBoxLayout()
		self.layout_ai.addWidget(self.label_ai)
		self.layout_ai.addWidget(self.combobox_ai)

		self.combobox_defeated = QComboBox()
		self.label_defeated = QLabel('获胜条件')
		self.defeated = ['land','army' ]
		self.combobox_defeated.addItems(self.defeated)
		self.combobox_defeated.setCurrentText(self.defult['defeated'])
		self.layout_defeated=QHBoxLayout()
		self.layout_defeated.addWidget(self.label_defeated)
		self.layout_defeated.addWidget(self.combobox_defeated)

		self.combobox_taxfactor = QComboBox()
		self.label_taxfactor = QLabel('税率')
		self.taxfactor = ['1.000000','1.200000','1.200000','1.500000','1.800000','2.000000','1.200000']
		self.combobox_taxfactor.addItems(self.taxfactor)
		self.combobox_taxfactor.setCurrentText(self.defult['taxfactor'])
		self.layout_taxfactor=QHBoxLayout()
		self.layout_taxfactor.addWidget(self.label_taxfactor)
		self.layout_taxfactor.addWidget(self.combobox_taxfactor)

		self.combobox_techlevel = QComboBox()
		self.label_techlevel = QLabel('科技水平')
		self.techlevel= ['1','2','3','4']
		self.combobox_techlevel.addItems(self.techlevel)
		self.combobox_techlevel.setCurrentText(self.defult['techlevel'])
		self.layout_techlevel=QHBoxLayout()
		self.layout_techlevel.addWidget(self.label_techlevel)
		self.layout_techlevel.addWidget(self.combobox_techlevel)

		self.combobox_alliance = QComboBox()
		self.label_alliance = QLabel('阵营')
		self.alliance = ['1','2','3','4']
		self.combobox_alliance.addItems(self.alliance)
		self.combobox_alliance.setCurrentText(self.defult['alliance'])
		self.layout_alliance=QHBoxLayout()
		self.layout_alliance.addWidget(self.label_alliance)
		self.layout_alliance.addWidget(self.combobox_alliance)

		self.combobox_color = QComboBox()
		self.label_color = QLabel('颜色')
		self.color = ['pink','red','darkred','darkpink']
		self.combobox_color.addItems(self.color)
		self.layout_color=QHBoxLayout()
		self.layout_color.addWidget(self.label_color)
		self.layout_color.addWidget(self.combobox_color)

		self.layout = QVBoxLayout()

		self.layout.addLayout(self.layout_id)
		self.layout.addLayout(self.layout_name)
		self.layout.addLayout(self.layout_commander)
		self.layout.addLayout(self.layout_ai)
		self.layout.addLayout(self.layout_defeated)
		self.layout.addLayout(self.layout_taxfactor)
		self.layout.addLayout(self.layout_techlevel)
		self.layout.addLayout(self.layout_alliance)
		self.layout.addLayout(self.layout_color)
		self.window1.setLayout(self.layout)



	def save_one(self):
		print('sfsf')

	@Slot()
	def openMessageBox01(self):
		# 生成一个view
		self.combobox_id.activated.connect(print(self.combobox_id.currentText()))
		# self.combobox.activated.connect(print(self.combobox.currentText()))
		# print(self.dic)
		self.window1.show()
		# self.window1.closeEvent(print('t'))




	@Slot()
	def openMessageBox02(self):
		messagebox = QMessageBox(self)
		messagebox.setText('content03')
		messagebox.exec_()
		print('after03')

	@Slot()
	def openMessageBox03(self):
		messagebox = QMessageBox(self)
		messagebox.setText('content03')
		messagebox.exec_()
		print('after03')




app = QApplication()
widget = country()
widget.show()
app.exec_()

# print(widget.dic)
