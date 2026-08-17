class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = min(strs)
        res = []
        for i in range(len(ref)):
            ch = ref[i]
            for j in range(len(strs)):
                if ch != strs[j][i]:
                    return "".join(res)
            res.append(ch)
        return "".join(res)
            

            

       
            


       