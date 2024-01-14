import os
import numpy as np
import json


def json2txt(path_json, path_txt):
    with open(path_json, 'r', encoding='gb18030') as path_json:
        jsonx = json.load(path_json)
        with open(path_txt, 'w+') as ftxt:
            for shape in jsonx['shapes']:
                xy = np.array(shape['points'])
                label = str(shape['label'])
                if label == 'QB' :
                    label = '0'
                elif label =='MAM':
                    label = '1'
                else:
                    label = '2'
                label += ' '
                strxy = ''
                for m, n in xy:
                    strxy += str(m) + ' ' + str(n) + ' '
                label += strxy
                ftxt.writelines(label + "\n")


dir_json = r"C:\Users\zhyx_\Desktop\MSTAR-10\test\debug"
dir_txt =  r"C:\Users\zhyx_\Desktop\MSTAR-10\test\txt"
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt, json_name in enumerate(list_json):
    print('cnt=%d,name=%s' % (cnt, json_name))
    path_json = dir_json + json_name
    path_txt = dir_txt + json_name.replace('.json', '.txt')
    print(path_json, path_txt)
    json2txt(path_json, path_txt)

