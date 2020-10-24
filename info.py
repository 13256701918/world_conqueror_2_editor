from other_rs import *
from all_dic import *
from PySide2.QtWidgets import QTableView,QWidget,QApplication,QLabel,QDialog,QPushButton, QMessageBox
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
class info_window(QDialog):
	def __init__(self,info,info_type='test'):
		super().__init__()
		self.second_attrib = None
		# self.setMinimumSize(280,600)
		if info_type == 'test':
			self.label = QLabel(info, self)
			self.setWindowTitle('子窗口')
		else:
			# print(info)
			# print(type(info))
			self.setWindowTitle(info_dic[info_type])
			for k, v in info.items():
				self.second_attrib = v
				break
			if type(self.second_attrib) == dict:
				self.model = QStandardItemModel(len(info), len(self.second_attrib))
				self.model.setHorizontalHeaderLabels(armydef_dic[key] for key in self.second_attrib.keys())
				self.model.setVerticalHeaderLabels(armydef_dic[key] for key in info.keys())
				for row,row_info in zip(range(len(info)),info.values()):
					for column,column_info in zip(range(len(self.second_attrib)),row_info.values()):
							item = QStandardItem(column_info)
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
			else:
				self.model = QStandardItemModel(len(info),1)
				self.model.setVerticalHeaderLabels(commanderdef_dic[key] for key in info.keys())
				# exit(0)
				for row,row_info in zip(range(len(info)),info.values()):
					item = QStandardItem(row_info)
					self.model.setItem(row,item)
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