class Keccak256:
    def __init__(self):
        self.state = [0] * 200
        self.rate = 1088
        self.capacity = 512
        self.delimited_suffix = 0x01
        self.output_length = 256
        self.block_size = self.rate // 8
        self.reset()

    def reset(self):
        self.state = [0] * 200
        self.buffer = bytearray()
        self.bits_in_buffer = 0

    def absorb(self, data):
        self.buffer.extend(data)
        self.bits_in_buffer += len(data) * 8

        while self.bits_in_buffer >= self.rate:
            self._absorb_block()
            self.bits_in_buffer -= self.rate

    def squeeze(self):
        self.buffer.append(self.delimited_suffix)
        self.buffer += b'\x00' * (self.block_size - len(self.buffer) % self.block_size)
        self.state[:len(self.buffer)] = self.buffer
        self.state[len(self.buffer)] ^= 0x80
        self._keccak_f()

        return bytes(self.state[:self.output_length // 8])

    def _absorb_block(self):
        for i in range(self.block_size):
            self.state[i] ^= self.buffer[i]
        self._keccak_f()
        self.buffer = self.buffer[self.block_size:]

    def _keccak_f(self):
        R = range
        rotc = [
            0, 1, 62, 28, 27, 36, 44, 6, 55, 20, 3, 10, 43, 25, 39, 41, 45, 15,
            21, 8, 18, 2, 61, 56, 14
        ]
        piln = [
            10, 7, 11, 17, 18, 3, 5, 16, 8, 21, 24, 4, 15, 23, 19, 13, 12, 2,
            20, 14, 22, 9, 6, 1
        ]
        RC = [
            1, 32898, -9223372036854742902, -9223372034707259392, 32907,
            2147483649, -9223372034707259263, -9223372036854743031,
            138, 136, 2147516425, 2147483658, 2147516555, -9223372036854775680,
            -9223372034707292150, -9223372034707259263, -9223372036854743031,
            32896, -9223372036854743168, -9223372036854775681, 2147483649,
            -9223372034707292288, -9223372034707259392, 32907, 2147483658
        ]

        for round in R(24):
            # θ step
            C = [self.state[i] ^ self.state[i + 5] ^ self.state[i + 10] ^ self.state[i + 15] ^ self.state[i + 20] for i in R(5)]
            D = [0] * 5
            for x in range(5):
                D[x] = C[(x - 1) % 5] ^ ((C[(x + 1) % 5] << 1) & 0xFFFFFFFFFFFFFFFF)
                for y in range(5):
                    self.state[x + 5 * y] ^= D[x]

            # ρ and π steps
            t = self.state[1]
            for x in range(24):
                j = piln[x]
                t, self.state[j] = self.state[j], ((t << rotc[x]) | (t >> (64 - rotc[x]))) & 0xFFFFFFFFFFFFFFFF

            # χ step
            for y in range(0, 25, 5):
                T = self.state[y:y + 5]
                for x in range(5):
                    self.state[y + x] ^= (~T[(x + 1) % 5]) & T[(x + 2) % 5]

            # ι step
            self.state[0] ^= RC[round]

    def update(self, data):
        self.absorb(data)

    def digest(self):
        return self.squeeze()

    def hexdigest(self):
        return self.digest().hex()