class Solution:
    def findMin(self, nums: List[int]) -> int:
        # normally, you would just perform binary search by dividing the input into two parts each time. but here, we have to sort the elements in ascending order first
        prev = -1001
        for i, curr in enumerate(nums):
            if curr > prev:
                if i is not len(nums)-1:
                    prev = curr
                else:
                    return nums[0]
            elif curr < prev:
                return curr