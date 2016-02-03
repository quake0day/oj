class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False] * w for x in range(h)]
        dz = zip([1,0,-1,0],[0,1,0,-1])
        ans = []

        def dfs(word, node, x, y):
            node = node.leaves.get(board[x][y])
            if node is None:
                return 
            visited[x][y] = True
            for z in dz:
                nx, ny = x + z[0] , y+z[1]
                if nx >= 0 and nx <h and ny >= 0 and ny < w and not visited[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.is_string:
                ans.append(word)
                trie.delete(word)
            visited[x][y] = False
        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)
        return sorted(ans)


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_string = False
        self.leaves = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root 
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True
    
    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.leaves.get(letter)
            if child is None:
                return False 
            node = child 
        if not node.is_string:
            return False 
        if len(node.leaves):
            node.is_string = False 
        else:
            for letter, node in reversed(queue):
                del node.leaves[letter]
                if len(node.leaves) or node.is_string:
                    break 
        return True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix) is not None
    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur


a = Solution()
#print a.findWords()
        