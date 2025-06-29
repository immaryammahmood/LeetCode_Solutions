class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        last_dup = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[last_dup] = nums[i]
                last_dup += 1
        return last_dup