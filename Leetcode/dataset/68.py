class Solution:
    def add_blanket(self, word_num, word_length):
        
        if word_num == 1:
            return [self.w - word_length]
        blank_widths = []
        left_length = self.w - word_length
        for i in range(word_num - 1, 0, -1):
            length = int((left_length - 1e-5) // i + 1)
            blank_widths.append(length)
            left_length -= length
        return blank_widths

    def convert_line(self, word_list, blank_widths):
        
        if len(word_list) == 1: 
            return word_list[0] + blank_widths[0] * ' '
        str = ''
        for i, each in enumerate(word_list[:-1]):
            str += each + blank_widths[i] * ' '
        return str + word_list[-1]

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        self.w = maxWidth
        i = 0
        while i < len(words):   
            start_idx = i
            length = 0
            while length <= maxWidth + 1 and i < len(words): 
                length += len(words[i]) + 1
                i += 1
            if i == len(words) and length <= maxWidth + 1:  
                line = ' '.join(words[start_idx:])
                res.append(line + ' ' * (self.w - len(line)))
            else: 
                i -= 1
                length -= 2 + len(words[i])
                blank_widths = self.add_blanket(i - start_idx, len(''.join(words[start_idx:i])))
                res.append(self.convert_line(words[start_idx:i], blank_widths))
        return res