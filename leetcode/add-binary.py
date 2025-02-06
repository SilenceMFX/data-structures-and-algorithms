class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            a_bit = int(a[i]) if i >= 0 else 0
            b_bit = int(b[j]) if j >= 0 else 0

            total = a_bit + b_bit + carry
            carry = total // 2
            res.append(str(total % 2))

            i -= 1
            j -= 1

        # 反转结果并处理前导零
        res_str = ''.join(reversed(res))
        res_str = res_str.lstrip('0')

        return res_str if res_str else '0'
