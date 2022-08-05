from Anagrams1 import Anagrams


def test_should_list_same_word_as_anagram():
    anagram = Anagrams(["testword"])
    assert "testword" in anagram.list_anagrams("testword")


def test_should_reject_words_that_add_new_letters():
    anagrams = Anagrams(["testword", "test"])
    assert "testword" not in anagrams.list_anagrams("test")


def test_should_list_all_anagrams():
    anagrams = Anagrams(["abc", "bac"])
    assert "abs" and "bac" in anagrams.list_anagrams("cab")
