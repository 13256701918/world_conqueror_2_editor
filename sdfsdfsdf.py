a=r"‘隆美尔’、‘戈林’、‘古德里安’、‘麦克阿瑟’、‘巴顿’、‘尼米兹’、‘朱可夫’、‘罗科索夫斯基’、‘蒙哥马利’、‘戴高乐’、‘山本’、‘格拉齐亚尼’、‘张’、‘彭’、‘common1’、‘common2’、‘common3’"
b=a.replace('‘','')
c=b.replace('’','')
d=c.replace('、',',')
t=list(d.split(','))
print(t)

e=['Rommel', 'Goering', 'Guderian', 'MacArthur', 'Patton', 'Nimitz', 'Zhukov', 'Rokossovsky', 'Montgomery', 'de Gaulle', 'Yamamoto', 'Graziani', 'Zhang', 'Peng', 'common1', 'common2', 'common3']

new_dic={}
print(type(t))
print(len(t))
for i in range(0,len(t)):
    new_dic[t[i]]=e[i]

print(new_dic)



