#1.利用os模块编写一个能实现dir -l输出的程序。
#2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os
name=input("请输入需要查找的文件名：")
rootdir=str(input('请输入查找的根目录的路径：'))

def find_file(s,location):
    if not os.path.exists(location):
        print('not exist,input error')
        return
    if not os.path.isdir(location):
        print('not a dir_path')
        return
    num=0
    for paths,child_dirs,files in os.walk(location):
        for file in files:
            if (s in file):
                print(os.path.join(paths,file))
                print('\n')
                num=num+1
    return num

file_num=find_file(name,rootdir)
print('一共查找%s个文件。'%file_num)
