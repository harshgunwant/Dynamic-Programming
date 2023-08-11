import time
class Solution:
    def fib(self, n)->int:
        ##RECURSION - NO DP
        # ##base case
        # if n == 1 or n == 0:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)
        ## here TC:O(2^n) and SC:O(2^n) for recursion stack

        ## SOLUTION USING MEMOIZATION + DP
        # dp={}
        # ##base case
        # if n==1 or n==0:
        #     return n
        # if (n) in dp:
        #     return dp[(n)]
        # dp[(n)]=self.fib(n-1)+self.fib(n-2)
        # return dp[(n)]
        ## TC: O(N) and SC:O(n)+O(n) for recursion stack + array

        ## SOLUTION USING RECURSION + TABULATION.
        dp=[-1]*(n+1)
        dp[0],dp[1]=0,1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    ## TC: O(n) and SC: O(n)''here we are not using any recursion stack space(less Memo usage)

    ## we can even optimize the above solution by using prev, curr, prev2 as pointers.
    ## this will lead to constant memory.
    
##try making a whole tree and then see by yourself if the base case is correct or not.

## the above commented code will work efficiently for small n, but for larger n it
## will give a TLE as the above solution has a TC of O(2^n).

## then we have used the memoization technique to store the pre calculated values.



sol=Solution()
s=time.time()
obj=sol.fib(8)
## it is  ms for n=40 when we use Memoization
### it is  ms for n=40 when we do it using recursion.
e=time.time()
print(obj)
print('The time taken is: ', e-s," ms")