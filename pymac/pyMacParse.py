import os
from pymac.buffering import reset

def Lexer(code):
    i = 0;
    buf = ""
    macroname = "";
    arch = 0
    state = 0;
    argarr = []
    for c in code:
        if (c == '(' and state == 0):
            state = 1;
            macroname = buf
            buf = reset(buf);
        elif c == ',' and state == 1:
            argarr.append(buf.strip());
            buf = reset(buf)
        elif c == '"' and state == 1:
            arch = state
            state = 999
        elif c == '"' and state == 999:
            state = arch
            arch = 0
        elif c == ')' and state == 1:
            state = 0;
            if (len(buf) > 0):
                argarr.append(buf.strip());
            break;
        else:
            buf += c
        i += 1
    return {
        "macroname": macroname,
        "args": argarr,
        "laststate": state
    }