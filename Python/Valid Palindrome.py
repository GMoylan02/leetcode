class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = format(s)
        if len(s) == 0:
            return True
        for i in range(int(len(s)/2)):
            if not s[i] == s[len(s)-1-i]:
                return False
        return True

def format(s):
    s = s.lower()
    result = ""
    for i in range(len(s)):
        if (0 <= ord(s[i]) - 97 < 26) or (0 <= ord(s[i])-48 <= 9):
            result += s[i]
    print(result)
    return result