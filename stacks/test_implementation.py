from stacks.implementation import (SetOfStacks, Stack)

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


empty_stacks = SetOfStacks()
filled_stacks = SetOfStacks()
filled_stacks.push(1.0)
filled_stacks.push("here")
filled_stacks.push("there")
filled_stacks.push("where?")


def test_stacks_capacity():
    assert empty_stacks.capacity == 3

def test_size():
    assert empty_stacks.size() == 0
    assert filled_stacks.size() == 4

def test_index_of_stacks():
    assert empty_stacks.idx_of_stacks == 0
    assert filled_stacks.idx_of_stacks == 1

def test_pop_first_stack():
    assert filled_stacks.pop() == "where?"
    assert filled_stacks.idx_of_stacks == 1

def test_pop_second_stack():
    assert filled_stacks.pop() == "there"
    assert filled_stacks.idx_of_stacks == 0
