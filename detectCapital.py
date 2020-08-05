'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # variable to count the number of Capital letters in the string
        count = 0

        # Iterating over the word to count number of capital letters
        for char in word:
            if ord(char) < 91:
                count += 1
        if count == len(word) or count == 0:
            return True

        if count == 1 and ord(word[0]) < 91:
            return True


        return False

def TestFunction(word, desired):
    soln = Solution()

    if soln.detectCapitalUse(word) == desired:
        print("Test case passed")
    else:
        print("Test case failed")

TestFunction("USA", True)
TestFunction("Name", True)
TestFunction("leetcode", True)
TestFunction("g", True)
TestFunction("FlaG", False)
TestFunction("mYNaMe", False)


