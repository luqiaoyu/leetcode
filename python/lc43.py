# 43. Multiply Strings

# index i * index j --> index i + j, index i + j + 1: 160ms
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        pos = [0 for i in range(m + n)]

        # from right to left!
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                temp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sum = temp + pos[p2]

                pos[p2] = sum % 10
                pos[p1] += sum // 10
        
        res = ""
        for p in pos:
            if len(res) != 0 or p != 0: res += str(p)
        return res if len(res) != 0 else "0"
