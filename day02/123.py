alist=[1,2,3,4,5,6,7,8,9,10]

def pop_list():
    print(alist.pop())

#将列表排序的方法
def orderby_demo():
    print('调用正序排的方法')
    sort_demo()
    print('调用倒序排的方法')
    reverse_demo()
    pass

#正序方法
def sort_demo():
    #将alist正序排
    alist.sort()
    print(alist)
    pass


#倒序方法
def reverse_demo():
    #将alist倒序排
    alist.reverse()
    print(alist)
    pass


if __name__ == '__main__':
    orderby_demo()
    #print(alist.pop())

