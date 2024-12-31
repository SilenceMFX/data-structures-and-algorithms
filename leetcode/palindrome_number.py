class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        for i in range(0, len(x)):
            j = len(x) - 1 - i
            if j <= i:
                return True
            if x[i] != x[j]:
                return False
        return True

    def isPalindrome2(self, x):
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(0))
