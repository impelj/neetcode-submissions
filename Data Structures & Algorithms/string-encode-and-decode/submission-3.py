class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        st = '||'.join(strs)
        return st
    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return []
        
        st = s.split('||')
        return st