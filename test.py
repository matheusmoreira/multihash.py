import unittest
from typing import List, NamedTuple

import multihash

def h(s: str) -> bytes:
    return bytes(bytearray.fromhex(s))

class Representation(NamedTuple):
    """A map of bytes to its known correct binary representation."""
    value: multihash.MultiHash
    binary: bytes

class TestMultiHash(unittest.TestCase):

    # Example values from the multihash website and specification
    # https://multiformats.io/multihash/
    # https://github.com/multiformats/multihash/blob/master/README.md
    examples: List[Representation] = [
        Representation(
            multihash.MultiHash(0x12, 0x20, h('41dd7b6443542e75701aa98a0c235951a28a0d851b11564d20022ab11d2589a8')),
            h('122041dd7b6443542e75701aa98a0c235951a28a0d851b11564d20022ab11d2589a8')
        ),
    ]

    all: List[Representation] = examples

    def test_decode(self) -> None:
        value: multihash.MultiHash
        binary: bytes

        for (value, binary) in TestMultiHash.all:
            self.assertEqual(multihash.decode(binary), value)


if __name__ == '__main__':
    unittest.main()
