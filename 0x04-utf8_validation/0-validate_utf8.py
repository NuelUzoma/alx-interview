#!/usr/bin/python3
"""Write a method that determines if a given data set represents
a valid UTF-8 encoding."""


def validUTF8(data):
    numBytes = 0

    for byte in data:
        if numBytes == 0:
            if byte >= 128:
                numOnes = 0
                # Count the number of consecutive 1s starting from MSB
                mask = 1 << 7
                while mask & byte:
                    numOnes += 1
                    mask = mask >> 1

                # Check if number of consecutive 1s is valid
                if numOnes < 2 or numOnes > 4:
                    return False

                # Determine the number of bytes required for this character
                numBytes = numOnes - 1

                # Check for single-byte character
                if numBytes == 0:
                    continue
            else:
                continue
        else:
            # Verify that the byte starts with "10"
            if not (128 <= byte <= 191):
                return False

            numBytes -= 1

    # After processing all bytes, check if any extra bytes remain
    return numBytes == 0
