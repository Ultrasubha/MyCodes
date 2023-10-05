sqrt = lambda n: int(n ** 0.5)+1
for i in range(int(input())) :
    n = int(input())
    cnt = 0
    for i in range(1,sqrt(n)):
        if n%i == 0:
            cnt += 1
            if i != n//i:
                cnt += 1
    print(cnt)