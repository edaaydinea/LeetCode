from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length_nums = len(nums)
        if length_nums == 0:
            return length_nums
        count = 0
        index = 0
        while index < length_nums - count:
            if nums[index] == val:
                nums[index] = nums[length_nums - 1 - count]
                count += 1
            else:
                index += 1
        return length_nums - count
