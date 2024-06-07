'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers first reaches 58% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

import time

starttime = time.time()

def check_increasing(n:int):
    prev=0
    for i in [int(x) for x in list(str(n))]:
        if not i>=prev:
            return False
        prev=i
    return True

def check_decreasing(n:int):
    prev=9
    for i in [int(x) for x in list(str(n))]:
        if not i<=prev:
            return False
        prev=i
    return True

def check_bouncy(n:int):
    if not check_decreasing(n) and not check_increasing(n):
        return True
    return False

searching=True
num=0
bouncy=0
while searching:
    if check_bouncy(num):
        bouncy+=1
        if bouncy/num>=0.99:
            searching=False
    num+=1

print(num-1)
print(time.time()-starttime)