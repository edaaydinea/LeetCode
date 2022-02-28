class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev, total = 0, 0
        for c in s:
            curr = roman[c]
            total += curr

            if curr > prev:
                total -= 2 * prev
            prev = curr
        return total
