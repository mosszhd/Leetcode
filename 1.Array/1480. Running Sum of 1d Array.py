class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        arr.append(nums[0])
        for i in range(1,len(nums)):
            arr.append(nums[i]+arr[i-1])
        return arr

# sol = Solution()
# print(sol.runningSum([1,2,3,4]))