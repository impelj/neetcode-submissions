class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for word in strs:
            encoded_str.append(str(len(word)))
            encoded_str.append('#')
            encoded_str.append(word)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            i = j + 1 + length
        return decoded

