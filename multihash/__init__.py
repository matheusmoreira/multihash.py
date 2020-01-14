"""Future-proof self-describing hashes.

Examples:
    decode(data).digest
"""

from typing import NamedTuple

import uvarint


class MultiHash(NamedTuple):
    """The digest, its length and the hashing algorithm that produced it."""
    function: int
    length: int
    digest: bytes


class LengthMismatchError(Exception):
    """Raised when the multihash and actual digest lengths don't match."""

    expected: int
    actual: int

    def __init__(self, expected: int, actual: int) -> None:
        template = "length from data ({}) and metadata ({}) don't match"
        super().__init__(template.format(actual, expected))

        self.expected = expected
        self.actual = actual

def decode(multihash: bytes) -> MultiHash:
    """Decode the given bytes as a multihash value."""
    (function, length), digest = uvarint.cut(2, multihash)

    if len(digest) != length:
        raise LengthMismatchError(length, len(digest))

    return MultiHash(function, length, digest)
