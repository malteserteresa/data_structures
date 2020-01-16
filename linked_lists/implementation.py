class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        return True if self.size == 0 else False

    def push_front(self, value):
        if self.size:
            self.head = Node(value, self.head)
            self.size += 1
        else:
            self.head = Node(value, None)
            self.size += 1

    def __getitem__(self, index):
        head = self.head
        i = 0
        index = (self.size + index) % self.size

        while i < index:
            head = head.next
            i += 1

        return head

    def pop_front(self):
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def pop_back(self):
        head = self.head
        while head.next != None:
            previous = head
            head = head.next

        previous.next = None
        self.size -= 1
        value = head.value
        return value

    def push_back(self, value):
        head = self.head
        if head:
            new_node = Node(value, None)
            while head.next != None:
                head = head.next
            head.next = new_node
            self.size += 1
        else:
            self.head = Node(value, None)
            self.size += 1
