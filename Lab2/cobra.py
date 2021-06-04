from typing import Final, Callable

import numpy as np

from utils import hex_pi_digit_generator, int_rotate_right, int_rotate_left


BLOCK_SIZE: Final[int] = 4
ROUNDS: Final[int] = 24
MAX_KEY_SIZE: Final[int] = ROUNDS // 2 * (BLOCK_SIZE - 1)
W_FIRST_DIM_SIZE: Final[int] = 2
S_SECOND_DIM_SIZE: Final[int] = 256


class Cobra:
    def __init__(self, key: np.ndarray) -> None:
        if len(key) == 0 or len(key) > MAX_KEY_SIZE:
            raise ValueError(f'Key length should be in range 1 to {MAX_KEY_SIZE}')
        key = key.copy()

        hex_pi_gen = hex_pi_digit_generator()
        self.P = (np.fromiter(hex_pi_gen, dtype=np.int32, count=ROUNDS * (BLOCK_SIZE - 1))
                  .reshape((ROUNDS, BLOCK_SIZE - 1)))
        self.S = (np.fromiter(hex_pi_gen, dtype=np.int32, count=BLOCK_SIZE * S_SECOND_DIM_SIZE)
                  .reshape((BLOCK_SIZE, S_SECOND_DIM_SIZE)))
        self.W = (np.fromiter(hex_pi_gen, dtype=np.int32, count=W_FIRST_DIM_SIZE * BLOCK_SIZE)
                  .reshape((W_FIRST_DIM_SIZE, BLOCK_SIZE)))

        for repetition in range(2):
            key_index = np.arange(np.product(self.P.shape)).reshape(self.P.shape) % len(key)
            self.P ^= key[key_index]

            self.change_boxes(self.P)

            if repetition == 0:
                key = np.vectorize(int_rotate_right)(key, 1)

        self.change_boxes(self.P)
        self.change_boxes(self.S)
        self.change_boxes(self.W)

    def change_boxes(self, boxes: np.ndarray) -> None:
        buffer = np.zeros((BLOCK_SIZE,), dtype=np.int32)

        for i, index in enumerate(np.ndindex(boxes.shape)):
            if i % BLOCK_SIZE == 0:
                buffer = self.encrypt_block(buffer)
            boxes[index] = buffer[i % BLOCK_SIZE]

    def encrypt_block(self, data: np.ndarray) -> np.ndarray:
        if len(data) != BLOCK_SIZE:
            raise ValueError(f'Block size should be {BLOCK_SIZE}')

        result = data ^ self.W[0]

        next_result = np.zeros((BLOCK_SIZE,), dtype=np.int32)

        for i in range(ROUNDS):
            next_result[0] = result[BLOCK_SIZE - 1]
            for j in range(1, BLOCK_SIZE):
                next_result[j] = int_rotate_right(result[j - 1] ^ self.f(result[j], self.P[i][j - 1]), 1)

            result = next_result.copy()

        result ^= self.W[W_FIRST_DIM_SIZE - 1]
        return result

    def decrypt_block(self, data: np.ndarray) -> np.ndarray:
        if len(data) != BLOCK_SIZE:
            raise ValueError(f'Block size should be {BLOCK_SIZE}')

        result = data ^ self.W[W_FIRST_DIM_SIZE - 1]

        next_result = np.zeros((BLOCK_SIZE,), dtype=np.int32)

        for i in range(ROUNDS - 1, -1, -1):
            next_result[BLOCK_SIZE - 1] = result[0]
            for j in range(BLOCK_SIZE - 1, 0, -1):
                next_result[j - 1] = int_rotate_left(result[j], 1) ^ self.f(next_result[j], self.P[i][j - 1])

            result = next_result.copy()

        result ^= self.W[0]
        return result

    def f(self, x: int, p: int) -> int:
        z = x ^ p
        return (((self.S[0, (z >> 24) & 0xff] + self.S[1, (z >> 16) & 0xff])
                ^ self.S[2, (z >> 8) & 0xff]) + self.S[3, z & 0xff])

