class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: #type: ignore
        dict = {}
        for i in range(len(nums)):
           difference = target - nums[i]
           if difference in dict:
                return [dict[difference],i]
           dict.update({nums[i]:i})

