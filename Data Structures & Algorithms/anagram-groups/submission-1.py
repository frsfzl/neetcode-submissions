class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        res = []
        for i, s in enumerate(strs):
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())