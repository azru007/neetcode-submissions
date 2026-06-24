class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for word in strs:
            ww = sorted(list(word))
            ide = "".join(ww)
            # return [[ide]]
            ana[ide].append(word)
            

        
        return list(ana.values())