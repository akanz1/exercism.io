def find_anagrams(word, candidates):
    word_chars = {char.lower(): word.count(char) for char in set(word)}
    candidates = list(
        filter(lambda x: x.lower() != word.lower(), candidates)
    )  # eliminate occurences of "word" in "candidates"

    result = [
        candidate
        for candidate in candidates
        if {char.lower(): candidate.count(char) for char in set(candidate)}
        == word_chars
    ]
    return result
