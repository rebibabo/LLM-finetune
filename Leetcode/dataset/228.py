class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start, p, span, ans = nums[0], nums[0], 1, []
        for n in nums[1:]:
            if n == p + 1:
                span += 1
            else:
                if span == 1:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{p}")
                    span = 1
                start = n    
            p = n
        if span == 1:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{p}")
        return ans