# 34. Find First and Last Position of Element in Sorted Array

# 方法一：先判断是否存在，再利用bisect库判断是在哪儿: 60ms
import bisect

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        flag = self.biSearch(nums, target) # 注意调用类内部方法的方式
        if flag == False:   # 不要用~, ~似乎是按位取反
            return [-1, -1]
        else:
            return [bisect.bisect_left(nums, target), bisect.bisect(nums, target) - 1]

    def biSearch(self, nums, target):
        left, right = -1, len(nums)
        while(left + 1 != right):
            mid = (left + right) // 2 # 注意python3中默认(left + right) / 2是float,这里要用//
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return False

'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

    def biSearchLeft(self, nums, target):
        left, right = -1, len(nums)
        while(left + 1 != right):
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid


    def biSearchRight(self, nums, target):
'''

'''
# trick method: 72ms
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums:
            return [bisect.bisect_left(nums, target), bisect.bisect(nums, target) - 1]
        else:
            return [-1, -1]
'''