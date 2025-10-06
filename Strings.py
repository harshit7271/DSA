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
# Example usage:
s = "abcde"
goal = "cdeab"
solution = Solution()
print(solution.rotateString(s, goal))
    
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


# Sort Characters By Frequency
from collections import Counter
class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = ''.join([i*j for i, j in sorted_chars])
        return result
    
# Example usage:
s = "tree"  
solution = Solution()
print(solution.frequencySort(s))


# MAXIMUM NESTING DEPTH OF THE PARENTHESES
class Solution:
    def maxDepth(self, s):
        current_depth = 0
        max_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth
    
# Example usage:
s = "(1+(2*3)+((8)/4))+1"
solution = Solution()
print(solution.maxDepth(s))


# Roman number to Integer
class Solution:
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for i in s:
            current_value = roman_numerals[i]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value
            prev_value = current_value
        return total
    
# Example usage:
s = "MCMXCIV"
solution = Solution()
print(solution.romanToInt(s))

# Integer to Roman
class Solution:
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        return roman_numeral
    
# String to Integer (atoi)
class Solution:
    def myAtoi(self, s):
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        
        num *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
    
# Example usage:
s = "   -42"    
solution = Solution()
print(solution.myAtoi(solution))


# REVERSE A STRING

class Solution(object):
    def reverseString(self, s):    
        s.reverse()         # when s is already a list otherwise convert it in list if its an array
        return "".join(s)   # this will merge the list 
    

# MIN MAX SUM IN AN ARRAY

class Solution:
    def findSum(self, A, N):
      
        #if N == 1:
         #   return A[0] * 2
        
        #mini = maxi = A[0]
        #for i in range(1, N):
            #if A[i] > maxi:
                #maxi = A[i]
            #elif A[i] < mini:
                #mini = A[i]
        #return maxi + mini
        #OR
        return max(A) + min(A)



