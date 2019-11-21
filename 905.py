class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        odd = []
        for x in A:
            if x % 2 == 0:
                ans.append(x)
            else:
                odd.append(x)
        ans.extend(odd)
        return ans 
