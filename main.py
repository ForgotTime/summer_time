import settings
import json
import xml.etree.cElementTree as et
def get_dict_by_txt():
    d = {}
    file = open("main.txt")
    content = file.readlines()
    for i in content:
        key = i.strip().split("=",1)[0]
        value = i.strip().split("=",1)[1]
        d[key] = value
    return d

def get_dict_by_py():
    d = {}
    l = dir(settings)
    for i in l:
        key = i
        value = getattr(settings,key,0)
        d[key] = value
    return d
def get_dict_by_json():
    fr = open("main.json")
    d = json.load(fr)
    fr.close()
    return d

def get_root_by_xml():
    tree = et.parse("main.xml")
    root = tree.getroot()
    return root

d = get_dict_by_json()
mail_title = d["mail_title"]
mail_content = d["mail_content"]
print(
f'''
邮件标题：{mail_title}
邮件内容：{mail_content}
''')
root = get_root_by_xml()
country = root.find("country")
name = country.find("name").text
rank = country.find("rank").text
year = country.find("gdppc").text
neighbor = country.find("neighbor")
neighbor_name = neighbor.find("name").text
neighbor_direction = neighbor.find("direction").text
print(f'''
国家名称：{name}
国家排名：{rank}
国家gdp：{year}
邻国名称：{neighbor_name}
邻国方向：{neighbor_direction}
''')
