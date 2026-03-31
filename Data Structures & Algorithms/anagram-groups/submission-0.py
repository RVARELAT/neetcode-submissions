class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams by mapping each string to a 26-length frequency signature.
        Time:  O(m * n)  where m = number of strings, n = max length of a string
        Space: O(m)      for the hashmap entries (ignoring the output lists)
        """
        buckets = defaultdict(list)  # key: 26-tuple counts, value: list of anagrams

        for s in strs:
            # 26 letters in the alphabet
            # # Build frequency of 'a'..'z' in O(len(s))
            counts = [0] * 26
            for ch in s:
                # ex: 'a' - 'a' gives us 0, so counts[0] += 1
                counts[ord(ch) - ord('a')] += 1

            key = tuple(counts)  # lists are unhashable; tuple makes it a valid dict key
            buckets[key].append(s) # group the current string under its signature

        # We only need the grouped lists. Order of groups and order within groups doesn't matter.
        return list(buckets.values())

# Word:  act → key: (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# Word:  cat → key: (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
# Word:  hat → key: (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)


        