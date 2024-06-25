from sys import getsizeof



class Conversor:
    __SEQUENCE = """0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ.,;:<>[](){}=!@#$%&_+-*/|"""

    def __init__(self, encoding="utf8",augmented=True):
        if augmented:
            Conversor.__SEQUENCE = "".join([chr(i) for i in range(33,500) if i<127 or i>160])
        self.encoding = encoding

    def converter(self, from_, to_, item):
        # str[string], cypher[string_based_on_SEQUENCE], int[integer], hex[hexadecimal],

        ...

    def int2cypher(self, val: int) -> str:
        if type(val) != int:
            raise TypeError("[val] must be int type.")
        if val == 0:
            return "0"
        if val < 0:
            raise ValueError("[val] must be nonnegative.")
        s = ""
        while val > 0:
            res = val % len(Conversor.__SEQUENCE)
            s += Conversor.__SEQUENCE[res]
            val -= res
            val //= len(Conversor.__SEQUENCE)
        return s[::-1]

    def cypher2int(self, cp: str) -> int:
        if type(cp) != str:
            raise TypeError("[cp] must be str type.")
        if cp == "":
            return -1
        cp = [ch for ch in cp]
        answer = 0
        exponent = 0
        while cp:
            weight = Conversor.__SEQUENCE.find(cp.pop())
            answer += weight*(len(Conversor.__SEQUENCE)**exponent)
            exponent += 1
        return answer

    def str2hex(self, stg: str) -> str:
        return stg.encode(self.encoding).hex()

    def hex2str(self, val: int) -> str:
        return (bytes.fromhex(val)).decode(self.encoding)

    def str2int(self, stg: str) -> int:
        return self.hex2int(self.str2hex(stg))

    def int2str(self, val: int) -> str:
        return self.hex2str(self.int2hex(val))

    def int2hex(self, val: int) -> str:
        return hex(val)[2:]

    def hex2int(self, hx: str) -> int:
        return int(hx, 16)

    def hex2cypher(self, hx: str) -> str:
        return self.int2cypher(self.hex2int(hx))

    def cypher2hex(self, cp: str) -> str:
        return self.int2hex(self.cypher2int(cp))

    def cypher2str(self, cp: str) -> str:
        return self.hex2str(self.cypher2hex(cp))

    def str2cypher(self, stg: str) -> str:
        return self.hex2cypher(self.str2hex(stg))

    def bytes2hex(self, bt: bytes) -> str:
        return bytes.hex(bt)

    def hex2bytes(self, hx: str) -> bytes:
        return bytes.fromhex(hx)

    def bytes2int(self, bt: bytes) -> int:
        return self.hex2int(self.bytes2hex(bt))

    def int2bytes(self, val: int) -> bytes:
        return self.hex2bytes(self.int2hex(val))

    def bytes2cypher(self, bt: bytes) -> str:
        return self.int2cypher(self.bytes2int(bt))

    def cypher2bytes(self, cp: str) -> bytes:
        return self.int2bytes(self.cypher2int(cp))

    def bytes2str(self, bt: bytes) -> str:
        return self.int2str(self.bytes2int(bt))

    def str2bytes(self, stg: str) -> bytes:
        return self.int2bytes(self.str2int(stg))

    def __repr__(self):
        return f"<Conversor object at {hex(id(self)).upper()} [{getsizeof(self)} B]>"





