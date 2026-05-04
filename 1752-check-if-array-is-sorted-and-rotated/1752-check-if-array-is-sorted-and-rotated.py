class Solution:
    def check(self, nums: List[int]) -> bool:
        def check_sort(arr):
            l = 0
            for r in range(1, len(arr)):
                if arr[l] > arr[r]:
                    return False
                l += 1
            return True
            
        new_arr = nums[:]
        for i in range(len(nums)):
            first = new_arr[0]
            if not check_sort(new_arr):
                new_arr = new_arr[1:]
                new_arr.append(first)
            else:
                return True
        return False

        