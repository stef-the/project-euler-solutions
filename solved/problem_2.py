# Even sum of fibonacci to 4 million
start = [1, 2]

while start[-1] < 4000000:
    start.append(start[-1]+start[-2])

print(sum([x if x % 2 == 0 else 0 for x in start]))