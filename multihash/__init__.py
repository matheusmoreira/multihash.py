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


def decode(multihash: bytes) -> MultiHash:
    """Decode the given bytes as a multihash value."""
    (function, length), bytes_read = uvarint.expect(2, multihash)
    digest = multihash[bytes_read:]

    return MultiHash(function, length, digest)
