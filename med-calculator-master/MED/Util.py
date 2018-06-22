'''
    Costants and Utility Function used by Cell and Matrix
'''

from sys import version_info

# Flag Constants
BTFLAG_UP = 1       # Backtrace Up Flag
BTFLAG_LEFT = 2     # Backtrace Left Flag
BTFLAG_DIAG = 4     # Backtrace Diagonal Flag

# unicode characters - need Python 3!
if version_info.major == 3:
    BTMATRIX_SYMBOLS = [
        " ",                   # 0 - No flags were set
        "\u2191",              # 1 - Up flag set
        "\u2190",              # 2 - Left flag set
        "\u2190\u2191",        # 3 - Up flag and Left flag set
        "\u2196",              # 4 - Diagonal flag set
        "\u2196\u2191",        # 5 - Diagonal flag and Up flag set
        "\u2196\u2190",        # 6 - Diagonal flag and Left flag set
        "\u2196\u2190\u2191",  # 7 - All flags are set
    ]
else:
    BTMATRIX_SYMBOLS = [
        " ",                   # 0 - No flags were set
        "U",                   # 1 - Up flag set
        "L",                   # 2 - Left flag set
        "U",                   # 3 - Up flag and Left flag set
        "G",                   # 4 - Diagonal flag set
        "G",                   # 5 - Diagonal flag and Up flag set
        "G",                   # 6 - Diagonal flag and Left flag set
        "G",                   # 7 - All flags are set
    ]

# Spacing constant
FORMAT_SPACING = 4

def CellFormat(value):
    '''
    Returns a right justified string based on spacing constant.
    Returns a str()
        -Returns the string " ###..." if the value passed to large to display
        with the current spacing
    '''
    value_length = len(str(value))
    if value_length >= FORMAT_SPACING:
        return " " + "#" * (FORMAT_SPACING - 1)
    else:
        return " " * (FORMAT_SPACING - value_length) + str(value)

