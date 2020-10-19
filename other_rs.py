from defult import  dir
import xml.etree.ElementTree as et
import xml.dom.minidom as minidom


def get_armydef():
    armydef_file = dir+r'armydef.xml'
    tree = et.parse(armydef_file)

    root = tree.getroot()

    armydef_dic ={}
    armydef_list = root.findall('country')

    for armydef in armydef_list:
        # print(armydef.attrib)
        armydef_name = armydef.attrib['name']
        temp_dic= {}
        for _ in armydef:
            # print(_.attrib)
            temp_dic[_.attrib['type']]=[_.attrib['strength'],_.attrib['movement'],_.attrib['minatk'],_.attrib['maxatk']]
        armydef_dic[armydef_name] = temp_dic
    # print(armydef_dic)

    return armydef_dic
    # break


if __name__=='__main__':
    print(get_armydef()['others'])


