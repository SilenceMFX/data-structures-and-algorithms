class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for index in range(len(digits) - 1, -1, -1):
            digits[index] += 1
            digits[index] %= 10
            if digits[index] != 0:
                return digits
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([9]))
