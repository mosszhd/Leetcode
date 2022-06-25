from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        res = []
        for i in candies:
            candies_each = i + extraCandies
            if candies_each >= max_candies:
                res.append(True)
                #max_candies = candies_each
            else:
                res.append(False)
        return res


solution = Solution()
print(solution.kidsWithCandies([4,2,1,1,2],1))