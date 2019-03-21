def list_demo():
    alist = [4,'chenwen','8',7]
    print(alist)
    #通过索引访问 元素
    print(alist[0])
    print(alist[1])
    #倒序访问
    print(alist[-1])
    print(alist[-2])

#更新列表中的元素
def list_update(alist):
    alist[0]=1
    print(alist[0])
    print(alist)

#切片操作
def list_update1(alist):
    # 从索引2的位置 取到 索引5
    print(alist[2:6])
    #从索引0的位置索引到5
    print(alist[6])
    #从索引3的味道渠道索引末尾
    print(alist[3:])


if __name__ == '__main__':
    alist = [4,'chenwen','8',7,2,6,9,4]
    list_update(alist)