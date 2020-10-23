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
from remove_widget_file import remove_widget

armydef_dic=get_armydef()
print(commander_reserve_dic)
class country_model(QWidget):
	def __init__(self,parent=None,file_name='battle_axis1.xml',Number_Id=0):
		super().__init__(parent)
		self.setMinimumSize(500,300)
		self.number_id=Number_Id
		# print(self.filename)
		self.file_name=file_name
		self.defult = read(self.file_name,self.number_id)

		self.combobox_id = QComboBox()
		self.label_id = QLabel('国家')
		self.id = list(id_dic.keys())
		self.combobox_id.addItems(self.id)
		self.combobox_id.setCurrentText(id_reverser_dic[self.defult['id']])
		# self.combobox_id.setCurrentText('ru2')
		self.layout_id=QHBoxLayout()
		self.layout_id.addWidget(self.label_id)
		self.layout_id.addWidget(self.combobox_id)

		# print(self.combobox_id.currentText())

		self.combobox_name = QComboBox()
		self.label_name = QLabel('军队')
		self.name = list(country_dic.keys())
		self.combobox_name.addItems(self.name)
		self.combobox_name.setCurrentText(country_reverse_dic[self.defult['name']])
		self.layout_name=QHBoxLayout()
		self.info_name = info_button(self,info=armydef_dic[country_dic[self.combobox_name.currentText()]],info_type='armydef')
		self.combobox_name.currentIndexChanged.connect(self.battle_country_name)

		self.layout_name.addWidget(self.label_name)
		self.layout_name.addWidget(self.combobox_name)
		self.layout_name.addWidget(self.info_name)
		self.layout_name.setStretch(0,2)
		self.layout_name.setStretch(1,2)

		# print(self.combobox_id.currentText())

		self.combobox_commander = QComboBox()
		self.label_commander = QLabel('指挥官')
		self.commander = list(commander_dic.keys())
		self.combobox_commander.addItems(self.commander)
		self.combobox_commander.setCurrentText(commander_reserve_dic[self.defult['commander']])
		self.layout_commander=QHBoxLayout()
		self.layout_commander.addWidget(self.label_commander)
		self.layout_commander.addWidget(self.combobox_commander)

		self.combobox_ai = QComboBox()
		self.label_ai = QLabel('电脑或玩家控制')
		self.ai = list(control_dic.keys())
		self.combobox_ai.addItems(self.ai)
		self.combobox_ai.setCurrentText(control_reverse_dic[self.defult['ai']])
		self.layout_ai=QHBoxLayout()
		self.layout_ai.addWidget(self.label_ai)
		self.layout_ai.addWidget(self.combobox_ai)

		self.combobox_defeated = QComboBox()
		self.label_defeated = QLabel('获胜条件')
		self.defeated = list(defeated_dic.keys())
		self.combobox_defeated.addItems(self.defeated)
		self.combobox_defeated.setCurrentText(defeated_reverse_dic[self.defult['defeated']])
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
		self.color = list(color_dic.keys())
		self.combobox_color.addItems(self.color)
		self.defult_color={}
		for _ in ('a','b','g','r'):
			self.defult_color[_]=self.defult[_]
		self.combobox_color.setCurrentText(color_reverse_dic(self.defult_color))
		print(self.defult_color)
		print(color_reverse_dic(self.defult_color))
		self.color_map = {'r':int(color_dic[self.combobox_color.currentText()]['r']),
								'g':int(color_dic[self.combobox_color.currentText()]['g']),
								'b':int(color_dic[self.combobox_color.currentText()]['b']),
								'a':int(color_dic[self.combobox_color.currentText()]['a'])}

		self.label_map = QLabel()
		self.label_map.setMaximumSize(30,30)
		# self.label_map.setBackgroundRole(self.color_map)
		self.label_map.setStyleSheet("background-color: rgba(%s,%s,%s,%s)"%(self.color_map['r'],self.color_map['g'],self.color_map['b'],self.color_map['a']))
		self.layout_color=QHBoxLayout()
		self.layout_color.addWidget(self.label_color)
		self.layout_color.addWidget(self.combobox_color)
		self.layout_color.addWidget(self.label_map)
		self.combobox_color.currentIndexChanged.connect(self.change_color)

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

	def battle_country_name(self):
		if country_dic[self.combobox_name.currentText()] in armydef_dic.keys():
			self.temp_info = armydef_dic[country_dic[self.combobox_name.currentText()]]
		else:
			self.temp_info = armydef_dic['others']

		self.info_name.info_change(info=self.temp_info,info_type='armydef')


	def change_color(self):
		self.color_map = {'r':int(color_dic[self.combobox_color.currentText()]['r']),
								'g':int(color_dic[self.combobox_color.currentText()]['g']),
								'b':int(color_dic[self.combobox_color.currentText()]['b']),
								'a':int(color_dic[self.combobox_color.currentText()]['a'])}

		self.label_map.setStyleSheet("background-color: rgb(%s,%s,%s)"%(self.color_map['r'],self.color_map['g'],self.color_map['b']))


	def closeEvent(self, event):

		self.defult['id'] = id_dic[self.combobox_id.currentText()]
		self.defult['name'] = country_dic[self.combobox_name.currentText()]
		self.defult['commander'] = commander_dic[self.combobox_commander.currentText()]
		self.defult['ai'] = control_dic[self.combobox_ai.currentText()]
		self.defult['alliance'] = self.combobox_alliance.currentText()
		self.defult['defeated']=defeated_dic[self.combobox_defeated.currentText()]
		self.defult['techlevel'] = self.combobox_techlevel.currentText()
		self.defult['taxfactor'] = self.combobox_taxfactor.currentText()
		self.defult['a'] = color_dic[self.combobox_color.currentText()]['a']
		self.defult['b'] = color_dic[self.combobox_color.currentText()]['b']
		self.defult['g'] = color_dic[self.combobox_color.currentText()]['g']
		self.defult['r'] = color_dic[self.combobox_color.currentText()]['r']
		# self.defult['name'] = self.combobox_color.currentText()
		print(self.defult)
		# print(self.filename)
		# print(self.number_id)
		save(self.defult,self.file_name,self.number_id)