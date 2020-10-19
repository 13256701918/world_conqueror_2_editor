

from PySide2.QtCore import Signal, Slot
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from  read_and_save import read,save

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def enterEvent(self, event):
        pass
        # print('我进到widget里面啦')

    def closeEvent(self, event):
        pass
        # print('我要消失啦')

    def moveEvent(self, event):
        pass
        # print('别动我')

    def showEvent(self, event):
        pass
		# print('我马上出现')


class country_model(MyWidget):
	def __init__(self,parent=None,MapType='battle_allies',MapNum=1,Number_Id=0):
		super().__init__(parent)
		self.setMinimumSize(500,300)
		self.number_id=Number_Id

		if MapType =='conquest':
			self.filename=MapType+'_%s.xml'%str(MapNum)
		else:
			self.filename=MapType+'%s.xml'%str(MapNum)
		# print(self.filename)
		self.defult = read(self.filename,self.number_id)
		# print(self.defult)
		# print(type(self.defult))
		# print(self.defult['commander'])

		self.combobox_id = QComboBox()
		self.label_id = QLabel('势力')
		self.id = ['de1', 'de2', 'de3', 'ru1', 'ru2','ru3','gb','am','am1','am2','am3','cn','tw','nk','rk','gb','in','ja','au','ca','fr','ca','de','it','ru','ro','bg','hu','fl','tr','es','pt','se','ch']
		self.combobox_id.addItems(self.id)
		self.combobox_id.setCurrentText(self.defult['id'])
		# self.combobox_id.setCurrentText('ru2')
		self.layout_id=QHBoxLayout()
		self.layout_id.addWidget(self.label_id)
		self.layout_id.addWidget(self.combobox_id)

		# print(self.combobox_id.currentText())

		self.combobox_name = QComboBox()
		self.label_name = QLabel('国家')
		self.name = ['gb','am','fr','ca','de','it','ru','ro','bg','hu','fl','tr','es','pt','se','ch','am','ru','cn','tw','nk','rk','gb','in','ja','au','ca']
		self.combobox_name.addItems(self.name)
		self.combobox_name.setCurrentText(self.defult['name'])
		self.layout_name=QHBoxLayout()
		self.layout_name.addWidget(self.label_name)
		self.layout_name.addWidget(self.combobox_name)

		# print(self.combobox_id.currentText())

		self.combobox_commander = QComboBox()
		self.label_commander = QLabel('指挥官')
		self.commander = ['common1', 'Rommel', 'Guderian', 'Rokossovsky', 'common2','Patton','Zhukov','Nimitz','Montgomery','de Gaulle','Graziani','Peng']
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
		self.techlevel= ['1','2','3','4','5']
		self.combobox_techlevel.addItems(self.techlevel)
		self.combobox_techlevel.setCurrentText(self.defult['techlevel'])
		self.layout_techlevel=QHBoxLayout()
		self.layout_techlevel.addWidget(self.label_techlevel)
		self.layout_techlevel.addWidget(self.combobox_techlevel)

		self.combobox_alliance = QComboBox()
		self.label_alliance = QLabel('阵营')
		self.alliance = ['a','b','c','n']
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
		self.setLayout(self.layout)

	def closeEvent(self, event):
		self.defult['id'] = self.combobox_id.currentText()
		self.defult['name'] = self.combobox_name.currentText()
		self.defult['commander'] = self.combobox_commander.currentText()
		self.defult['ai'] = self.combobox_ai.currentText()
		self.defult['alliance'] = self.combobox_alliance.currentText()
		self.defult['techlevel'] = self.combobox_techlevel.currentText()
		self.defult['taxfactor'] = self.combobox_taxfactor.currentText()
		# self.defult['name'] = self.combobox_color.currentText()
		print(self.defult)
		print(self.filename)
		print(self.number_id)
		save(self.defult,self.filename,self.number_id)





class battle_or_conquest(QWidget):
	def __init__(self,parent=None,maptype='conquest',mapnum=1):
		super().__init__(parent)

		# self.window.setFixedSize(400, 300)

		self.btn_dialog01 = QPushButton('第1个战斗方')
		self.btn_dialog01.clicked.connect(self.openMessageBox01)
		self.btn_dialog02 = QPushButton('第2个战斗方')
		self.btn_dialog02.clicked.connect(self.openMessageBox02)
		self.btn_dialog03 = QPushButton('第3个战斗方')
		self.btn_dialog03.clicked.connect(self.openMessageBox03)
		self.btn_dialog04 = QPushButton('第4个战斗方')
		self.btn_dialog04.clicked.connect(self.openMessageBox04)
		self.btn_dialog05 = QPushButton('第5个战斗方')
		self.btn_dialog05.clicked.connect(self.openMessageBox05)
		self.btn_dialog06 = QPushButton('第6个战斗方')
		self.btn_dialog06.clicked.connect(self.openMessageBox06)
		self.btn_dialog07 = QPushButton('第7个战斗方')
		self.btn_dialog07.clicked.connect(self.openMessageBox07)
		self.btn_dialog08 = QPushButton('第8个战斗方')
		self.btn_dialog08.clicked.connect(self.openMessageBox08)
		self.btn_dialog09 = QPushButton('第9个战斗方')
		self.btn_dialog09.clicked.connect(self.openMessageBox09)
		self.btn_dialog10 = QPushButton('第10个战斗方')
		self.btn_dialog10.clicked.connect(self.openMessageBox10)
		self.btn_dialog11 = QPushButton('第11个战斗方')
		self.btn_dialog11.clicked.connect(self.openMessageBox11)
		self.btn_dialog12 = QPushButton('第12个战斗方')
		self.btn_dialog12.clicked.connect(self.openMessageBox12)
		self.btn_dialog13 = QPushButton('第13个战斗方')
		self.btn_dialog13.clicked.connect(self.openMessageBox13)
		self.btn_dialog14 = QPushButton('第14个战斗方')
		self.btn_dialog14.clicked.connect(self.openMessageBox14)
		self.btn_dialog15 = QPushButton('第15个战斗方')
		self.btn_dialog15.clicked.connect(self.openMessageBox15)
		self.btn_dialog16 = QPushButton('第16个战斗方')
		self.btn_dialog16.clicked.connect(self.openMessageBox16)
		self.btn_dialog17 = QPushButton('第17个战斗方')
		self.btn_dialog17.clicked.connect(self.openMessageBox17)
		self.btn_dialog18 = QPushButton('第18个战斗方')
		self.btn_dialog18.clicked.connect(self.openMessageBox18)
		self.btn_dialog19 = QPushButton('第19个战斗方')
		self.btn_dialog19.clicked.connect(self.openMessageBox19)
		self.btn_dialog20 = QPushButton('第20个战斗方')
		self.btn_dialog20.clicked.connect(self.openMessageBox20)


		self.layout = QGridLayout()
		self.layout.addWidget(self.btn_dialog01, 1, 1)
		self.layout.addWidget(self.btn_dialog02, 1, 2)
		self.layout.addWidget(self.btn_dialog03, 1, 3)
		self.layout.addWidget(self.btn_dialog04, 1, 4)
		self.layout.addWidget(self.btn_dialog05, 1, 5)
		self.layout.addWidget(self.btn_dialog06, 2, 1)
		self.layout.addWidget(self.btn_dialog07, 2, 2)
		self.layout.addWidget(self.btn_dialog08, 2, 3)
		self.layout.addWidget(self.btn_dialog09, 2, 4)
		self.layout.addWidget(self.btn_dialog10, 2, 5)
		self.layout.addWidget(self.btn_dialog11, 3, 1)
		self.layout.addWidget(self.btn_dialog12, 3, 2)
		self.layout.addWidget(self.btn_dialog13, 3, 3)
		self.layout.addWidget(self.btn_dialog14, 3, 4)
		self.layout.addWidget(self.btn_dialog15, 3, 5)
		self.layout.addWidget(self.btn_dialog16, 4, 1)
		self.layout.addWidget(self.btn_dialog17, 4, 2)
		self.layout.addWidget(self.btn_dialog18, 4, 3)
		self.layout.addWidget(self.btn_dialog19, 4, 4)
		self.layout.addWidget(self.btn_dialog20, 4, 5)

		self.setLayout(self.layout)
		self.country_01 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=0)
		self.country_02 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=1)
		self.country_03 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=2)
		self.country_04 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=3)
		self.country_05 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=4)
		self.country_06 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=5)
		self.country_07 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=6)
		self.country_08 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=7)
		self.country_09 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=8)
		self.country_10 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=9)
		self.country_11 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=10)
		self.country_12 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=11)
		self.country_13 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=12)
		self.country_14 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=13)
		self.country_15 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=14)
		self.country_16 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=15)
		self.country_17 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=16)
		self.country_18 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=17)
		self.country_19 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=18)
		self.country_20 = country_model(MapType=maptype, MapNum=mapnum, Number_Id=19)

	@Slot()
	def openMessageBox01(self):
		print(type(self.country_01))
		self.country_01.show()
		print(self.country_01.combobox_id.currentText())

	@Slot()
	def openMessageBox02(self):
		print(type(self.country_02))
		self.country_02.show()
		print(self.country_02.combobox_id.currentText())

	@Slot()
	def openMessageBox03(self):
		print(type(self.country_03))
		self.country_03.show()
		print(self.country_03.combobox_id.currentText())

	@Slot()
	def openMessageBox04(self):
		print(type(self.country_04))
		self.country_04.show()
		print(self.country_04.combobox_id.currentText())

	@Slot()
	def openMessageBox05(self):
		print(type(self.country_05))
		self.country_05.show()
		print(self.country_05.combobox_id.currentText())

	@Slot()
	def openMessageBox06(self):
		print(type(self.country_06))
		self.country_06.show()
		print(self.country_06.combobox_id.currentText())

	@Slot()
	def openMessageBox07(self):
		print(type(self.country_07))
		self.country_07.show()
		print(self.country_07.combobox_id.currentText())

	@Slot()
	def openMessageBox08(self):
		print(type(self.country_08))
		self.country_08.show()
		print(self.country_08.combobox_id.currentText())

	@Slot()
	def openMessageBox09(self):
		print(type(self.country_09))
		self.country_09.show()
		print(self.country_09.combobox_id.currentText())

	@Slot()
	def openMessageBox10(self):
		print(type(self.country_10))
		self.country_10.show()
		print(self.country_10.combobox_id.currentText())

	@Slot()
	def openMessageBox11(self):
		print(type(self.country_11))
		self.country_11.show()
		print(self.country_11.combobox_id.currentText())

	@Slot()
	def openMessageBox12(self):
		print(type(self.country_12))
		self.country_12.show()
		print(self.country_12.combobox_id.currentText())

	@Slot()
	def openMessageBox13(self):
		print(type(self.country_13))
		self.country_13.show()
		print(self.country_13.combobox_id.currentText())

	@Slot()
	def openMessageBox14(self):
		print(type(self.country_14))
		self.country_14.show()
		print(self.country_14.combobox_id.currentText())

	@Slot()
	def openMessageBox15(self):
		print(type(self.country_15))
		self.country_15.show()
		print(self.country_15.combobox_id.currentText())

	@Slot()
	def openMessageBox16(self):
		print(type(self.country_16))
		self.country_16.show()
		print(self.country_16.combobox_id.currentText())

	@Slot()
	def openMessageBox17(self):
		print(type(self.country_17))
		self.country_17.show()
		print(self.country_17.combobox_id.currentText())

	@Slot()
	def openMessageBox18(self):
		print(type(self.country_18))
		self.country_18.show()
		print(self.country_18.combobox_id.currentText())

	@Slot()
	def openMessageBox19(self):
		print(type(self.country_19))
		self.country_19.show()
		print(self.country_19.combobox_id.currentText())

	@Slot()
	def openMessageBox20(self):
		print(type(self.country_20))
		self.country_20.show()
		print(self.country_20.combobox_id.currentText())


app = QApplication()
widget = battle_or_conquest(maptype='conquest',mapnum=6)
widget.show()
app.exec_()

# print(widget.dic)
