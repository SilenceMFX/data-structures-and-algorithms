class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return j


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    print(k)
