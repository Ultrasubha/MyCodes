def isPalindrome(num):
	temp=num
	rev=0
	while temp>0:
		rem=temp%10
		temp//=10
		rev=rev*10+rem
	if rev==num:
		return True
	else:
		return False

def Factorial(num):	#T(n) = θ(n) space = θ(1)
    val=1
    for i in range(2,num+1):
        val*=i
    return val

def rFactorial(num): # 	T(n) = T(n-1) + θ(1) space = θ(n)
    if num<2:
        return 1
    return num*rFactorial(num-1)

def trailingZero(num):
    val=0
    while num>=5:
        num//=5
        val+=num
    return val

def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a)

print(trailingZero(10))