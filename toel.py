# -*- cording:utf-8 -*-
import os
import time
import shutil
import chardet

copyFileCounts = 0


def whatcode(filepath):
    with open(filepath, "rb") as f:
        data = f.readline()
        codeType = chardet.detect(data)['encoding']
        print(codeType)


def whatype(value):        # 判断输入类型
    if not str:
        print("Type is Null")
        return "Null"
    else:
        if isinstance(value, int):
            print("Type is int")
            return "int"
        if isinstance(value, list):
            print("Type is list")
            return "list"
        if isinstance(value, tuple):
            print("Type is tuple")
            return "tuple"
        if isinstance(value, dict):
            print("Type is dict")
            return "dict"
        if isinstance(value, str):
            if value.strip() == "":
                print("Type is Null")
                return "Null"
            else:
                print("Type is str")
                return "str"


class AutoBackup(object):

    def __init__(self, path, target):
        self.sourceDir = path
        self.targetDir = target
        self.copyFile()

    def copyFile(self):
        global copyFileCounts
        for f in os.listdir(self.sourceDir):
            sourceF = os.path.join(self.sourceDir, f)   # 创建绝对地址
            targetF = os.path.join(self.targetDir, f)
            if os.path.isfile(sourceF):
                if not os.path.exists(self.targetDir):  # 创建目标文件夹
                    os.makedirs(self.targetDir)
                if os.path.exists(targetF) and (os.path.getmtime(targetF) >= os.path.getmtime(sourceF)):
                    # print("%s %s 已为最新" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF))
                    pass
                else:
                    # open(targetF, "wb").write(open(sourceF, "rb").read())   # 写入2进制文件
                    shutil.copy(sourceF, targetF)
                    print("%s %s 已备份 *" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), sourceF))
                    copyFileCounts += 1
            elif os.path.isdir(sourceF):
                AutoBackup(sourceF, targetF)
        # print("%s 当前处理文件夹%s已备份%s个文件到%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.sourceDir, copyFileCounts, self.targetDir))


def list_folders_files(path):
    """
    返回path中包含的 "文件夹" 和 "文件" 的绝对路径
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
            list_folders.append(file_path)
        else:
            list_files.append(file_path)
    return (list_folders, list_files)


def alter(file,old_str,new_str):
    """
      替换文件中的字符串
      :param file:文件名
      :param old_str:就字符串
      :param new_str:新字符串
      :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
         f.write(file_data)


if __name__ == "__main__":
    print("Select the function number: 1 for test; 2 for AutoBackup; ")
    fuc = input()
    if fuc == "1":      # test测试
        print(__name__)
        a = dict()
        print("a is", whatype(a))
        whatcode(r'C:\Users\Leon\Desktop\Research\SogouQ\SogouQutf8\access_log.20060804.decode.filter')
    elif fuc == "2":    # AutoBackup自动备份
        # AutoBackup("H:\Learn\Project\py_project\Toel", "H:\Learn\Project\py_project\Toel_backup")
        try:
            AutoBackup("H:\BigDate\Project", "G:\Projects")
            # AutoBackup("G:\Projects\HiveDemo", "H:\BigDate\Project\HiveDemo")
        except Exception as err:
            try:
                AutoBackup("I:\Learn\Project", "D:\Projects")
            except Exception as err:
                print("Nothing is new.")
                pass
    elif fuc == "3":     # 替换所有文件字符
        path = r'C:\Users\Leon\Desktop\Research\SogouQ\Sg_log'
        (list_folders, list_files) = list_folders_files(path)
        for file in list_files:
            alter(file, ' ', '\t')
            print(file.split('\\')[-1] + "\tis altered.")
    elif fuc == "4":     #  替换单个文件字符
        file = r'G:\Research\SogouQ\\associated.txt'
        alter(file, '\n', '')
        print(file.split('\\')[-1] + "\tis altered.")
