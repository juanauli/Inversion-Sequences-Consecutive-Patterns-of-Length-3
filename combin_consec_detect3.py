# Detection of combinations of consecutive patterns of length 3
# Uses the file consec_detect3.py


import consec_detect3

# Determines whether two patterns of length 3 (BOTH) occurs in a sequence.
# Parameters: sequence is a list, pattern1 and pattern2 are strings.
# Returns True if both patterns are found and False otherwise.


def detect_and_pattern3(sequence, pattern1, pattern2):
    return consec_detect3.detect_pattern3(sequence, pattern1) and\
        consec_detect3.detect_pattern3(sequence, pattern2)

# Determines if at least one of two patterns of length 3 occurs in a sequence.
# Parameters: sequence is a list, pattern1 and pattern2 are strings.
# Returns True if at least one pattern is found and False otherwise.


def detect_or_pattern3(sequence, pattern1, pattern2):
    return consec_detect3.detect_pattern3(sequence, pattern1) or\
        consec_detect3.detect_pattern3(sequence, pattern2)

# Determines if pattern1 occurs and pattern2 does not (length 3).
# Parameters: sequence is a list, pattern1 and pattern2 are strings.
# Returns True if pattern1 is found and pattern2 is not, and False otherwise.


def detect_but_pattern3(sequence, pattern1, pattern2):
    return consec_detect3.detect_pattern3(sequence, pattern1) and\
        not consec_detect3.detect_pattern3(sequence, pattern2)

# Determines if exactly one pattern occurs (length 3).
# Parameters: sequence is a list, pattern1 and pattern2 are strings.
# Returns True if pattern1 is found and pattern2 is not, and False otherwise.


def detect_exact_pattern3(sequence, pattern1, pattern2):
    return detect_but_pattern3(sequence, pattern1, pattern2) or\
        detect_but_pattern3(sequence, pattern2, pattern1)
