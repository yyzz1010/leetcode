class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        freq_dict = {}
        for x in A:
            if x not in freq_dict:
                freq_dict[x] = 1
            else:
                freq_dict[x] += 1
        
        for k,v in freq_dict.items():
            if v >= 2:
                ans = k
        return ans
