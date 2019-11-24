class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        line2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        line3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        line_list = []
        for x in words:
            x = x.lower()
            text = list(x)
            list_item = ''
            for y in text:
                if y in line1:
                    list_item += '1'
                elif y in line2:
                    list_item += '2'
                elif y in line3:
                    list_item += '3'
            item_length = len(set(list_item))
            line_list.append(item_length)
        
        index_list = [i for i, e in enumerate(line_list) if e == 1]
        return [words[index] for index in index_list]
