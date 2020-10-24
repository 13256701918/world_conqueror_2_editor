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
        new_dic = {}
        for _ in armydef:
            # print(_.attrib)
            # print(_.attrib)
            new_dic[_.attrib['type']]={keys:_.attrib[keys] for keys in _.keys() if keys !='type'}
            # for __ in _:
                # print(__,'ssssss')
            temp_dic[_.attrib['type']]=[_.attrib['strength'],_.attrib['movement'],_.attrib['minatk'],_.attrib['maxatk']]
        # print(new_dic)
        armydef_dic[armydef_name] = new_dic
    # print(armydef_dic)

    return armydef_dic
    # break

def get_commanderdef():
    commanderdef_file = dir+r'commanderdef.xml'
    tree = et.parse(commanderdef_file)

    root = tree.getroot()

    commanderdef_list = root.findall('commander')
    # print(commanderdef_list)
    commanderdef_dic ={}
    for commanderdef in commanderdef_list:
        # print(commanderdef.keys())
        commanderdef_dic[commanderdef.attrib['name']]={keys:commanderdef.attrib[keys] for keys in commanderdef.keys() if keys != 'name'}


    return commanderdef_dic

if __name__=='__main__':
    print(get_armydef())

    # print(get_armydef())

