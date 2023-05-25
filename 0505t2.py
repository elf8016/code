import random

list = [0, 0, 0, 0]
ListLen = 0

while list[0] == 0:
    for i in range(4):
        aa = random.randrange(10)
        list[i] = aa
        print(list)
        
    ListLen = len(set(list))
    if ListLen != 4:
        list[0] = 0

    continue





