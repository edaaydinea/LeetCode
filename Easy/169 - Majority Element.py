class Solution:
    def majorityElement(self, nums):
        maj = nums[0]
        count = 0
        for i in nums:
            if (maj == i):
                count += 1
            else:
                count -= 1
            if (count == 0):
                maj = i
                count += 1
        return maj
