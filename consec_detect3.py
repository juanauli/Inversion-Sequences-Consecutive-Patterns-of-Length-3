# Detection of consecutive patterns of length 3

# Detects the pattern 000.


def detect000(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 100.


def detect100(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 110.


def detect110(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 101.


def detect101(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 2] > sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 010.


def detect010(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 2] < sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 011.


def detect011(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] == sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 001.


def detect001(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] == sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 012.


def detect012(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 1] < sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 201.


def detect201(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 2] > sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 210.


def detect210(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] > sequence[index + 1] > sequence[index + 2]:
            return True
        index += 1
    return False

# Detects the pattern 120.


def detect120(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index + 2] < sequence[index] < sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 021.


def detect021(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index] < sequence[index + 2] < sequence[index + 1]:
            return True
        index += 1
    return False

# Detects the pattern 102.


def detect102(sequence):
    index = 0
    while index < len(sequence) - 2:
        if sequence[index + 1] < sequence[index] < sequence[index + 2]:
            return True
        index += 1
    return False

# Determines whether a pattern of length 3 occurs in a sequence.
# Parameters: sequence is a list, pattern is a string.
# Returns True if the pattern is found and False otherwise.


def detect_pattern3(sequence, pattern):
    if pattern == '000':
        return detect000(sequence)
    elif pattern == '100':
        return detect100(sequence)
    elif pattern == '110':
        return detect110(sequence)
    elif pattern == '101':
        return detect101(sequence)
    elif pattern == '010':
        return detect010(sequence)
    elif pattern == '011':
        return detect011(sequence)
    elif pattern == '001':
        return detect001(sequence)
    elif pattern == '012':
        return detect012(sequence)
    elif pattern == '201':
        return detect201(sequence)
    elif pattern == '210':
        return detect210(sequence)
    elif pattern == '120':
        return detect120(sequence)
    elif pattern == '021':
        return detect021(sequence)
    elif pattern == '102':
        return detect102(sequence)
