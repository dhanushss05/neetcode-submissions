class Solution:
    def encode(self, strs: list[str]) -> str:
        # Append the delimiter to EVERY string, including empty ones
        return "".join(s + "@!@#" for s in strs)

    def decode(self, s: str) -> list[str]:
        # Split will result in an extra empty string at the end, so we slice it off with [:-1]
        return s.split("@!@#")[:-1]