#!/usr/bin/python
"""
Purpose: https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""
import time


class Solution:
    def __init__(self):
        self.start_time = time.time_ns()

    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        for _index, _ in enumerate(s):
            sub_str = s[:_index] + s[_index + 1:]
            if sub_str == sub_str[::-1]:
                return True
            # print(sub_str, sub_str == sub_str[::-1])
        return False

    def __del__(self):
        print(f'Time Taken : {time.time_ns() - self.start_time}ns')


print(Solution().validPalindrome(
    "sxigqizmbopbyluwxmehcqudofdjadhsteappejrnxyfoxobpdlpuhzkojxabyybmlsviemdjtptxoatpiztvebbbsmozxcomjyudelcmzmpadftmegvhudcivnpuondhapibzvtrlokydxswdihcmsoupfohwuyoamglrwptvixhgjhskjiyyymwciynhmdjtavvzrlxgqwmzkcpoainizfgacmixzmoakwwrslrsbfcapinwobhfufvtzgqznlqwzwdmztztxchnnbmqdpapxsyyjscseeevzinrmiittqpgkuvusayuldlfzdrjokwygavfvkmjljedflzkmvvhlwriwsavptnfqhqcxgdsnsbughdhkxjtzwnkzaioltvqfwayupkxzkmioxpgdlzsrkahteoptjyihxuzbmxyonxwnglfphosvgaytvrexeprlduttetlugjrhrmatssanekatiugnfluwvyuiqlndefpvhujgshmgltcamniqktfaajyekhmbzqishcebfovgjmvtuqjsakwoxganxckbflctlelanyxfoyvxpxrtbigiwbxaddqdfyehuntzzsavbvsynxiqgxuhpcjfplpbphfvkrqczzoaxebqxpbwxqiamxbruxskbodjivaoyrfnjaauxhqcylssaxcblrvvfhvyirsubmrtiqjxnulobfzumohiuxmuwbygeamnxirxwcfsjnxmnqcbkrkhclvfhzmphncjpefxnvhulztbemyvvpqaogkioyrxfxpanlkiitzxrrvfwjsluihbcujsarmufmiuxnzftrhpjfkwkgdqsshyhshaoerkefsfxzpmrdzxmlbvkjturdwxlrjdwrhfswtjwmctendxgwydktzbevgbecxoqgxofdyzmzmfcniantmcsjlohyltlykthfrcywwbnscrjasofwmdzxiejggfwrkbkygwnuzzgalysocrheemksgypnit"))
assert Solution().validPalindrome("aba") == True
assert Solution().validPalindrome("abca") == True  # You could delete the character 'c'

s = "sxigqizmbopbyluwxmehcqudofdjadhsteappejrnxyfoxobpdlpuhzkojxabyybmlsviemdjtptxoatpiztvebbbsmozxcomjyudelcmzmpadftmegvhudcivnpuondhapibzvtrlokydxswdihcmsoupfohwuyoamglrwptvixhgjhskjiyyymwciynhmdjtavvzrlxgqwmzkcpoainizfgacmixzmoakwwrslrsbfcapinwobhfufvtzgqznlqwzwdmztztxchnnbmqdpapxsyyjscseeevzinrmiittqpgkuvusayuldlfzdrjokwygavfvkmjljedflzkmvvhlwriwsavptnfqhqcxgdsnsbughdhkxjtzwnkzaioltvqfwayupkxzkmioxpgdlzsrkahteoptjyihxuzbmxyonxwnglfphosvgaytvrexeprlduttetlugjrhrmatssanekatiugnfluwvyuiqlndefpvhujgshmgltcamniqktfaajyekhmbzqishcebfovgjmvtuqjsakwoxganxckbflctlelanyxfoyvxpxrtbigiwbxaddqdfyehuntzzsavbvsynxiqgxuhpcjfplpbphfvkrqczzoaxebqxpbwxqiamxbruxskbodjivaoyrfnjaauxhqcylssaxcblrvvfhvyirsubmrtiqjxnulobfzumohiuxmuwbygeamnxirxwcfsjnxmnqcbkrkhclvfhzmphncjpefxnvhulztbemyvvpqaogkioyrxfxpanlkiitzxrrvfwjsluihbcujsarmufmiuxnzftrhpjfkwkgdqsshyhshaoerkefsfxzpmrdzxmlbvkjturdwxlrjdwrhfswtjwmctendxgwydktzbevgbecxoqgxofdyzmzmfcniantmcsjlohyltlykthfrcywwbnscrjasofwmdzxiejggfwrkbkygwnuzzgalysocrheemksgypnit"
