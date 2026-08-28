class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i]))
            encoded += "#"
            encoded += strs[i]
        return encoded

    

    def decode(self, s: str) -> List[str]:

        decoded = []
        cur = 0
        while cur < len(s):
            strlength = ""
            while s[cur] != "#":
                strlength += s[cur]
                cur += 1
            length = int(strlength)
            word = ""
            for i in range(length):
                cur += 1
                word += s[cur]
            cur += 1
            decoded.append(word)


        

        return decoded
