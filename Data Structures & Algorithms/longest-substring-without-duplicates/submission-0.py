class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        h=set()
        ans=0

        for r in range(len(s)):
            while s[r] in h:
                h.remove (s[l])
                l+=1
            h.add(s[r])
            ans = max(ans,r-l+1)
        return ans