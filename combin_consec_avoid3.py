# Avoidance of combinations of consecutive patterns of length 3
# Uses the file combin_consec_detect3.py


import combin_consec_detect3

# Counts the number of sequences in a collection that avoid
# two given patterns of length 3.
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the number of sequences avoiding the patterns, an integer.


def count_and_avoiding3(collection, pattern1, pattern2):
    counter = 0
    for sequence in collection:
        if not combin_consec_detect3.detect_or_pattern3(sequence,
                                                        pattern1, pattern2):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid
# two given patterns of length 3.
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the sequences avoiding the patterns, a list.


def find_and_avoiding3(collection, pattern1, pattern2):
    avoiding_seq = list()
    for sequence in collection:
        if not combin_consec_detect3.detect_or_pattern3(sequence,
                                                        pattern1, pattern2):
            avoiding_seq.append(sequence)
    return avoiding_seq

# Counts the number of sequences in a collection that avoid
# at least one of two given patterns of length 3.
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the number of sequences avoiding at least one pattern, an integer.


def count_or_avoiding3(collection, pattern1, pattern2):
    counter = 0
    for sequence in collection:
        if not combin_consec_detect3.detect_and_pattern3(sequence,
                                                         pattern1, pattern2):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid at least one of two
# given patterns of length 3.
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the sequences avoiding at least one pattern, a list.


def find_or_avoiding3(collection, pattern1, pattern2):
    avoiding_seq = list()
    for sequence in collection:
        if not combin_consec_detect3.detect_and_pattern3(sequence,
                                                         pattern1, pattern2):
            avoiding_seq.append(sequence)
    return avoiding_seq

# Counts the number of sequences in a collection that avoid pattern1, but
# not pattern 2 (length 3).
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the number of sequences avoiding pattern1,
# but not patter2, an integer.


def count_but_avoiding3(collection, pattern1, pattern2):
    counter = 0
    for sequence in collection:
        if combin_consec_detect3.detect_but_pattern3(sequence,
                                                     pattern2, pattern1):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid pattern1, but
# not pattern 2 (length 3).
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the sequences avoiding pattern1, but not patter2, a list.


def find_but_avoiding3(collection, pattern1, pattern2):
    avoiding_seq = list()
    for sequence in collection:
        if combin_consec_detect3.detect_but_pattern3(sequence,
                                                     pattern2, pattern1):
            avoiding_seq.append(sequence)
    return avoiding_seq

# Counts the number of sequences in a collection that avoid exactly one
# of two given patterns(length 3).
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the number of sequences avoiding exactly one of the two
# patterns, an integer.


def count_exact_avoiding3(collection, pattern1, pattern2):
    counter = 0
    for sequence in collection:
        if combin_consec_detect3.detect_exact_pattern3(sequence,
                                                       pattern1, pattern2):
            counter += 1
    return counter

# Finds the sequences in a collection that avoid exactly one
# of two given patterns(length 3).
# Parameters: collection is a list of lists, pattern1 and pattern2 are strings.
# Returns the sequences avoiding exactly one of the two patterns, a list.


def find_exact_avoiding3(collection, pattern1, pattern2):
    avoiding_seq = list()
    for sequence in collection:
        if combin_consec_detect3.detect_exact_pattern3(sequence,
                                                       pattern1, pattern2):
            avoiding_seq.append(sequence)
    return avoiding_seq
