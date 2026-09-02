class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        start = ""
        backup = ""
        end = ""
        for i in s:
            if i == "0":
                backup += "0"
            elif end != "" and i == "1":
                start += "1"
            else:
                end += "1"
        result = start + backup + end
        return result
