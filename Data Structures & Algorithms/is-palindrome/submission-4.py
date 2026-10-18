class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(i for i in s if i.isalnum())
        print(s)
        print("".join(reversed(s)))
        return (s == "".join(reversed(s)))
        