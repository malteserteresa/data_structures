from linked_lists.implementation import LinkedList
from linked_lists.implementation import Node

# TODO edge cases, empty list, huge list, combine classes

node = Node(3, Node(5, None))


def test_get_next_node():
    assert id(node) != id(node.next)
    assert node.next.next == None


def test_get_value():
    assert node.value == 3
    assert node.next.value == 5


def test_push_front():
    ll = LinkedList()
    size = 3
    n = 3
    for _ in range(size):
        ll.push_front(n)
        n += 3

    assert ll.size == size
    assert ll[0].value == size * 3
    assert ll[1].value == (size - 1) * 3
    assert ll[2].value == (size - 2) * 3


def test_push_back():
    ll = LinkedList()
    size = 3
    n = 5

    for _ in range(size):
        ll.push_back(n)
        n += 5

    assert ll.size == size
    assert ll[-1].value == size * 5
    assert ll[-2].value == (size - 1) * 5
    assert ll[-3].value == (size - 2) * 5


def test_pop_front():
    ll = create_linked_list()

    assert ll.size == 4
    assert ll.pop_front() == 1
    assert ll.pop_front() == 2
    assert ll.pop_front() == 3
    assert ll.pop_front() == 4
    assert ll.size == 0


def create_linked_list():
    ll = LinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    return ll


def test_pop_back():
    ll = create_linked_list()

    assert ll.size == 4
    assert ll.pop_back() == 4
    assert ll.pop_back() == 3
    assert ll.pop_back() == 2
    assert ll.size == 1
