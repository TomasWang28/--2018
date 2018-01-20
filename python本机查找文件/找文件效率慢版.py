import os

def search(filename, filepath):
    for d in os.listdir(filepath):
        path=os.path.join(filepath,d)
        if os.path.isdir(path):
            search(filename,path)
        if os.path.isfile(path):
            if d.find(filename)!=-1:
                print(path)

filename=input('请输入查询文件名：')
filepath=input('请输入查询目录：')
search(filename,filepath)
