
import os
#输入要更改文件的上级目录，我的话就是images和labels这两个文件夹下的train文件夹和val文件夹，以下以images/train文件夹为例。
path = r"C:\Users\zhyx_\Desktop\yolov5-master\SAR\datasets\labels\train"
#需要被替换的字符images
originalname = 'train'
#替换的字符串fire
replacename = ''
def main1(path1):
    files = os.listdir(path1)  # 得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
        if os.path.isdir(path1 + '\\' + file):
            main1(path1 + '\\' + file)
        else:
            files2 = os.listdir(path1 + '\\')
            for file1 in files2:
                if originalname in file1:
                    #用‘’替换掉 X变量
                    n = str(path1 + '\\' + file1.replace(originalname,replacename))
                    n1 = str(path1 + '\\' + str(file1))
                    try:
                        os.rename(n1, n)
                    except IOError:
                        continue
main1(path)


print('修改完成')
