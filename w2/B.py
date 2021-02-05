class Solution:
    def interpret(self, command: str) -> str:
        o=''
        s=command
        for i in range(len(s)):
            if i<len(s)-3:
                if s[i]+s[i+1]+s[i+2]+s[i+3]=='(al)':
                    o=o+'al'
            if i<len(s)-1:
                if s[i]+s[i+1]=='()':
                    o=o+'o'
            if s[i]=='G':
                o=o+'G'
            
        return o
