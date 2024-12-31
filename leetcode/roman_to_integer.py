class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s):
            j = i + 1
            if j >= len(s):
                result += nums[s[i]]
                break
            if nums[s[i]] < nums[s[j]]:
                result = nums[s[j]] - nums[s[i]] + result
                i = j + 1
            else:
                result = result + nums[s[i]]
                i = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("IX"))
