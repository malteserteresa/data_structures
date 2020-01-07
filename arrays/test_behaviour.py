from arrays.behaviour import (first_and_last, first_and_last_slice, iterate)


sequences = [[1, 2, 3, 4], ("a", "a", "a"), "bbbbb"]


def test_modify():
    # TODO  *= commands, manipulate list while iterate &
    #  swap elements -> what happens to their ids

    id_of_sequence = id(sequences[0])
    sequences[0][:] = list(range(5))
    assert id_of_sequence == id(sequences[0])


def test_iterate():
    for sequence in sequences:
        iterate(sequence)


def test_first_last():
    assert first_and_last(sequences[0]) == 5
    assert first_and_last_slice(sequences[0]) == [1, 4]
