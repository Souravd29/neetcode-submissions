from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)       # frequency of each char required
        required = len(need)    # number of unique chars to satisfy

        window = {}
        have = 0                # unique chars currently satisfied

        left = 0
        result = ""
        result_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if (right - left + 1) < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return result