class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            word = "".join(sorted(i))
            if word in result:
                result[word].append(i)
            else:
                result[word] = [i]
        return list(result.values())


        