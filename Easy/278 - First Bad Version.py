# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 0
        last = n
        while first <= last:
            mid = (first + last) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    last = mid - 1
            else:
                first = mid + 1
        return -1
