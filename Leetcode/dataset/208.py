class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        root = self.tree
        for c in word[:-1]:
            if c not in root:
                root[c] = {}
            root = root[c]
        root.setdefault(word[-1], {})   
        root[word[-1]][0] = 0

    def search(self, word: str) -> bool:
        root = self.tree
        for c in word:
            if c in root:
                root = root[c]
            else:
                return False
        return 0 in root    

    def startsWith(self, prefix: str) -> bool:
        root = self.tree
        for c in prefix:
            if c in root:
                root = root[c]
            else:
                return False
        return True