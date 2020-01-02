sequences = [[1, 2, 3, 4], ("a", "a", "a"), "bbbbb"]

# Sequence type share same interface
def iterate(sequence):
    for i in sequence:
        print(i)

def test_iterate():
    for sequence in sequences:
        iterate(sequence)

# Return slice returns data structure data type
def first_and_last(sequence):
    return sequence[0] + sequence[-1]

def first_and_last_slice(sequence):
    return sequence[:1] + sequence[-1:]

def test_first_last():
    assert first_and_last(sequences[0]) == 5
    assert first_and_last_slice(sequences[0]) == [1, 4]

def modify(sequence):
    return sequence[:] == ["a"] * 20

def test_modify():
    # TODO  *= commands, manipulate list while iterate &
    #  swap elements -> what happens to their ids

    id_of_sequence = id(sequences[0])
    sequences[0][:] = list(range(5))
    assert id_of_sequence == id(sequences[0])


if __name__ == "__main__":
    test_iterate()
    test_first_last()
    test_modify()

