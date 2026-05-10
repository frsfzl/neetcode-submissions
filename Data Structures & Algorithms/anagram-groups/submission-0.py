class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in count:
                count[key] = []
            count[key].append(s)
        
        return list(count.values())
            

        