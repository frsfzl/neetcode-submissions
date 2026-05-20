class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            current = 1
            k = num
            while k + 1 in nums_set:
                current += 1
                k += 1
            longest = max(current, longest)
        return longest