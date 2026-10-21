class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def add(self, word):

        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()

            cur = cur.children[i]

        cur.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for i in words:
            root.add(i)

        ROWS = len(board)
        COLS= len(board[0])

        res = set()

        visit = set()


        def dfs(r,c, node, word):

            if (r < 0 or c < 0 or r >= ROWS or c>= COLS or (r,c) in visit or board[r][c] not in node.children):
                return

            visit.add((r,c))
            node=node.children[board[r][c]] # here i am unsure my frined ATACKKAKCKCAKC
            word += board[r][c]


            if node.end_of_word:
                res.add(word)


            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))

        for r in range((ROWS)):
            for c in range((COLS)):
                dfs(r,c,root,"")

        return list(res)




        