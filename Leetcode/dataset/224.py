class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join([c for c in s if c != ' '])

        st = [] 
        RPN = []   
        priority = {'(':0, '+':1, '-':2, '_':3}
        num, flag = 0, False
        for i, c in enumerate(s):
            if 48 <= ord(c) <= 57:
                num = num * 10 + int(c)
                flag= True
                continue
            if flag:
                RPN.append(num)
                flag = False
                num = 0
            if c == '(':
                st.append(c)
            elif c == '-' and (not i or st and s[i-1] == '('):  
                    st.append('_')
            elif c == ')':
                while st:
                    c = st.pop()
                    if c == '(':
                        break
                    RPN.append(c)
            else:
                while st and priority[st[-1]] >= priority[c]:
                    RPN.append(st.pop())
                st.append(c)
        if flag:
            RPN.append(num)
        while st:
            RPN.append(st.pop())
                
        st = []
        for c in RPN:
            if c not in ["+","-","_"]:
                st.append(int(c))
            else:
                a = st.pop()
                if c == '+':
                    b = st.pop()
                    st.append(a+b)
                elif c == '-':
                    b = st.pop()
                    st.append(b-a)
                elif c == '_':
                    st.append(-a)
        return st[-1]