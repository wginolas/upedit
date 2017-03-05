import sys

CSI = "\x1b["

def term_out(s):
    print(s, end="")

def term_reset():
    term_out("\x1bc")

def term_set_cursor_pos(row, col):
    term_out(CSI + str(row) + ";" + str(col) + "f")
    
def term_read():
    while True:
        c = sys.stdin.read(1)
        print("read " + repr(c))
        if len(c) > 0:
            return c

def is_ansi_code(s):
    return s.startswith(CSI) and s[-1].isalpha()

def term_read_ansi_code():
    buf = ""
    while not is_ansi_code(buf):
        print("buf:<" + repr(buf)+">")
        buf += term_read()
        while len(buf) > 0 and buf[0] != CSI[0]:
            buf = buf[1:]
    return buf

def term_get_cursor_pos():
    term_out(CSI + "6n")
    print(repr(term_read_ansi_code()))

def term_set_local_echo(on):
    if on:
        term_out(CSI + "12l")
    else:
        term_out(CSI + "12h")

term_reset()
term_set_local_echo(False)
term_set_cursor_pos(10,1)
term_get_cursor_pos()

