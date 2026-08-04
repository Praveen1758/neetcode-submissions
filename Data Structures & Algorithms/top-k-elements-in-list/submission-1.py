class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}

        for i in nums:
            if i not in h:
                h[i]=1

            else:
                h[i]+=1

        a=[]
        a=sorted(h.items(), key=lambda x: x[1], reverse=True)
        b=[]
        for i in a[:k]:
            b.append(i[0])
            # b.append(i[1])
        return b