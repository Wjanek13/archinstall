import termios
import tty

def clear():
    print("\033[H\033[J", end="", flush=True)

def getch():
    with open('/dev/tty', 'r') as tty_file:
        fd = tty_file.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = tty_file.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

if __name__ == "__main__":
    while True:
        key = getch()
        clear()
        print(f"\nYou pressed: {key}")
