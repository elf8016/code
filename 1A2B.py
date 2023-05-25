import random


def MakeAns():
    list = [0, 0, 0, 0]

    while list[0] == 0:
        for i in range(4):
            aa = random.randrange(10)
            list[i] = aa
            print(list)
        
        ListLen = len(set(list))
        if ListLen != 4:
            list[0] = 0

        continue

    return list


def CheckGuess(x: str):
    Lenght = len(x)
    xListLen = len(list(set(x)))

    # 判斷str內是否只有四個（包含英文、數字、空白）
    if Lenght != 4:
        print("\033[31m !!!!!! 4-Error !!!!!! \033[0m")
        return False

    # 判斷str內是否只有數字，是＝true
    if x.isdigit() == False:
        print("\033[31m !!!!!! Number-Error !!!!!! \033[0m")
        return False

    # 判斷input是否重複
    if xListLen != 4:
        print("\033[31m !!!!!! Repeat-Error !!!!!! \033[0m")
        return False

    return True


def lookGuess(G, A):
    listAB = [0, 0]
    for i in range(4):
        for k in range(4):
            if A[i] == G[k]:
                if i == k:
                    listAB[0] = listAB[0] + 1
                else:
                    listAB[1] = listAB[1] + 1

    return listAB


if __name__ == "__main__":
    Ans = MakeAns()
    Guess = input()
    CheckG = CheckGuess(Guess)
    CheckA = [0,0]

    while CheckA[0] != 4:
        
        while CheckG != True:
            Guess = input()
            CheckG = CheckGuess(Guess)
            continue

        Guess = list(Guess)
        Guess = list(map(int,Guess))
        CheckA = lookGuess(Guess, Ans)
        print("A :",CheckA[0],"   B :",CheckA[1])
        CheckG = False
        continue
    
    print("A :",CheckA[0],"B :",CheckA[1])
    print("End")
