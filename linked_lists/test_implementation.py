from linked_lists.implementation import (LinkedList, Node)

node = Node(3, Node(5, None))

def test_get_next_node():
    assert id(node) != id(node.next)
    assert node.next.next == None

def test_get_value():
    assert node.value == 3
    assert node.next.value == 5

empty = LinkedList()
filled = LinkedList()
filled.push_front(2)
filled.push_front(1)
filled.push_front(5)

def test_size():
    assert empty.size == 0

def test_is_empty():
    assert empty.is_empty() == True

def test_push_front():
    assert filled[0].value == 5
    assert filled[1].value == 1
    assert filled[2].value == 2
    assert filled.size == 3

def test_push_back():
    filled.push_back(10)
    assert filled[-1].value == 10
    filled.push_back(11)
    assert filled[-1].value == 11

def test_pop_front():
    assert filled.size == 5
    assert filled.pop_front() == 5
    assert filled.size == 4
    assert filled.pop_front() == 1

def test_pop_back():
    assert filled.size == 3
    assert filled.pop_back() == 11
    assert filled.size == 2

