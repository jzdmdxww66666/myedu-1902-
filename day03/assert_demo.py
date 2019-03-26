if __name__ == '__main__':
    ##断言为ture 不会有报错
    #assert 4>2
    ##断言为false会报错 AssertionError
    #assert 1>2
    ##断言字符串
    astr = '的经费和大家回复大家更好地'
    ##判断astr字符内 是有包含  你 这个字
    #assert '你 'in astr
    ##判断 astr字符内 是否不包含 你 这个字
    #assert '你 'not in  astr

    #a=0
    ##while语法 ： while（当）条件：--> 条件为true 进入循环， 知道 条件为false
    #while a<5:
    #    print('hellow world')
    #    a+=1
    #try用于异常处理；如果出现异常 则执行except内的代码；不会影响后面的代码 继续执行
    #应用场景；用于包裹 可能会出错的代码块，出错执行except内的代码，
    #try:
    #    assert '你' in astr
    #except:
    #    print('报错了')


