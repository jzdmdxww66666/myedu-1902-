#声明一个全量 dict 变量 （字典）

adict = {"name":"chenbaba","pwd":"123456"}

#这是一个字符串 不过他是json格式 也是字典的格式
adictStr = '{"name":"chenbaba","pwd":"123456"}'

if __name__ == '__main__':
    print(adict)
    #adict.pop('name')
    print(adict['name'])
    print(adict)