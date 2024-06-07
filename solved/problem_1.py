n = 1000
sum_ = 0
for i in range(0, n):
    if i % 5 == 0 or i % 3 == 0:
        sum_ += i
print(sum_)