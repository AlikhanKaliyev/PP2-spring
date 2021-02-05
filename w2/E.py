class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        t=n
        e=0
        k=1
        while(t!=0):
            e=e+t%10
            k=k*(t%10)
            t=int(t/10)
        return (k-e)
        
