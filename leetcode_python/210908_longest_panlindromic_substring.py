# https://leetcode.com/problems/longest-palindromic-substring/

#%%
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        list_palindromes = []
        for i, _ in enumerate(s):
            substring = s[i:]
            for j, _ in enumerate(substring):
                if j == 0:
                    substring_2 = substring
                else:
                    substring_2 = substring[:-j]

                if is_palindrome(substring_2):
                    list_palindromes.append(substring_2) 
                    break
        
        list_len_palindrome = [len(x) for x in list_palindromes]
        max_size_palindrome = max(list_len_palindrome)
        idx = list_len_palindrome.index(max_size_palindrome)
        the_longest_palindrome = list_palindromes[idx]
        print(list_palindromes)
        return the_longest_palindrome


#%%
is_palindrome("bab")
is_palindrome("dassad")
is_palindrome("dassa")
#%%
s = "babad"
solution = Solution()
solution.longestPalindrome(s) in ["bab", "aba"]

#%%
s = "cbbd"
solution = Solution()
solution.longestPalindrome(s) in ["bb"]

#%%
s = "a"
solution = Solution()
solution.longestPalindrome(s) in ["a"]

#%%
s = "ac"
solution = Solution()
solution.longestPalindrome(s) in ["a", "c"]

# %%
s = "vnjwvalrbypfcbqnmopltjnoifmzwgvpzqzsdtvawndpjtpmpjbjionjifqtvvocpeaftvhpdgjjfafunfndztdjkcxyihtsyppendfzzjeyxlbwpdygiqmdqcdbmgyjigrmfkswcwryaydjilqqxvcnyvviesuncslvzikawwqykqwdfibggezufqihcjkebapmgkvwixywgdextafxycnipjglsndkyjoqfyfljfkkvoieksmavdlmlhhnstesibffiopqvlyuidvrawndbzonwzbsjmpeqoglmdbinkovqpzfkxihzitdopnomseqhmrrkcsvrzziphwpuhjngeotwcrebcmbtirkgeavojtmpakcewmexhxacngknokxsvtqobdgckutpexswgwqzbosjpxauyflnylfcxsucsehqvakbpvfmkelmkspsqxnutwfwacpqqvovdqafeylobneojdsgqowcbxfsvuqusdbylcgcvgrofgvzubakjmlbffjhrafvnqttwuyhokzpmhlludpbowuxzrebxsdusalljfjgjkucwzpmndqncykvfnbrxcrcaxwisjpstejjqbpwegpxyrtyafxklgralnkwxkmjpuqfixzkonznmguyizlancpxdzcfkgiotyelegprbaytdhbutbuihkxnbtuqrtezaskfqsmrznfohhlqp"
solution = Solution()
solution.longestPalindrome(s)

# %%
