class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        total = 0
        mod = 10**9 + 7
        for i in range(delay, n):
            total += dp[i - delay]
            dp[i] = total
            if i - forget + 1 >= 0:
                total -= dp[i - forget + 1]
        return (sum(dp[-forget:])) % mod 