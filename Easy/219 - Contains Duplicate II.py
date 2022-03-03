class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        for i in range(len(nums)):
            if i > k:
                check.remove(nums[i - k - 1])
            if nums[i] in check:
                return True
            else:
                check.add(nums[i])
        return False
