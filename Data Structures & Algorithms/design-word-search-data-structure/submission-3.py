class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode(None)
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode(c)

            cur = cur.children[c]
        
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        def searchFrom(cur, i):
            if i >= len(word):
                return cur.isWord
            elif word[i] == ".":
                for child in cur.children.values():
                    if searchFrom(child, i+1):
                        return True
                return False
            elif word[i] in cur.children:
                return searchFrom(cur.children[word[i]], i+1)
            else:
                return False
            
        return searchFrom(self.root, 0)

