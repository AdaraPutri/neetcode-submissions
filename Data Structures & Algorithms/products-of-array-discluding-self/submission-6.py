import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            product = math.prod(nums)
            arr = []
            for n in nums:
                arr.append(int(product/n))
            return arr
        elif 0 in nums:
            idx = nums.index(0)
            try:
                if nums[idx+1:].index(0)!= -1:
                    empty = [0]*len(nums)
                    return empty
            except:
                arr = [0]*len(nums)
                nums.pop(idx)
                arr[idx] = math.prod(nums)
                return arr