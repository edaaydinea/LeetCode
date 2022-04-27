class NumArray:

    def __init__(self, nums: List[int]):
        self.lst = []
        total = 0
        for i in nums:
            total += i
            self.lst.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.lst[right] - self.lst[left - 1]
        else:
            return self.lst[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
