from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length_arr = len(nums)
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

sol = Solution()
print(sol.shuffle([1,2,3,9,8,7],3))