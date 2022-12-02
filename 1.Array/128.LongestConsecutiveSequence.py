from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for i in nums:
            length = 0
            if (i-1) not in unique:
                while(i in unique):
                    length = length + 1
            longest = max(length,longest)
        return longest

nums = [100,4,200,1,3,2]
sol = Solution()
res = sol.longestConsecutive(nums)
print(res)