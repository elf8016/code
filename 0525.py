"""
def code():
    print("o")


def func(p1, p2=10, *args, **kwargs):
    print("p1 =", p1)
    print("p2 =", p2)
    print("args =", args)
    print("kwargs =", kwargs)


aa = {12, 34, 2, "a", 3.221}

func(0, 1, 24, 4.22, kw0=20, kw4=5.23, kw6=[1, 3, "a"])
# func(10, 20,30)



aa = {"t1": "12", "t2": "3", "t3": 21}
bb = (2, 1, 5)
print(**aa)
print(*bb)
"""

def tt(p1,p2,/,p3,kw0=100,*,p10,kw1=1,kw2=20):
    print('p1 =',p1)
    print('p2 =',p2)
    print('p3 =',p3)
    print('kw0 =',kw0)
    print('p10 =',p10)
    print('kw1 =',kw1)
    print('kw2 =',kw2)

    for i in range(10):
        if a == b:
            

tt(0,1,100, p10=10)
