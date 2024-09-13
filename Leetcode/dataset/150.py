class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c not in ["+","-","*","/"]:
                st.append(int(c))
            else:
                a = st.pop()
                b = st.pop()
                st.append(int(eval(f"{b}{c}{a}")))
        return st[-1]