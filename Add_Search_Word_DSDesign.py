'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.col = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if len(word) in self.col:
            self.col[len(word)].append(word)
        else:
            self.col[len(word)] = [word]

    def search(self, search_word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        count=0

        for a in search_word:
            if a.isalpha():
                count+=1

        if len(search_word) in self.col:
            X=self.col[len(search_word)]
            ans=0
            for word in X:
                temp=0
                for i in range(len(word)):
                    if  search_word[i]!="." and word[i]==search_word[i]:
                        temp+=1
                ans=max(temp,ans)
            if ans==count:
                return True
            return False

        return False