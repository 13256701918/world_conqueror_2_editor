
from global_thing import mainwindow,remove_widget_list

def remove_widget(current_type=None):
	if remove_widget_list is not []:
		# print(remove_widget_list)
		for widget,type in remove_widget_list:
			if current_type == type:
				remove_widget_list.remove((widget,type))
				if widget.delete_widget is not None:
					widget.delete_widget.close()
				if widget.delete_mainwidget is not None:
					mainwindow.removeDockWidget(widget.delete_mainwidget)




