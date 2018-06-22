#!/usr/bin/env python3

# This file is the main entrypoint for the MED code
# Can be called from the command line

import sys
import os
import MED

def main():
    # If we didn't get enough arguments, print usage info and exit
    if len(sys.argv) < 3:
        print("USAGE: %s SOURCE_WORD DESTINATION_WORD" % sys.argv[0])
        sys.exit(1)

    matrix = MED.Matrix(sys.argv[1], sys.argv[2])

    print("Minimum Edit Distance: %d" % matrix.MED)
    print("Distance Matrix/Backtrace Matrix:")

    print(matrix.getDistMatrixFormatted())

    sys.stdout.write(os.linesep)  # Newline

    print(matrix.getBTMatrixFormatted())

    sys.stdout.write(os.linesep)  # Newline again

    print("String Alignment:")
    print(matrix.getStringAlignmentFormatted())

# Having a main() makes Python feel like C, which makes me feel better
if __name__ == "__main__":
    main()
