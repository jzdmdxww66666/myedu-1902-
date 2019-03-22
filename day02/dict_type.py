import json

#声明一个全量 dict 变量 （字典）

adict = {"name":"chenbaba","pwd":"123456",}

#这是一个字符串 不过他是json格式 也是字典的格式
adictStr = '{"name":"chenbaba","pwd":"123456","1":"数字1"}'

def china_demo():
    loads = json.loads(adictStr)
    print(type(loads))
    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)


if __name__ == '__main__':

    print(adict)
    #adict.pop('name')
    #print(adict['name'])
    #print(adict)
    #print(type(adict))
    #print(type(adictStr))
    #loads = json.loads(adictStr)
    #print(type(loads))
    loads = json.loads(adictStr)
    print(type(loads))
    dumps = json.dumps(loads, ensure_ascii=False)
    print(dumps)

