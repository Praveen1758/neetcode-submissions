class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}

        for i in strs:
            key = "".join(sorted(i))

            if key not in h:
                h[key]=[]
            
            h[key].append(i)

        return list(h.values())