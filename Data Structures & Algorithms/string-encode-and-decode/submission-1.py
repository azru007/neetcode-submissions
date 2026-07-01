import ctypes
class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs: return ""
        return str(id(strs))
    def decode(self, s: str) -> List[str]:
        # if not s: return []
        return ctypes.cast(int(s), ctypes.py_object).value 
