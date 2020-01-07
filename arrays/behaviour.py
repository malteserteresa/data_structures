# Sequence type share same interface
def iterate(sequence):
    for i in sequence:
        print(i)


# Return slice returns data structure data type
def first_and_last(sequence):
    return sequence[0] + sequence[-1]


def first_and_last_slice(sequence):
    return sequence[:1] + sequence[-1:]


def modify(sequence):
    return sequence[:] == ["a"] * 20
