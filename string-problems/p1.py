"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "*")  true
isMatch("aa", "a*")  true
isMatch("ab", "?*")  true
isMatch("aab", "a*e")  false

"""

def isMatch(s, p):

        len_s = len(s); len_p = len(p)
        pPointer = sPointer = ss = 0
        star = -1
        while sPointer < len_s:
            if pPointer < len_p and (p[pPointer] == '?' or p[pPointer] == s[sPointer]):
                sPointer += 1; pPointer += 1;
                continue
            if pPointer < len_p and p[pPointer] == '*':
                star = pPointer; pPointer +=1; ss = sPointer
                continue
            if star != -1:
                pPointer = star + 1; ss += 1; sPointer = ss
                continue
            return False
        while pPointer < len_p and p[pPointer] == '*':
            pPointer += 1
        return pPointer == len_p   


print isMatch("aa","a") 
print isMatch("aa","aa")
print isMatch("aaa","aa")
print isMatch("aa", "*")
print isMatch("aa", "a*")
print isMatch("ab", "?*")
print isMatch("aab", "c*a*b")

print isMatch("a","aa") 
print isMatch("","*") 
print isMatch("","?")
print isMatch("a","a*") 

print isMatch("b","??") 
        
