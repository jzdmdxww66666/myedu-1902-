# 声明一个 int_demo方法
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
