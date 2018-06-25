import os

def rename_files():
    path = os.getcwd()
    test_path = os.path.join(path,'test')
    #print(test_path)
    all_files = os.listdir(test_path)
    #print(all_files)
    for file in all_files:
        file_com = os.path.splitext(file)
        #print(file_com)
        filename = file_com[0]
        extension = file_com[1]
        new_file = filename + '_test' + extension
        #print(new_file)
        old_file_path = os.path.join(test_path,file)
        new_file_path = os.path.join(test_path,new_file)
        os.rename(old_file_path,new_file_path)

#删除病毒代码

raw_path = input('请输入要处理的文件路径：')
c_path = os.getcwd()
templates_path = raw_path
all_files = os.listdir(templates_path)
rule = '<script language="jscript">'
for file in all_files:
    path = os.path.join(templates_path,file)
    fp = open(path,'r',encoding='utf-8')
    #print(fp.tell())
    lines = fp.readlines()
    new_lines = []
    vb_start = False
    for line in lines:
        #代表指针已在有病毒的区域
        if rule in line:
            vb_start = True
        elif '</srcipt>' in line:
            vb_start = False
        else:
            if vb_start:
                continue
            else:
                new_lines.append(line)
    fp.close()

    #再重新写入文件覆盖原有的
    fp = open(path,'w')
    fp.writelines(new_lines)
    fp.close()

#1.假如病毒代码不在最后面
#2.路径由用户自己输入
#3.如果文件太大，如何处理
#4.如果这个文件夹下有子文件夹
#5.文件打开的方式,不是最优化
with open(path,'r') as fp:
    pass




