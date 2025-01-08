def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 1:
        return False
    stack = list()
    mapping = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in mapping:
            if not stack or stack[-1] != mapping[i]:
                return False
            stack.pop()
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True


class Solution(object):
    pass


if __name__ == '__main__':
    sol = Solution()
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([])"))
