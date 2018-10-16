# 415. Add Strings

# 大数加法: 64ms
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result_r = ""
        num1_r = num1[::-1]
        num2_r = num2[::-1]
        i = 0
        s = 0
        while(i < len(num1) or i < len(num2)):
            if(i < len(num1) and i < len(num2)):
                temp = int(num1_r[i]) + int(num2_r[i]) + s
                res = temp % 10
                s = temp // 10
                result_r += str(res)
            elif(i < len(num1) and i >= len(num2)):
                temp = int(num1_r[i]) + s
                res = temp % 10
                s = temp // 10
                result_r += str(res)
            else:
                temp = int(num2_r[i]) + s
                res = temp % 10
                s = temp // 10
                result_r += str(res)
            i += 1
        if s > 0:
            result_r += str(s)
        result = result_r[::-1]
        return result

        
