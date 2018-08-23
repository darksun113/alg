def RecursiveFibonacci(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    return RecursiveFibonacci(n-2) + RecursiveFibonacci(n-1)

def BottomUpFibonacci(n):
    memo = [0]*(n+1)
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def CompressedBottomUpFibonacci(n):
    memo_i = 1
    memo_i_1 = 1
    memo_i_2 = 0
    for i in range(2, n+1):
        memo_i = memo_i_1 + memo_i_2
        memo_i_2 = memo_i_1
        memo_i_1 = memo_i
    return memo_i

class UpDownFibonacci:
    def __init__(self,num):
        self.n = num
        self.memo = [-1]*(num+1)
    
    def fib(self, num):
        if(self.memo[num]!=-1):
            return self.memo[num]
        if(num<=2):
            self.memo[num]=1
        else:
            self.memo[num] = self.fib(num-2) + self.fib(num-1)
            
        return self.memo[num]
        


print(RecursiveFibonacci(6))
udf = UpDownFibonacci(6)
print(udf.fib(6))
print(BottomUpFibonacci(6))
print(CompressedBottomUpFibonacci(6))

