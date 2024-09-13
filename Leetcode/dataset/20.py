class Solution:
    def isValid(self, s: str) -> bool:
        from queue import LifoQueue
        st = LifoQueue()
        map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if st.empty():
                st.put(c)
            else:
                top = st.queue[-1]
                if c in map:
                    if top != map[c]:
                        return False
                    st.get()
                else:
                    st.put(c)
        return st.empty()