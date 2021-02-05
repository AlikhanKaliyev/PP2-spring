class Solution:
    def defangIPaddr(self, address: str) -> str:
        o=''
        for i in range(len(address)):
            if address[i]!='.':
                o=o+address[i]
            else:
                o=o+'[.]'
        return o
