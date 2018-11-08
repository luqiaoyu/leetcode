# 8. String to Integer (atoi)

# 80ms 41.84%
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        
        res = 0
        flag = False
        sign = True
        for x in str:
            if flag:
                temp = ord(x) - ord('0')
                if (0 <= temp <= 9):
                    if sign:
                        if (res > (2 ** 31 - 1) // 10 or (res == (2 ** 31 - 1) // 10 and temp > 7)):
                            return 2 ** 31 - 1
                    else:
                        if ((res > (2 ** 31 - 1) // 10 or (res == (2 ** 31 - 1) // 10 and temp > 8))):
                            return - 2 ** 31
                    res = res * 10 + temp
                else:
                    break
            else:
                if x == '-':
                    flag = True
                    sign = False
                    continue
                if x == '+':
                    flag = True
                    sign = True
                    continue
                if x == ' ':
                    continue
                temp = ord(x) - ord('0')
                if (0 <= temp <= 9):
                    flag = True
                    sign = True
                    res = res * 10 + temp
                else:
                    break
        return res if sign else - res
                        
