import random


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
    list1 = [1, 2, 5, 8]
    list2 = list(input())
    list2 = list(map(int,list2))
    CheckA = lookGuess(list2, list1)
    print(CheckA)
