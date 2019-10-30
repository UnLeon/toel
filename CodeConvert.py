# -*- coding: UTF-8 -*-
# https://blog.csdn.net/humanking7/article/details/78501474
import codecs
import os
import sys
import chardet


def convert(file, in_enc, out_enc="utf-8"):
    # 从指定格式转换到指定格式
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()
    if in_enc == 'GB2312':
        in_enc = 'GB18030'
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc)
        if in_enc != out_enc:
            file_con = codecs.open(file, 'r', encoding=in_enc).read()
            codecs.open(file, 'w', out_enc).write(file_con)
        else:
            pass
    # print (f.read())  量大谨慎
    except Exception as err:
        print("\t" + file.split('\\')[-1] + " : convert failed !")
        print("\t" + str(err))
        # print(str(err))


def list_folders_files(path):
    """
    返回 "文件夹" 和 "文件" 名字
    :param path: "文件夹"和"文件"所在的路径
    :return:  (list_folders, list_files)
            :list_folders: 文件夹
            :list_files: 文件
    """
    list_folders = []
    list_files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_folders.append(file)
        else:
            list_files.append(file)
    return (list_folders, list_files)


if __name__ == "__main__":

    path = r'C:\Users\Leon\Desktop\Research\SogouQ\SogouQutf8'
    (list_folders, list_files) = list_folders_files(path)

    print("Path: " + path)
    for fileName in list_files:
        filePath = path + '\\' + fileName
        #convert(filePath)
        with open(filePath, "rb") as f:
            data = f.readline()
            for i in range(30):
                data += f.readline()
            codeType = chardet.detect(data)['encoding']
            convert(filePath, codeType, 'utf-8')
