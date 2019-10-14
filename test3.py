# Tests for functions from the files:
# CONSEC3.py
# CONSEC_COMBIN3.py
# COUNT_CONSEC3.py

from CONSEC3 import count_inv_avoiding3
from CONSEC3 import find_inv_avoiding3
from CONSEC_COMBIN3 import count_and_inv_avoiding3
from CONSEC_COMBIN3 import find_and_inv_avoiding3
from CONSEC_COMBIN3 import count_or_inv_avoiding3
from CONSEC_COMBIN3 import find_or_inv_avoiding3
from CONSEC_COMBIN3 import count_but_inv_avoiding3
from CONSEC_COMBIN3 import find_but_inv_avoiding3
from CONSEC_COMBIN3 import count_exact_inv_avoiding3
from CONSEC_COMBIN3 import find_exact_inv_avoiding3
from COUNT_CONSEC3 import occur3
from COUNT_CONSEC3 import occur_list3
# Remark: The patterns are entered as strings. The possible strings are '000',
# '100', '110', '101', '010', '011', '001', '012', '201', '210', '120', '021'
# and '102'

# Count inversion sequences avoiding a pattern
# print count_inv_avoiding3(3, '102')

# Find inversion sequences avoiding a pattern
# print find_inv_avoiding3(3, '000')

# Count inversion sequences avoiding two patterns
# print count_and_inv_avoiding3(3, '000', '110')

# Find inversion sequences avoiding two patterns
# print find_and_inv_avoiding3(3, '000', '001')

# Count inversion sequences avoiding at least one of two patterns
# print count_or_inv_avoiding3(3, '000', '001')

# Find inversion sequences avoiding at least one of two patterns
# print find_or_inv_avoiding3(3, '000', '001')

# Count inversion sequences avoiding the 1st pattern, but not the 2nd
# print count_but_inv_avoiding3(3, '000', '001')

# Find inversion sequences avoiding the 1st pattern, but not the 2nd
# print find_but_inv_avoiding3(3, '100', '110')

# Count inversion sequences avoiding exactly one of two patterns
# print count_exact_inv_avoiding3(3, '000', '001')

# Find inversion sequences avoiding exactly one of two patterns
# print find_exact_inv_avoiding3(3, '000', '001')

# Count occurrences of a pattern among inversion sequences
# print occur3(4, '100')

# Find occurrences of a pattern among inversion sequences
# print occur_list3(3, '100')
