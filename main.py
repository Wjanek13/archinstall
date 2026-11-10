import sys
import termios
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == "__main__":
    print("Press any key to continue (or 'q' to exit): ", end="", flush=True)
    key = getch()
    print(f"\nYou pressed: {key}")
