class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) < 2:
            return []
        result = []
        for i in range(len(nums)):
            if target - nums[i] in result:
                return [nums.index(target - nums[i]), i]
            else:
                result.append(nums[i])
        return result


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
