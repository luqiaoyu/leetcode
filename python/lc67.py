# 67. Add Binary

# 60ms 37.73%
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = len(a)
        n = len(b)
        a_r = a[::-1]
        b_r = b[::-1]
        loop1 = min(m, n)
        loop2 = abs(m - n)

        carry = 0
        sum = 0
        res = ''

        for i in range(loop1):
            sum = ord(a_r[i]) - ord('0') + ord(b_r[i]) - ord('0') + carry
            res += str(sum % 2)
            carry = sum // 2

        if carry == 0:
            if m > n:
                res += a_r[loop1:]
            elif m < n:
                res += b_r[loop1:]
            return res[::-1]
        else:
            if m == n:
                res += '1'
                return res[::-1]
            elif m > n:
                for j in range(loop2):
                    if a_r[loop1 + j] == '0':
                        res += '1'
                        res += a_r[loop1 + j + 1:]
                        return res[::-1]
                    else:
                        res += '0'
                res += '1'
                return res[::-1]
            else:
                for j in range(loop2):
                    if b_r[loop1 + j] == '0':
                        res += '1'
                        res += b_r[loop1 + j + 1:]
                        return res[::-1]
                    else:
                        res += '0'
                res += '1'
                return res[::-1]

# 44ms 89.76%                        
class Solution1:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""

        c = 0
        i = len(a) - 1
        j = len(b) - 1
        while (i >= 0 or j >= 0 or c == 1):    # 注意循环条件，加入c == 1很巧妙
            c += ord(a[i]) - ord('0') if i >= 0 else 0
            c += ord(b[j]) - ord('0') if j >= 0 else 0
            res = str(c % 2) + res
            c //= 2
            i -= 1
            j -= 1

        return res
        
