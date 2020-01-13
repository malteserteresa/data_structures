class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

class SetOfStacks:

    def __init__(self):
        self.capacity = 3
        self.idx_of_stacks = 0
        self.stacks = [Stack()]

    def size(self):
        return self.stacks[self.idx_of_stacks].size() if self.idx_of_stacks == 0 else \
            (len(self.stacks) - 1) * 3 + self.stacks[-1].size()

    def push(self, item):
        if self.stacks[self.idx_of_stacks].size() == self.capacity:
            self.idx_of_stacks += 1
            self.stacks.append(Stack())
            self.stacks[self.idx_of_stacks].push(item)

        else:
            self.stacks[self.idx_of_stacks].push(item)

    def pop(self):
        if self.stacks[self.idx_of_stacks].size() == 0:
            self.idx_of_stacks -= 1

        return self.stacks[self.idx_of_stacks].pop()

