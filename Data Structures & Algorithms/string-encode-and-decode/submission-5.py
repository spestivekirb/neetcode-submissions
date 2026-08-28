class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        word = ""
        decoded = []
        i = 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            i += 1

            for j in range(int(count)):
                word += s[i]
                i += 1
            
            decoded.append(word)
            word = ""

        return decoded