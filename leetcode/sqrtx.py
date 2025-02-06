class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(2))
    print(solution.mySqrt(8))
    print(solution.mySqrt(9))
    print(solution.mySqrt(25))
