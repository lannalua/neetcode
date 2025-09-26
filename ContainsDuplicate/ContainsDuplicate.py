"""
Given an integer array nums, return true if any value appears more 
than once in the array, otherwise return false.
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        checked = set()
        self.nums = nums

        for i in range(len(self.nums)):
            if self.nums[i] not in checked:
                checked.add(self.nums[i])
            else:
                return True
        return False

def main():
    nums = [1, 2, 3, 4]
    results = Solution()
    print(results.hasDuplicate(nums))

main()