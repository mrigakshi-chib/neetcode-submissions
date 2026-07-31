class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force
        '''
        if "".join(sorted(s))=="".join(sorted(t)) :
            return True
        return False
        '''
        #optimised - TC: O(n), SC : O(1)
        
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0) + 1
            hash_t[t[i]] = hash_t.get(t[i],0) + 1
        if hash_s == hash_t:
            return True
        return False
        


                

        