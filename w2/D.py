class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max=0
        lol=[0]
        k=0
        for i in range(0,len(gain)):
           k=k+gain[i]
           lol.append(k)
        lol.sort()
        return lol[len(gain)]
