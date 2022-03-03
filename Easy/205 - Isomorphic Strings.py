class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x, y = [], []
        for i in s:
            x.append(s.index(i))
        for i in t:
            y.append(t.index(i))
        if x == y:
            return True
        return False
