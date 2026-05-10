class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        sequence = 0
        for num in numbers:
            i = num
            if i - 1 not in numbers:
                length = 1
                while i + 1 in numbers:
                    length += 1
                    i += 1
                sequence = max(sequence, length)
        return sequence