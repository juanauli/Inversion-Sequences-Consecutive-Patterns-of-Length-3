# Count occurrences of consecutive patterns

# Counts occurrences of the pattern 000


def count000(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 100.


def count100(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 110.


def count110(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 101.


def count101(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 2] > sequence[index + 1]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 010.


def count010(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 2] < sequence[index + 1]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 011.


def count011(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] == sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 001.


def count001(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 012.


def count012(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 201.


def count201(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 2] > sequence[index + 1]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 210.


def count210(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] > sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 120.


def count120(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index + 2] < sequence[index] < sequence[index + 1]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 021.


def count021(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 2] < sequence[index + 1]:
            counter += 1
        index += 1
    return counter

# Counts occurrences of the pattern 102.


def count102(sequence):
    index = 0
    counter = 0
    while index < len(sequence) - 2:
        if sequence[index + 1] < sequence[index] < sequence[index + 2]:
            counter += 1
        index += 1
    return counter

# Counts the occurrences of a pattern of length 3 in a sequence.
# Parameters: sequence is a list, pattern is a string.
# Returns the number of times the pattern occurs, an integer.


def count_pattern3(sequence, pattern):
    if pattern == '000':
        return count000(sequence)
    elif pattern == '100':
        return count100(sequence)
    elif pattern == '110':
        return count110(sequence)
    elif pattern == '101':
        return count101(sequence)
    elif pattern == '010':
        return count010(sequence)
    elif pattern == '011':
        return count011(sequence)
    elif pattern == '001':
        return count001(sequence)
    elif pattern == '012':
        return count012(sequence)
    elif pattern == '201':
        return count201(sequence)
    elif pattern == '210':
        return count210(sequence)
    elif pattern == '120':
        return count120(sequence)
    elif pattern == '021':
        return count021(sequence)
    elif pattern == '102':
        return count102(sequence)
