class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        dictionary = {}
        seen = set()
        for x, word in enumerate(words):
            if pattern[x] not in dictionary:
                if word in seen:
                    return False
                seen.add(word)
                dictionary[pattern[x]] = word

            else:
                if dictionary[pattern[x]] != word:
                    return False

        return True
