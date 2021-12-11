import collections

class FrontMiddleBackQueue:

    def __init__(self):
        self.first = collections.deque()
        self.second = collections.deque()

    def pushFront(self, val: int) -> None:
        self.first.appendleft(val)
        if len(self.first) > len(self.second) +1:
            self.second.appendleft(self.first.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.first) > len(self.second):
            self.second.appendleft(self.first.pop())
        self.first.append(val)

    def pushBack(self, val: int) -> None:
        self.second.append(val)
        if len(self.first) < len(self.second):
            self.first.append(self.second.popleft())

    def popFront(self) -> int:
        if not self.first and not self.second: return -1
        result = self.first.popleft()
        if len(self.first) < len(self.second):
            self.first.append(self.second.popleft())
        return result

    def popMiddle(self) -> int:
        if not self.first and not self.second: return -1
        result = self.first.pop()
        if len(self.first) < len(self.second):
            self.first.append(self.second.popleft())
        return result

    def popBack(self) -> int:
        if not self.first and not self.second: return -1
        if not self.second: return self.first.pop()
        result = self.second.pop()
        if len(self.first) > len(self.second) + 1:
            self.second.appendleft(self.first.pop())
        return result
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()