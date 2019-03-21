# 声明一个 int_demo方法
# modle 模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系通过缩进来表示
# class 类 类型
# 合法标识符（变量名方法名）：必须以字母或者_开头 剩下的可以是字母数字 下划线 大小写敏感 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+k commit 代码
# ctrl+shift+k push代码
def int_demo():
    # 声明aint变量，并赋值1
    aint = 1
    print(aint)
    # 打印aint的类型 type（aint） 获取aint的类型
    print(type(aint))


# 声明一个add方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回aint+bint
    return aint + bint


# 声明一个sub方法 参数有两个 aint,bint
def sub(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回aint+bint
    return aint - bint

# 声明一个 float_demo方法
def float_demo():
    # 声明afloat变量，并赋值1
    afloat = 1.8
    print(afloat)
    # 打印afloat的类型 type（afloat） 获取afloat的  类型
    print(type(afloat))

if __name__ == '__main__':
    # 提取变量 ctrl+alt+v
    # 调用sub方法 传入1,2得到返回值 赋值给result变量
    float_demo()
    #result = sub(5, 3)
    #print(result)

# 演示字符串拼接 : +
def str_demo1():
    a= 'hello'
    b= ' world'
    return a+b

# 字符串拼接: %s
def str_demo2():
    a= 'hello '
    b= 250
    # print(a+ str(b))
    print('a 是 : %s;b 是 : %s'%(a,b))

# 去掉两头空格
def str_demo3():
    astr = ' ysl '
    # astr 是变量 也叫 对象  ,对象 . 可以调用对象的方法
    print(astr)
    print(astr.strip())