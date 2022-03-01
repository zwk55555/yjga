from os import listdir

try:
    #获取json文件存放目录
    path = input("请输入json文件存放的路劲：")
    dirs = listdir(path + '/JsonFile/')  # 获取当前目录列表
    #用于存放提取的数据
    data = []
    for i in range(len(dirs)):
        with open(path + '/JsonFile/' + dirs[i], 'r') as f:
            print(dirs[i]+"   "+"正则处理中。。。。")
            #print("--------------------------------------")
            #读取json文件中的所有行并保存
            for line in f:
                data.append(line)
    #写入txt文档
    with open(path + '/Result/result.txt', 'w', encoding='utf-8') as f:  # 以写入为目的打开文件
        for i in range(len(data)):
            s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同
            s = s.replace('"', '') + '\n'  # 去除引号，每行末尾追加换行符
            f.write(s)
except:
    print("错误，请重试")
