# 71. Simplify Path

# stack
# 40ms 100%
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_l = path.split('/')
        for x in path_l:
            if x == '' or x == '.':
                continue
            if x == '..':
                if len(stack) != 0:
                    stack.pop()
                continue

            stack.append(x)

        if len(stack) == 0: return '/'
        res = ''
        for x in stack:
            res = res + '/' + x
        return res