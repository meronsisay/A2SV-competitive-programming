class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = x
        rev = 0
        if z < 0:
            return False
        while z > 0:
            last = z % 10
            rev = rev * 10 + last
            z //= 10
        return x == rev
    

       
