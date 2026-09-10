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
            print("0 is here")
            idx = nums.index(0)
            print("the first one: ", idx)
            try:
                if nums[idx+1:].index(0)!= -1:
                    print("the second one: ", nums[idx+1:].index(0))
                    empty = [0]*len(nums)
                    return empty
            except:
                print("throws an error instead")
                arr = [0]*len(nums)
                nums.pop(idx)
                arr[idx] = math.prod(nums)
                return arr