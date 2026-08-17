class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def find(s, t):
            l, r = 0, 0
            res = []
            while l < len(s) and r < len(t):
                if s[l] != t[r]:
                    return "".join(res)
                res.append(s[l])
                l += 1
                r += 1 
            return "".join(res)

        if len(strs) == 1:
            return strs[0]
        common = strs[0]
        for i in range(1, len(strs)):
            common = find(common, strs[i])
        return common



     
            

            

       
            


       