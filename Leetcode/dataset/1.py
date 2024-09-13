class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [(x,i) for i, x in enumerate(nums)]
        new_nums = sorted(new_nums, key=lambda x:x[0])
        i, j = 0, len(new_nums) - 1
        while i < j:
            if new_nums[i][0] + new_nums[j][0] > target:
                j -= 1
            elif new_nums[i][0] + new_nums[j][0] < target:
                i += 1
            else:
                return [new_nums[i][1], new_nums[j][1]]