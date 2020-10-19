from other_rs import *
from all_dic import *
from PySide2.QtWidgets import QTableView,QWidget,QApplication,QLabel,QDialog,QPushButton, QMessageBox
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
class info_window(QDialog):
	def __init__(self,info,info_type='test'):
		super().__init__()
		# self.setMinimumSize(280,600)
		if info_type == 'test':
			self.label = QLabel(info, self)
			self.setWindowTitle('子窗口')
		if info_type == 'armydef':
			self.setWindowTitle('国家属性')
			# self.resize(500, 300)
			# 设置数据层次结构，4行4列
			self.model = QStandardItemModel(len(info), 4)
			# 设置水平方向四个头标签文本内容


			armydef_list_1=[]
			armydef_list_2=[]
			# print(type(info))
			for k,v in info.items():
				armydef_list_1.append(k)
				armydef_list_2.append(v)

			self.model.setVerticalHeaderLabels(armydef_dic[i] for i in armydef_list_1)
			self.model.setHorizontalHeaderLabels(['生命值','移动能力','最小攻击力','最大攻击力'])

			for row in range(len(info)):
				for column in range(4):
						item = QStandardItem(info[armydef_list_1[row]][column])
						self.model.setItem(row, column, item)
			# 实例化表格视图，设置模型为自定义的模型
			self.tableView = QTableView(self)
			self.tableView.resize(400,600)
			self.tableView.setModel(self.model)
			# #todo 优化1 表格填满窗口
			# #水平方向标签拓展剩下的窗口部分，填满表格
			# 水平方向标签拓展剩下的窗口部分，填满表格
			self.tableView.horizontalHeader().setStretchLastSection(True)
			# 水平方向，表格大小拓展到适当的尺寸
			self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
			#
			# #TODO 优化3 删除当前选中的数据
			# indexs=self.tableView.selectionModel().selection().indexes()
			# print(indexs)
			# if len(indexs)>0:
			#     index=indexs[0]
			#     self.model.removeRows(index.row(),1)

class info_button(QPushButton):
	def __init__(self, parent=None,info='test',info_type='test'):
		super().__init__(parent)
		# self.setFixedSize(300, 200)
		self.setBaseSize(10,10)
		self.setText('?')
		self.info = info_window(info,info_type)

	def info_change(self,info,info_type):
		print(info)
		self.info=info_window(info,info_type)

	def mousePressEvent(self, event):
		self.info.show()
		self.info.exec_()

	def mouseReleaseEvent(self, event):
		self.info.close()

if __name__=="__main__":
	app = QApplication()
	window = QWidget()
	test = info_button(window,info='sssss')
	window.show()
	app.exec_()