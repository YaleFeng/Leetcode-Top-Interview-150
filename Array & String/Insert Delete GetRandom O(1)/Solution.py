from typing import List

class RandomizedSet:

    def __init__(self):
        self.ran = set()

    def insert(self, val: int) -> bool:
        if val in self.ran:
            return False
        else:
            self.ran.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.ran:
            self.ran.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.ran))

