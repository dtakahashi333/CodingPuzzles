from random import randint


# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
class RandomizedSet:

    def __init__(self):
        self.items = {}

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        else:
            self.items[val] = val
            return True

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False
        else:
            del self.items[val]
            return True

    def getRandom(self) -> int:
        n = len(self.items)
        return list(self.items)[randint(0, n - 1)]
