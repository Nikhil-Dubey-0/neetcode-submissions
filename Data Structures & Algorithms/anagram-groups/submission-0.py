class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map={}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in h_map:
                h_map[sorted_word].append(word)
                continue
            else:
                h_map[sorted_word]= [word]
                # data.setdefault(sorted_word, []).append(word)
        return list(h_map.values())