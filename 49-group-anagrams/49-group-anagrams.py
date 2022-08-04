class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagram_map = {}
        for each_string in strs:
            word = ''.join(sorted(each_string))
            if word in Anagram_map:
                Anagram_map[word].append(each_string)
            else:
                Anagram_map[word] = [each_string]
        
        return Anagram_map.values()