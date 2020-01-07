import ctypes

# TODO  insert(index, item), delete(index), remove(item), find(item)


class DynamicArray:
    def __init__(self):
        self.length_of_array = 0
        self.initial_capacity = 3
        self.elements = self.make_array(self.initial_capacity)

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def size(self):
        return self.length_of_array

    def is_empty(self):
        return True if self.length_of_array == 0 else False

    def append(self, value):
        if len(self.elements) == self.length_of_array:
            self._resize()

        self.elements[self.length_of_array] = value
        self.length_of_array += 1

    def _resize(self):
        more_elements = self.make_array(self.length_of_array * 2)

        for i in range(self.length_of_array):
            more_elements[i] = self.elements[i]

        self.elements = more_elements

    def __getitem__(self, i):
        if not 0 <= i < self.length_of_array:
            raise IndexError("i is out of bounds")
        return self.elements[i]

    def pop(self):
        if self.length_of_array == 0:
            raise IndexError("cannot pop empty array")
        return self.elements[self.length_of_array - 1]
