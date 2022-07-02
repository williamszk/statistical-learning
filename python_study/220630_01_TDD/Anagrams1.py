class Anagrams:
    def __init__(self, word_list) -> None:
        self.word_list = word_list

    def list_anagrams(self, word):
        words = []
        for anagram in self.word_list:
            if self._is_anagram(anagram, word):
                word.append(anagram)

        self._display_results(words, word)
        return words
    

