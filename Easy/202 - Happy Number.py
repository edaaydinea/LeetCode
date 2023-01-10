class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            square_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                square_sum += pow(digit, 2)
            return square_sum

        while n != 1 and n != 4:
            n = get_next_number(n)

        return n == 1
