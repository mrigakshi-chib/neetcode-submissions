class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c,0) + 1
        for i in range(len(s1)):
            c = s2[i]
            window[c] = window.get(c,0) + 1
        if need == window:
            return True
        window_size = len(s1)
        for right in range(window_size, len(s2)):
            incoming = s2[right]
            outgoing = s2[right - window_size]

            window[incoming] = window.get(incoming, 0) + 1

            window[outgoing] -= 1

            if window[outgoing] == 0:
                del window[outgoing]
            if window == need:
                return True

        return False