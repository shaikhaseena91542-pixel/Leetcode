from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        if s_len < total_len:
            return []

        word_count = Counter(words)
        result = []

        # Try each possible starting offset within the first word_len characters
        for offset in range(word_len):
            left = offset
            count = 0
            window_counts = Counter()

            for right in range(offset, s_len - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    window_counts[word] += 1
                    count += 1

                    # If a word appears too many times, shrink from the left
                    while window_counts[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_counts[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Found a valid concatenation
                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        window_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # Word not in words list — reset window
                    window_counts.clear()
                    count = 0
                    left = right + word_len

        return result