# 如何调用别人的代码
#  第一步: 导入: import   如果是大模块导入 ,需要加 from 大模块的名字 import 小模块的名字
from day01 import base_type

if __name__ == '__main__':
    # 如何使用 小模块的方法
    # 小模块的名字.方法名() : 若有参数,入参,写括号内,可指定参数入参,可默认参数入参;没有参数不管
    # = 后面是 调用方法
    # = 前面是 给方法的返回值起个名字 ,存起来
    result = base_type.add(aint=10, bint=5)
    print(result)
    # base_type.intqq 不带括号 ,说明调用了一个变量 ,这个变量是这个模块里面有的
    print(base_type.intqq)


if __name__ == '__main__':
    # for : 声明一个for 循环;  i : 循环次数 ; range 函数,只有一个参数: 5 代表 循环 从0开始 到 4结束 (4是根据小于5的最大整数来的)
    # for i in range(5):
    #     print(i)
    #     print('hello world')
    #
    # # for : 声明一个for 循环;  i : 循环次数 ; range 函数,有两个参数: 第一个参数代表循环从3(看第一个参数的值)开始 到小于第二个参数的最大整数结束
    # for i in range(3,7):
    #     print(i)

    # for : 声明一个for 循环;  i : 循环次数 ; range 函数,有三个参数: 第一个参数代表循环从3(看第一个参数的值)开始 到小于第二个参数的最大整数结束
    # 第三个参数 代表 步长, 不写的话 每次 加 1 ,写几 每次就加几
    # for i in range(3,10,3):
    #     print(i)

    # 之前 是递增方式, 本次第三个参数 是负数 : 那就是递减的方式
    # for i in range(10,3,-1):
    #     print(i)

    alist = ['我', '你', '他', '老王', '老闫']
    # alist[0]
    # for i in range(5):
    #     # i 随循环次数变化 从0 到 4
    #     print(i)
    #     # 会吧 alist 的索引 从 0到 4 取一边
    #     print(alist[i])

    for i in alist:
        print(i)