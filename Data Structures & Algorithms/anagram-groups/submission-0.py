from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A defaultdict automatically creates an empty list for new keys
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word to use as the dictionary key
            # We use tuple() or join() because lists cannot be dictionary keys
            sorted_word = "".join(sorted(word))
            
            # Append the original word to the correct anagram group
            anagram_map[sorted_word].append(word)
            
        # Return just the grouped lists
        return list(anagram_map.values())