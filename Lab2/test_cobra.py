import os
import random
import numpy as np

import pytest

from cobra import Cobra


def test_cobra():
    key = np.random.randint(0, 1_000_000, size=random.randint(3, 10), dtype=np.int32)
    cobra = Cobra(key)

    for _ in range(10):
        data = np.random.randint(0, 1_000_000, size=4)
        encrypted_data = cobra.encrypt_block(data)
        decrypted_data = cobra.decrypt_block(encrypted_data)
        assert np.any(encrypted_data != data)
        assert np.all(data == decrypted_data)


if __name__ == '__main__':
    pytest.main([os.path.relpath(__file__), '-v'])
