# unix is so pretty
def getch():
        import sys, tty, termios, select
        if not sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            return None
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
