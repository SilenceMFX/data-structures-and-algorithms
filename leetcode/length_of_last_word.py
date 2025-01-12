class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and length > 0:
                break
            if s[i] == ' ':
                continue
            else:
                length += 1
        return length


if __name__ == '__main__':
    s = Solution()
    length = s.lengthOfLastWord("luffy is still joyboy")
    print(length)
