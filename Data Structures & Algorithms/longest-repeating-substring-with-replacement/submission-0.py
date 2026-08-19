class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count = {}
        ans=0
        for r in range(len(s)):
            if s[r] not  in count:
                count[s[r]] = 1
            else:
                count [s[r]] +=1
            
            max_freq = max(count.values())

            replacements = (r - l + 1) - max_freq

            if replacements > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans