# Finding and counting inversion sequences avoiding
# consecutive patterns of length 3
# Uses the file consec_detect3.py and gen_inv_seq.py


import consec_detect3
import gen_inv_seq


# Counts the number of sequences in a collection that avoid
# a given pattern of length 3.
# Parameters: collection is a list of lists, pattern is a string.
# Returns the number of sequences avoiding the pattern, an integer.


def count_avoiding3(collection, pattern):
    counter = 0
    for sequence in collection:
        if not consec_detect3.detect_pattern3(sequence, pattern):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid a given pattern of length 3.
# Parameters: collection is a list of lists, pattern is a string.
# Returns the sequences avoiding the pattern, a list.


def find_avoiding3(collection, pattern):
    avoiding_seq = list()
    for sequence in collection:
        if not consec_detect3.detect_pattern3(sequence, pattern):
            avoiding_seq.append(sequence)
    return avoiding_seq

# Counts the number of inversion sequences of a given length
# that avoid a given pattern of length 3.
# Parameters: length is an integer, pattern is a string.
# Returns the number of inversion sequences of the given length
# that avoid the pattern, an integer.


def count_inv_avoiding3(length, pattern):
    return count_avoiding3(gen_inv_seq.inv_seq(length), pattern)

# Finds the inversion sequences of a given length that avoid
# a given pattern of length 3.
# Parameters: length is an integer, pattern is a string.
# Returns the inversion inversion sequences of the given length
# that avoid the pattern, a list.


def find_inv_avoiding3(length, pattern):
    return find_avoiding3(gen_inv_seq.inv_seq(length), pattern)
