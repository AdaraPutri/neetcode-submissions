# two pointer
# sort the numbers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combinations = []

        for i, curr in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            complement = 0 - curr
            left, right = i + 1, len(nums) - 1

            while (left < right):
                if (nums[left] + nums[right]) == complement:
                    triplet = [curr, nums[left], nums[right]]
                    if triplet not in combinations:
                        combinations.append(triplet)
                    left += 1
                    right -= 1
                elif (nums[left] + nums[right]) < complement:
                    left += 1
                else:
                    right -= 1

        return combinations

        