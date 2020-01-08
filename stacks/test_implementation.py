from stacks.implementation import Stack

empty_stack = Stack()
filled_stack = Stack()
filled_stack.push(1.0)
filled_stack.push("here")
filled_stack.push("there")

def test_size():
    assert empty_stack.size() == 0
    assert filled_stack.size() == 3

def test_pop():
    assert filled_stack.pop() == "there"
    assert filled_stack.pop() == "here"
