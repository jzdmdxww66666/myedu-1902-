
if __name__ == '__main__':
    #for i in range(5):
    #    print(i)
    #    # 如果i 等于3
    #    if i ==3:
    #        # 终止所有循环
    #        break
    #    print('第%s次循环' % i)

    for i in range(5):
        print(i)
        # 如果i 等于3
        if i ==3:
            continue
        #%s:占位符 %i：i是变量 加百分号就是被替换的内容
        print('第%s次循环' % i)#