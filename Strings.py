# Remove outermost Parentheses
class Solution:
    def removeOuterParentheses(self, s):
        result = []
        open_count = 0
        
        for char in s:
            if char == '(':
                if open_count > 0:
                    result.append(char)
                open_count += 1
            elif char == ')':
                open_count -= 1
                if open_count > 0:
                    result.append(char)
        
        return ''.join(result)
# Example usage:
s = "(()())(())"    
solution = Solution()
print(solution.removeOuterParentheses(s)) 

# Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""   
    
# Example usage:
num = "35427"   
solution = Solution()
print(solution.largestOddNumber(num))


# Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num):
        max_good_integer = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good_integer = num[i:i + 3]
                if good_integer > max_good_integer:
                    max_good_integer = good_integer
        
        return max_good_integer
# Example usage:
num = "6777133339"  
solution = Solution()
print(solution.largestGoodInteger(num))


# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()

        first = strs[0]
        last = strs[-1]

        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return ans
# Example usage:
strs = ["flower","flow","flight"]       
solution = Solution()
print(solution.longestCommonPrefix(strs))

        
# Isomorphic Strings
class Solution:
    def isIsomorphic(self,s,t):
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for i, j in zip(s, t):   # we use zip to iterate over both strings simultaneously
            if i not in s_to_t:
                s_to_t[i] = j
            elif s_to_t[i] != j:
                return False
            
            if j not in t_to_s:
                t_to_s[j] = i
            elif t_to_s[j] != i:
                return False
        
        return True
# Example usage:
s = "egg"   
t = "add"
solution = Solution()
print(solution.isIsomorphic(s, t))

# rotate string
class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        return goal in (s + s)
    
# Valid Anagram  (a word or phrase formed by rearranging the letters of a different word or phrase)
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
# Example usage:
s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))
