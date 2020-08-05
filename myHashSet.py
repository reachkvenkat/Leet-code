'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
'''


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()
        

    def add(self, key: int) -> None:
        # add key to the Hash Set
        self.hash.add(key)        

    def remove(self, key: int) -> None:
        # Removes the key if the key is present or does nothing
        if key in self.hash:
            self.hash.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hash:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    # returns true
print(hashSet.contains(3))    # returns false (not found)
hashSet.add(2)
print(hashSet.contains(2))    # returns true
hashSet.remove(2)
print(hashSet.contains(2))    # returns false (already removed)