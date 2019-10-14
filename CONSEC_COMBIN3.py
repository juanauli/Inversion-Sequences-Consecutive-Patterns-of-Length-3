# Finding and counting inversion sequences avoiding combinations of
# consecutive patterns of length 3
# Uses the file combin_consec_avoid3.py and gen_inv_seq.py


import combin_consec_avoid3
import gen_inv_seq

# Counts the number of inversion sequences of a given length
# that avoid two patterns of length 3.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the number of inversion sequences of the given length
# that avoid both patterns, an integer.


def count_and_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.count_and_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Finds the inversion sequences of a given length
# that avoid two patterns of length 3.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the inversion sequences of the given length
# that avoid both patterns, a list.


def find_and_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.find_and_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Counts the number of inversion sequences of a given length
# that avoid at least one of two patterns of length 3.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the number of inversion sequences of the given length
# that avoid at least one of the patterns, an integer.


def count_or_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.count_or_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Finds the inversion sequences of a given length
# that avoid at least one of two patterns of length 3.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the inversion sequences of the given length
# that avoid at least one of the patterns, a list.


def find_or_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.find_or_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Counts the number of inversion sequences of a given length that
# avoid pattern1, but not pattern2 (length 3).
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the number of inversion sequences of the given length
# that avoid pattern1, but not pattern2, an integer.


def count_but_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.count_but_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Finds the inversion sequences of a given length that
# avoid pattern1, but not pattern2 (length 3).
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the inversion sequences of the given length
# that avoid pattern1, but not pattern2, a list.


def find_but_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.find_but_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Counts the number of inversion sequences of a given length that
# avoid exactly one of two given patterns.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the number of inversion sequences of the given length
# that avoid exactly one of the patterns, an integer.


def count_exact_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.count_exact_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)

# Finds the of inversion sequences of a given length that
# avoid exactly one of two given patterns.
# Parameters: length is an integer, pattern1 and pattern2 are strings.
# Returns the inversion sequences of the given length
# that avoid exactly one of the patterns, a list.


def find_exact_inv_avoiding3(length, pattern1, pattern2):
    return combin_consec_avoid3.find_exact_avoiding3(
        gen_inv_seq.inv_seq(length), pattern1, pattern2)
