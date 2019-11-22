class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}
        for x in arr:
            if x not in freq_dict:
                freq_dict[x] = 1
            else:
                freq_dict[x] += 1
                
        value_list = list(freq_dict.values())
        unique_value_list = set(value_list)

        if len(value_list) == len(unique_value_list):
            return bool(1)
        else:
            return bool(0)
