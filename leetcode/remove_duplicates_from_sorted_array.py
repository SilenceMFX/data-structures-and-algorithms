def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0  # 处理空列表的情况

    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j = j + 1
            nums[j] = nums[i]
    return j + 1


class Solution(object):
    pass


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
