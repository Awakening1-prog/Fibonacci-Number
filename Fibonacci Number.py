class Solution:
    def fib(self, N: int) -> int:
        dp=[0]*(N+1)
        if N==0:
            return 0
        if 0<N<=1:
            return 1
        dp[0]=1
        dp[1]=1
        for i in range(2,N+1):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp)
        return dp[N-1]
