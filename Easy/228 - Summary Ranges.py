class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for num in nums:
            if not ranges or num > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = num,

        return ['->'.join(map(str, r)) for r in ranges]
