#!/usr/bin/python
"""
Purpose: 
https://leetcode.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
Given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

Constraints:

    0 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It's guaranteed that all parentheses are balanced.
"""


class Solution:
    def reverseParentheses(self, s):
        if '(' not in s:
            return s
        s = s.replace('()', '')
        if s.rfind('(') < s.find(')'):
            substring = s[s.rfind('('): s.find(')') + 1]
        else:
            substring = s[s.find('('):s.find(')') + 1]
            if substring.count('(') > 1:
                substring = substring[substring.rfind('('): substring.find(')') + 1]
        s = s.replace(substring, substring[::-1].strip('()'))
        return self.reverseParentheses(s)

    def reverseParentheses(self, s):
        st = []
        for i in s:
            if i == '(':
                st.append('(')
            elif i != ')':
                st.append(i)
            elif i == ')':
                word = ''
                while st[-1] != '(':
                    word += st.pop(-1)
                # print(f'word is now {word}')
                # print(f'st is {st}' )
                st.pop(-1)
                for letter in word:
                    st.append(letter)
        res = ''
        for letter in st:
            res += letter
        return res


assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
# (ed(et(oc))el)
# (ed(etco)el)
# (edocteel)
# leetcode
assert Solution().reverseParentheses("(abcd)") == "dcba"
assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
assert Solution().reverseParentheses("ta()usw((((a))))") == "tauswa"
assert Solution().reverseParentheses("sxmdll(q)eki(x)") == "sxmdllqekix"
assert Solution().reverseParentheses("wnb(((z()qw)eyt)(bx(()ye)))") == "wnbbxeywqzeyt"
assert Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
