
def code0505 ():


   '''
   多行註記ㄉ頭
    t = "I'm a handsome guy"
    print (id(t))

    print (t.split(" "))
    print (len(t.split(" ")))
    print (t.split(" ")[2])
    print (type(t.split(" ")))
    print (type(t))
    print (id(t.split(" ")))
    print (len(t))

    print (t)

    i_list = [32,0,"good",0.1,22345.65]

    i_list.append(1)
    多行註記ㄉ尾'''


   i = [32,0,"good",0.1,22345.65]
    print (i)


    i.insert(3,"wow")
    print (i)

    i .pop()
    print (i)
    print(i[2])
    i.clear()
    print (i)

    t = (3, 10,  5)
    print (t)

    dd = {'aa':2,'bb':'s'}
    print(dd)
    dd['aa'] = 20
    dd[123]=1234
    print (dd)
    del dd ['aa']
    print (dd)


    list_2 = [set(dd)]
    print (list_2)

    list_1 = ['1','2','1','3','4','1','2']
    list_2 = list(set(list_1))
    list_2.sort()
    print(list_2)


#command + shift + p = 呼叫各個快捷鍵ㄉ解釋＋按鈕