
def list_bianli():
    alist = ['阿','第三方','二二','玩玩']
    for i in alist:
        print(i)
        print(i+'__hello')

def neixunhuan():
    for i in range(5):
        print('hello world')
        for j in range(2):
            print('内循环')

def chenfabiao():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s X %s = %s' %(i,j,i*j),end=' ')
            print('')
#if else 语法演示
def if_demo():
    a =False
    if a:
        print('a 是 对的')
    else:
        print('a 是 错的')

# 判断 a和b的大小
def if_demo1():
    a=10
    b=20
    if a>b:
        print('a大于b')
    else:
        print('a小于b')

#输出比较大的值
def if_demo2():
    a =10
    b =20
    if a>b:
        print(a)
    else:
        print(b)

def oushu(aint,bint):
    nub=0
    if aint>bint:
        for i in range(bint+1,aint):
            if i%2==0:
                nub = nub + i
        print(nub)
    else:
        for i in range(aint+1,bint):
            if i%2==0:
                nub = nub + i
        print(nub)




if __name__ == '__main__':
    oushu(12,79)
    #nub=0
    #for i in range(1,51):
    #     #    if i%2 !=0:
    #        nub = nub+i
    #print(nub)

