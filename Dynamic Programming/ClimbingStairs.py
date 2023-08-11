class Solution:
    def climbStairs(self, n: int) -> int:
        ##made changes to normal recursion that was giving TLE by using Memoization.
        # dp=[-1]*(n+1) ##we can also use here a hashmap as well.
        #
        # def solve(n):
        #     if dp[n]!=-1:
        #         return dp[n]
        #     ##base case
        #     if n==0:
        #         return 1
        #     if n<0:
        #         return 0
        #     dp[n]=solve(n-1)+solve(n-2)
        #     return dp[n]
        # return solve(n)

        ##doing Tabulation
        dp=[-1]*(n+1)
        dp[1],dp[2]=1,2
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

sol=Solution()
print(sol.climbStairs(5))