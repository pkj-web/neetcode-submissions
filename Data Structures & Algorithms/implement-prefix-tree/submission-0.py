
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class PrefixTree:

    def __init__(self):

        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        cur = self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()

            cur = cur.children[i]

        cur.end_of_word = True


    def search(self, word: str) -> bool:

        cur = self.root

        for i in word:
            if i not in cur.children:
                return False

            cur = cur.children[i]

        return cur.end_of_word
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        # seems hard to not pre-fire here
        for i in prefix:
            if i not in cur.children:
                return False

            cur = cur.children[i]

        return True


        
        