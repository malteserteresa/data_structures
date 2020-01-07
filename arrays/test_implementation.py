import pytest

from arrays.implementation import DynamicArray

empty = DynamicArray()

multiple_elements = DynamicArray()
multiple_elements.append(1.0)
multiple_elements.append("here")
multiple_elements.append("there")
multiple_elements.append("where?")


def test_capacity():
    assert empty.initial_capacity == 3
    assert multiple_elements.initial_capacity == 3


def test_size():
    assert empty.size() == 0
    assert multiple_elements.size() == 4


def test_is_empty():
    assert empty.is_empty() == True
    assert multiple_elements.is_empty() == False


def test_add():
    assert multiple_elements.size() == 4


def test_getitems():
    assert multiple_elements[0] == 1.0
    assert multiple_elements[1] == "here"
    assert multiple_elements[2] == "there"
    assert multiple_elements[3] == "where?"

    with pytest.raises(IndexError) as ie:
        multiple_elements[5]
    assert ie.value.args[0] == "i is out of bounds"


def test_pop():
    with pytest.raises(IndexError) as ie:
        empty.pop()
    assert ie.value.args[0] == "cannot pop empty array"

    assert multiple_elements.pop() == "where?"
