def fibonacci(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fibonacci(num-2) + fibonacci(num-1)


n = int(input())
for i in range(0, n):
	print(fibonacci(i), end=" ")
