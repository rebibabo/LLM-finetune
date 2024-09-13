class WordDictionary:
    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        root = self.tree
        for c in word[:-1]:
            if c not in root:
                root[c] = {}
            root = root[c]
        root.setdefault(word[-1], {})   
        root[word[-1]][0] = 0

    def search(self, word: str) -> bool:
        def help(root, word):
            if root == 0:   
                return False
            for i, c in enumerate(word):   
                if c in root:
                    root = root[c]  
                elif c == '.':  
                    for child in root.values():
                        if help(child, word[i+1:]):
                            return True
                    return False    
                else:
                    return False
            return 0 in root
        return help(self.tree, word)