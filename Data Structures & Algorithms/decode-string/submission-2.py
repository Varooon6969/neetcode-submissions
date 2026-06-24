class Solution:
    def decodeString(self, s: str) -> str:
        st = list()
        num = 0
        chars = ""
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)

            if ch.isalpha():
                chars += ch

            if ch == "[":
                st.append(chars)
                st.append(num)
                num = 0
                chars = ""

            if ch == "]":
                prev_num = st.pop()
                prev_string = st.pop()
                chars = prev_string + prev_num*chars

        return chars