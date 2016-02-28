_end = '_end_'
def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root 
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end  

    return root 



def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False 
    else:
        if _end in current_dict:
            return True
        else:
            return False


trie = make_trie('foo','bar','baz','barz')
print in_trie(trie, 'baz')


class TreeNode(object):
    def __init__(self):
        self.is_string = False 
        self.leaves = {}

class Trie(object):
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        cur = self.root 
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TreeNode()
            cur = cur.leaves[c]
        cur.is_string = True 


    def search(self, word):
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None 


    def childSearch(self, word):
        cur = self.root 
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None 
        return cur


trie = Trie() 
trie.insert("something")
print trie.search("something")
print trie.startsWith("som")