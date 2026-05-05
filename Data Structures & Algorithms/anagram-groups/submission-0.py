class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Initialize the dictionary
        res = {}

        for s in strs:
            # 2. Sort the string to create a consistent key
            # sorted("eat") -> ["a", "e", "t"] -> join it to "aet"
            sorted_s = "".join(sorted(s))
            
            # 3. If this key isn't in res, add it with an empty list
            if sorted_s not in res:
                res[sorted_s] = []
            
            # 4. Append the original string to the correct group
            res[sorted_s].append(s)

        # 5. Return all the groups as a list of lists
        # Use a dot (.) to call the method values()
        return list(res.values())