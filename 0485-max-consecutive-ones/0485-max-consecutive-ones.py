class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maxi = 0, 0
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                count = 0
            maxi = max(maxi, count)
        return maxi


       