
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        holder = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key in holder:
                holder[key].append(words)
            else: 
                holder[key] = [words]
        return list(holder.values())
            

        
        