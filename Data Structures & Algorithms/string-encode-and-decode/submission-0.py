class Solution:

    def encode(self, strs: List[str]) -> str:
        a=""
        for i in strs:
            a+=(str(len(i))+"#" + i)
        
        return a

    def decode(self, s: str) -> List[str]:
        ans=[]
        
        i=0
        j=0
        while j+1 <= len(s):
            if s[j] == "#":
                length = int(s[i:j])
                ans.append(s[j+1:(j+1)+length])
                i = j+length+1
                j = j+length+1 
            else:
                j+=1

        return ans