class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        new_list = [x[::-1] for x in A]
        invert_dict = {0:1, 1:0}
        for y in new_list:
            for z in range(len(y)):
                y[z] = invert_dict.get(y[z], y[z])
        return new_list
