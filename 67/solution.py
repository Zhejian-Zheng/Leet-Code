class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int(a, 2) -> make the int into binary
        # bin()[2:] -> make the result into binary and ignor the 0b
        return bin(int(a, 2) + int(b, 2))[2:]