import string
import random
from typing import Final, Optional


CHARS: Final[str] = string.ascii_letters + string.punctuation + string.digits


def random_bytes(length: Optional[int] = None) -> bytes:
    if length is None:
        length = random.randint(1, 100)

    return ''.join(random.choice(CHARS) for _ in range(length)).encode()
