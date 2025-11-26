# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        # sorted letters of the original word
        sorted_word = sorted(self.word)

        matches = []
        for candidate in candidates:
            # avoid matching the exact same word (case-insensitive)
            if candidate.lower() == self.word:
                continue

            # check if sorted letters match
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches
