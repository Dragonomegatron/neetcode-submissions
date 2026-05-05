class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: [length] + [#] + [string]
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next encoded block
            i = j + 1 + length
            
        return res