"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""


def dec2bin_forwards(num):
    """Convert a decimal number to binary representation."""

    options = '01'

    if num < 2:
        return options[num]
    else:
        return dec2bin_forwards(num // 2) + options[num % 2]

def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    options = '01'

    if num < 2:
        return options[num]
    else:
        return dec2bin_backwards(num // 2) + options[num % 2]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
