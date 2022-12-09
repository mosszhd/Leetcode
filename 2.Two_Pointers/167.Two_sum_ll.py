from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_index = 0
        end_index = len(numbers) - 1
        while start_index<end_index:
            sum = numbers[start_index] + numbers[end_index]
            if(sum == target):
                return [start_index+1,end_index+1]
            elif(sum > target):
                end_index -=1
            elif(sum < target):
                start_index +=1
        return []

sol = Solution()
print(sol.twoSum(numbers = [2,7,11,15], target = 9))
            
