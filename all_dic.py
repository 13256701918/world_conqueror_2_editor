id_dic={'英国':'gb','英国2':'gb2','英国1':'gb1','美国':'am','美国3':'am3','美国2':'am2','美国1':'am1','法国':'fr','加拿大':'ca','德国':'de','德国1':'de1','德国2':'de2','德国3':'de3',
		'意大利':'it','意大利1':'it1','意大利2':'it2','俄罗斯':'ru','俄罗斯1':'ru1','俄罗斯2':'ru2','俄罗斯3':'ru3','罗马尼亚':'ro','保加利亚':'bg','墨西哥':'mx','南斯拉夫':'yu','比利时':'be',
		'波兰':'pl','瑞士':'ch','丹麦':'dk','挪威':'no','希腊':'gr','匈牙利':'hu','芬兰':'fl','土耳其':'tr','西班牙':'es','葡萄牙':'pt','瑞典':'se','中国':'cn',
		'台湾':'tw','朝鲜':'nk','韩国':'rk','印度':'in','日本':'ja','澳大利亚':'au','加拿大':'ca','荷兰':'nl'}
id_reverser_dic={value:key for key,value in id_dic.items()}
country_dic={'英国':'gb','美国':'am','法国':'fr','加拿大':'ca','德国':'de','意大利':'it','俄罗斯':'ru','罗马尼亚':'ro','保加利亚':'bg','墨西哥':'mx','南斯拉夫':'yu','比利时':'be',
			 '波兰':'pl','瑞士':'ch','丹麦':'dk','挪威':'no','希腊':'gr','匈牙利':'hu','芬兰':'fl','土耳其':'tr','西班牙':'es','葡萄牙':'pt','瑞典':'se','中国':'cn','台湾':'tw',
			 '朝鲜':'nk','韩国':'rk','印度':'in','日本':'ja','澳大利亚':'au','加拿大':'ca','荷兰':'nl'}
country_reverse_dic={value:key for key,value in country_dic.items()}
battle_dic={'轴心国战役':'battle_axis','盟军战役':'battle_allies','北约战役':'battle_nato','华约战役':'battle_wto','征服':'conquest'}
battle_reverse_dic={value:key for key,value in battle_dic.items()}
commander_dic={'杂鱼1号':'common1', '隆美尔':'Rommel', '古德里安':'Guderian', '罗科索夫斯基':'Rokossovsky', '杂鱼2号':'common2','巴顿':'Patton','朱可夫':'Zhukov',
			   '尼米兹':'Nimitz','蒙哥马利':'Montgomery','戴高乐':'de Gaulle','格拉齐亚尼':'Graziani','彭德怀':'Peng'}
commander_reserve_dic={value:key for key,value in commander_dic.items()}

control_dic={'玩家':'0','电脑':'1'}
control_reverse_dic={value:key for key,value in control_dic.items()}

defeated_dic={'陆军':'land','全军':'army'}
defeated_reverse_dic={value:key for key,value in defeated_dic.items()}

color_dic={'俄罗斯1': {'r': '255', 'g': '0', 'b': '0', 'a': '90'}, '德国1': {'r': '0', 'g': '0', 'b': '0', 'a': '90'}, '德国2': {'r': '71', 'g': '87', 'b': '99', 'a': '90'},
		   '俄罗斯2': {'r': '204', 'g': '0', 'b': '32', 'a': '90'}, '俄罗斯3': {'r': '227', 'g': '32', 'b': '0', 'a': '90'}, '芬兰': {'r': '146', 'g': '205', 'b': '220', 'a': '90'},
		   '罗马尼亚': {'r': '149', 'g': '55', 'b': '53', 'a': '90'},'美国1': {'r': '64', 'g': '199', 'b': '64', 'a': '90'}, '美国2': {'r': '64', 'g': '255', 'b': '64', 'a': '90'},
		   '美国3': {'r': '162', 'g': '255', 'b': '64', 'a': '90'},
			'俄罗斯': {'r': '255', 'g': '0', 'b': '0', 'a': '90'}, '美国': {'r': '162', 'g': '255', 'b': '64', 'a': '90'},
		   '英国': {'r': '255', 'g': '255', 'b': '0', 'a': '90'}, '法国': {'r': '0', 'g': '170', 'b': '170', 'a': '90'}, '意大利': {'r': '80', 'g': '20', 'b': '200', 'a': '90'},
		   '中国': {'r': '255', 'g': '90', 'b': '90', 'a': '90'}, '波兰': {'r': '255', 'g': '128', 'b': '64', 'a': '90'}, '土耳其': {'r': '0', 'g': '128', 'b': '192', 'a': '90'},
		   '西班牙': {'r': '255', 'g': '0', 'b': '128', 'a': '90'}, '印度': {'r': '0', 'g': '102', 'b': '0', 'a': '90'}, '澳大利亚': {'r': '0', 'g': '49', 'b': '146', 'a': '90'},
		   '加拿大': {'r': '16', 'g': '86', 'b': '116', 'a': '90'}, '南斯拉夫': {'r': '218', 'g': '150', 'b': '148', 'a': '90'}, '罗马尼亚': {'r': '149', 'g': '55', 'b': '53', 'a': '90'},
		   '希腊': {'r': '83', 'g': '141', 'b': '213', 'a': '90'}, '保加利亚': {'r': '0', 'g': '0', 'b': '128', 'a': '90'}, '匈牙利': {'r': '128', 'g': '64', 'b': '90', 'a': '90'},
		   '朝鲜': {'r': '255', 'g': '153', 'b': '153', 'a': '90'}}
def color_reverse_dic(dic):
	return list(color_dic.keys())[list(color_dic.values()).index(dic)]

armydef_dic={'infantry': '步兵', 'panzer': '装甲兵', 'artillery': '炮兵', 'rocket': '火箭', 'tank': '坦克', 'heavytank': '重型坦克', 'destroyer': '驱逐舰', 'cruiser': '巡洋舰', 'battleship': '战列舰', 'aircraftcarrier': '航空母舰', 'carrier': '航母', 'airstrike': '空袭', 'bomber': '轰炸机', 'airborne': '空降兵', 'nuclearbomb': '核弹头'}
armydef_reverse_dic={value:key for key,value in armydef_dic.items()}
