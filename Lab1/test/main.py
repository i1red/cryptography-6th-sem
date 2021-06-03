import os

import pytest

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
COVERAGE_DIR = os.path.join(TEST_DIR, '..', 'algorithms')

if __name__ == '__main__':
    pytest.main([TEST_DIR, '-v', '--cov', COVERAGE_DIR])
