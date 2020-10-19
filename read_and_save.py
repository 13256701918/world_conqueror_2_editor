import xml.etree.ElementTree as et
import xml.dom.minidom as minidom
from all_dic import *

def read(name,number_id=1):
    filename=r"/Applications/World Conqueror 2.app/Contents/Resources/"+name
    print('this is reading')
    # print(number_id)
    # print(filename)
    tree = et.parse(filename)

    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    nodes_list = root.findall('list')
    country_list=nodes_list[0]
    area_list=nodes_list[1]
    dialog_list=nodes_list[2]
    # print(area_list)
    # print(country_list[number_id].attrib)
    if number_id >= len(country_list):

        return country_list[0].attrib
    else:
        print(country_list[number_id].attrib)
        return country_list[number_id].attrib

def read_contrylist(name='battle_allies1.xml'):
    filename=r"/Applications/World Conqueror 2.app/Contents/Resources/"+name
    print('this is reading')
    print(filename)

    tree = et.parse(filename)

    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    nodes_list = root.findall('list')
    country_list=nodes_list[0]
    area_list=nodes_list[1]
    dialog_list=nodes_list[2]
    # print(area_list)
    # print(country_list[number_id].attrib)
    # print(len(country_list))
    all_dic={}
    for i in range(0,len(country_list)):
        new_dic={}
        for k,v in country_list[i].attrib.items():
            if k == 'a' or k=='b' or k=='g' or k=='r':
                new_dic[k]=v
            if k == 'id':
                # print(v)
                # print(type(v))
                temp=id_reverser_dic[v]
        all_dic[temp]=new_dic
    # print(all_dic)


    return country_list

def read_orignal_contrylist(name='battle_axis10.xml'):

    filename = r"/Users/vajorstack/PycharmProjects/qt_wc/battle/" + name
    print('this is reading')
    print(filename)

    tree = et.parse(filename)

    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    nodes_list = root.findall('list')
    country_list=nodes_list[0]
    area_list=nodes_list[1]
    dialog_list=nodes_list[2]
    # print(area_list)
    # print(country_list[number_id].attrib)
    print(len(country_list))
    all_dic={}
    for i in range(0,len(country_list)):
        new_dic={}
        for k,v in country_list[i].attrib.items():
            if k == 'a' or k=='b' or k=='g' or k=='r':
                new_dic[k]=v
            if k == 'id':
                # print(v)
                # print(type(v))
                temp=id_reverser_dic[v]
        all_dic[temp]=new_dic
    print(all_dic)


    return country_list



def save(dict_get,name,nameid):
    filename=r"/Applications/World Conqueror 2.app/Contents/Resources/"+name
    print('this is saving')
    print(filename)
    tree = et.parse(filename)
    print(dict_get)
    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    nodes_list = root.findall('list')
    country_list=nodes_list[0]
    if nameid < len(country_list):
        country_list[nameid].attrib=dict_get

    tree = et.ElementTree(root)
    rough_str = et.tostring(root, 'utf-8')
    # 格式化
    reparsed = minidom.parseString(rough_str)
    new_str = reparsed.toprettyxml(indent='\t')
    tree.write(filename, )






def test():
    tree = et.parse("/Applications/World Conqueror 2.app/Contents/Resources/conquest_6.xml")

    root = tree.getroot()
    # print(root.tag)
    # print(root.attrib)
    nodes_list = root.findall('list')
    country_list=nodes_list[0]
    area_list=nodes_list[1]
    dialog_list=nodes_list[2]
    # print(area_list)
    for one in country_list:
        # print(one.tag)
        # print(one.attrib)
        # print(type(one.attrib))
        count=0
        dict={}
        # print(one.attrib)
        one.attrib
        for a,b in one.attrib.items():
            # dict[a]=b
            # print("'"+a+"'",end=',')
            #
            if a =='name':
               print("'"+b+"'",end=',')

            count+=1
        # print('\n')
        # return dict
        # break
    print(dict)
        # print()
        # print(one.get('ai'))
        # ai=0
        # one.set('ai',str(0))
        # one.set('ai',"%d"%int(0))
        # print(one.attrib)
    # print(area_list)
    # print(dialog_list)
    # for nodes in nodes_list:
    #     print(nodes)
    #     print(nodes.tag)
    #     print(nodes.attrib)
    #     for one in nodes:
    #         print(one.tag)
    #         print(one.attrib)
    #         print(one.get('ai'))
    #         ai=0
    #         one.set('ai',str(0))
    #         # one.set('ai',"%d"%int(0))
    #         print(one.attrib)
    #     break


    country_list[1].attrib['id']='de3'
    # print(country_list[1].attrib)


    tree = et.ElementTree(root)
    rough_str = et.tostring(root, 'utf-8')
    # 格式化
    reparsed = minidom.parseString(rough_str)
    new_str = reparsed.toprettyxml(indent='\t')
    tree.write('./s.xml',)

if __name__=='__main__':
    print(id_reverser_dic)
    read_orignal_contrylist()


