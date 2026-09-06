class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}

class PrefixTree:



    def __init__(self):
        self.root = TreeNode(None)
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = TreeNode(c)
                cur = cur.children[c]
        if "." not in cur.children:
            cur.children["."] = None


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return "." in cur.children

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        
        