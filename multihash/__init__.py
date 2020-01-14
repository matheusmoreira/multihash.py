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

    multihash_length: int
    digest_length: int

    def __init__(self, multihash_length: int, digest_length: int) -> None:
        template = "length from data ({}) and metadata ({}) don't match"
        super().__init__(template.format(multihash_length, digest_length))

        self.multihash_length = multihash_length
        self.digest_length = digest_length

def decode(multihash: bytes) -> MultiHash:
    """Decode the given bytes as a multihash value."""
    (function, length), digest = uvarint.cut(2, multihash)

    if len(digest) != length:
        raise LengthMismatchError(length, len(digest))

    return MultiHash(function, length, digest)
