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

def FactorialDigiCount(num): #T(n) = O(1) space = O(1)
    if n < 0:
        return 0
    if n <= 1:
        return 1
    x = (n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2.0)
    return math.floor(x) + 1

def Factorial(num):	#T(n) = θ(n) space = θ(1)
    val=1
    for i in range(2,num+1):
        val*=i
    return val

def rFactorial(num): # 	T(n) = T(n-1) + θ(1) space = θ(n)
    if num<2:
        return 1
    return num*rFactorial(num-1)

def trailingZero(num):  #T(n) = θ(1)
    val=0
    while num>=5:
        num//=5
        val+=num
    return val

def gcd(a, b):           #T(n) = O(Log min(a, b))
    if a == 0 :
        return b
    return gcd(b%a, a)

def lcm(a, b):           #T(n) = θ(1)
    return (a*b)//gcd(a,b)

def isPrime(n):         #T(n) = θ(√n)
    if n<2:
        return False
    if n<4:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    else:
        return True
    
def divisorsOf(n):      #T(n) = θ(√n) space = θ(1)
    arr=[]
    sqrt = int(n**0.5) + 3
    for i in range(1,sqrt):
        if n%i==0:
            arr.append(i)
    for j in reversed(range(1,i-2)):
        if n%j==0:
            arr.append(n//j)
    return arr

def sieve(n):           #T(n) = nloglog(n)
    isItPrime=[True]*(n+1)
    for i in range(2,n+1):
        if isItPrime[i]:
            yield i
            for j in range(i*i,n+1,i):
                isItPrime[j] = False

def expo(x,n,m):        #T(n) = O(log(n)) space = O(1)
    val=1
    while n>0:
        if n&1:
            val = (val*x) % M
        x = (x * x) % M
        n>>=1; # dividing by 2
    return val

M = 1000000007

for i in range(250):
    if isPrime(i):
        print(i, end=" ")