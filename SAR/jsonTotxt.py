import json
import os

name2id = {'2S1': 0, 'BMP2': 1, 'BRDM_2': 2,'BTR60': 3,'BTR70': 4,'D7': 5,'T62': 6,'T72': 7,'ZIL131': 8,'ZSU_23_4': 9}  # 标签名称


def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def decode_json(json_floder_path, json_name):
    txt_name ='C:\\Users\\zhyx_\\Desktop\\yolov5-master\\SAR\\datasets\\labels\\test\\' + json_name[0:-5] + '.txt'
    # 存放txt的绝对路径
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='gb2312', errors='ignore'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:

        label_name = i['label']
        if (i['shape_type'] == 'rectangle'):
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')


if __name__ == "__main__":

    json_floder_path = 'C:\\Users\\zhyx_\\Desktop\\yolov5-master\\SAR\\debug'
    # 存放json的文件夹的绝对路径
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path, json_name)