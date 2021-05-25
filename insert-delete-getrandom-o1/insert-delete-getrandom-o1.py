import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.out:
            self.out.append(val)
            return True
        else:
            return False
            

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.out:
            return False
        else:
            self.out.remove(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.out)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()