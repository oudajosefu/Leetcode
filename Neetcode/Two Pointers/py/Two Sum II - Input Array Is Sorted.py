from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers) - 1
        sum = numbers[p1] + numbers[p2]

        while sum != target:
            if sum < target:
                p1 += 1
            else:
                p2 -= 1
            sum = numbers[p1] + numbers[p2]
        
        return [p1+1, p2+1]

sol = Solution()
numbers = [-1,0]
target = -1
print(sol.twoSum(numbers, target))