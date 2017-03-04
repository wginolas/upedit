CSI = "\x1b["

def term_set_cursor_pos(row, col):
    print(CSI + str(row) + ";" + str(col) + "f", end="")
    
print("Hello World!")

term_set_cursor_pos(2,1)


