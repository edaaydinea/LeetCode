class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, cache):
            if n not in cache:
                cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
            return cache[n]

        return dp(n, {1: 1, 2: 2})
