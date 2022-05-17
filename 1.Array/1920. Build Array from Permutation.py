class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            arr.append(nums[i])
        return arr
        
sol = Solution()
print((sol.buildArray([0,2,1,5,3,4])))
