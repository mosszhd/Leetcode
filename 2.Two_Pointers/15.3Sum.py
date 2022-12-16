from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and v == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                th_sum = v + nums[l] + nums[r]
                if(th_sum == 0):
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1]:
                        l += 1
                elif th_sum < 0:
                    l += 1
                elif th_sum > 0:
                    r -= 1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))

[2,2,4,3,1]