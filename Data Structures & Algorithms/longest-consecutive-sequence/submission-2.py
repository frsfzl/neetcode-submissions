class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if num - 1 in nums:
                continue
            current = 1
            k = num
            while k + 1 in nums:
                current += 1
                k += 1
            longest = max(current, longest)
        return longest