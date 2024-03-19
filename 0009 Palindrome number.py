class Solution(object):
    def isPalindrome(self, x):
        strx = str(x)
        revx = strx[::-1]
        return revx==strx
