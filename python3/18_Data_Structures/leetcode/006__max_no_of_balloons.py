#!/usr/bin/python
"""
Purpose:
https://leetcode.com/problems/maximum-number-of-balloons/submissions/
Given a string text, you want to use the characters of text to form as many instances of the word 
"balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can 
be formed.
"""
from pprint import pprint


class Solution:
    # FAILED LOGIC
    # def maxNumberOfBalloons(self, text): 
    #     balloon_chars = {}
    #     for ech_chr in text:
    #         if ech_chr in 'balloon':
    #             balloon_chars[ech_chr] = balloon_chars.get(ech_chr, 0) + 1
    #     print(balloon_chars)
    #     # balloon: b-1, a-1, l-2, o-2, n-1

    # FAILED LOGIC
    # def maxNumberOfBalloons(self, text):
    #     print(text, '\n')
    #     for ech in set(text):
    #         if ech not in 'balloon':
    #             text = text.replace(ech, '')
    #     print(text, '\n')
    #     words = {}
    #     for search_chr in 'balloon':
    #         if search_chr not in text:
    #             return 0
    #         else:
    #             for i in range(text.count(search_chr)):
    #                 if not words.get(i):
    #                     words[i] = ''
    #                 words[i] += search_chr
    #             text = text.replace(search_chr, '', 1)
    #     print(text)
    #     pprint(words)
    #     return tuple(words.values()).count('balloon')

    def maxNumberOfBalloons(self, text):
        words_counts = []
        for search_chr in 'balloon':
            chr_count = text.count(search_chr)
            if search_chr in ('l', 'o'):
                chr_count //= 2
            words_counts.append(chr_count)
        return min(words_counts)

    def maxNumberOfBalloons(self, text):
        word = "balloon"
        char_count = {}
        for c in text:
            if c in word:
                if c not in char_count:
                    char_count[c] = 1
                else:
                    char_count[c] += 1
        nl = []
        nl.append(char_count.get('b', 0))
        nl.append(char_count.get('a', 0))
        nl.append(char_count.get('l', 0) // 2)
        nl.append(char_count.get('o', 0) // 2)
        nl.append(char_count.get('n', 0))

        return min(nl)


print(Solution().maxNumberOfBalloons(
    "siobnxjnmhnzoxjztwoezeqgoqkhetrpwszmwwwfpyybcizuzhrxriynbyjpbeplhfavddkwspyoddheetjgfqsmywnmxjviftexuzdbpuexfhsmyagqefhdilhehlhkitmkijgzoogicywcfxzalrvayrxavieoqodwoasbxuuuormvktvhwlidiilotsfwgcztxjktibraglhnhneororppplsylbfkebmqbzvftzsrrwfoiifajmxkjxtaxmvfmgxkdbxdycgottuymuknrnhjjcpwkpmbweirromdikbtcptxgtkslozeoejpchphkydsjexwjkiquaahuphtqftzoayqyqevtwszfmmkjqoqxexexltnwxpisszxdxljfubboxalbxhmnuabbypkpmrxyecuibqjoixdbjfvinxcgnjtwpyhieqneerorbllszkavoxearikldjeomdzyotdxioprkkvisadoccdrhkdknoyzmldomfdytzuvwvwoqatojlczydkvyfifkygtmwjynrtvllunelpkargfrkltadhzhggdmdtzordxrlxegknsqwmyqmpndpjtiwoutoxvgmxomhcjursxqzsoipvecltqjgurzhgsahpgrvshqddlqivbfiwcvrxpmneuwmpepyswrktflewfgfbtghjcvzfomsbozadzxzkmyzjsroftglrpmxzjnyekkiplfmuzkabmvdwurhuwnywqlxfzjzgsfsshbmszxxnxbotgryafvsyksaxvcxqbveuvqmutauqtcrqwnczzhrhgsjbxhnrpgxauqxtaouasklqxhndpsvrfcigpkjqgwyisaqzzcviqibbuzljshpbwgfgkjdcbsygptdebhyrdkmnibhedccpkoyfbgjbokdrxocfavwrqxrdrzfarhidwxcvtiqlmkecrhmvrbswyqsllxieztqppouuvxjuglyajhvypjtwegokegkmeh"))

assert Solution().maxNumberOfBalloons("nlaebolko") == 1
assert Solution().maxNumberOfBalloons("loonbalxballpoon") == 2
assert Solution().maxNumberOfBalloons("leetcode") == 0
assert Solution().maxNumberOfBalloons("balon") == 0
assert Solution().maxNumberOfBalloons("ballon") == 0
assert Solution().maxNumberOfBalloons("baloon") == 0
assert Solution().maxNumberOfBalloons(
    "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw") == 10
