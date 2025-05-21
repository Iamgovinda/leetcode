class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = dict(
            I=1,
            V=5,
            X=10,
            L=50,
            C=100,
            D=500,
            M=1000
        )

        num = 0
        for i in range(0, len(s)):
            if (i != len(s) - 1):
                if roman_map[s[i]] >= roman_map[s[i + 1]]:
                    num += roman_map[s[i]]
                    continue
            else:
                num += roman_map[s[i]]
                continue
            num -= roman_map[s[i]]
        return num
