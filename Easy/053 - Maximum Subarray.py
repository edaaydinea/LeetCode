class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -90000
        currSum = 0
        for i in nums:
            currSum += i
            if currSum > maxSum:
                maxSum = currSum
            if currSum < 0:
                currSum = 0
        return maxSum
