import random

def keyword():
    key = random.randrange(1000, 9999)
    for number in range(4):
        key = set(key)
        if (key < 1000):
      
    return key
    


print(keyword())






