class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set nums[0] as res
        # set left and right pointer, check if left is less than right
        # if not, then find middle
        # compare if left < middle
        # if not, then move right pointer to index before middle
        # check if left < right
        # if yes, set left as res with min comparison
        # return res

        res = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            middle = (left + right) // 2
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
            res = min(res, nums[middle])

        return res