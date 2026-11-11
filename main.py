import sys
import termios
import tty

choices = ["a", "b", "c"]
selected = 0
selected_min = 0
selected_max = len(choices) - 1

def clear():
    print("\033[H\033[J", end="", flush=True)

def getch():
    with open('/dev/tty', 'r') as tty_file:
        fd = tty_file.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = tty_file.read(1)

            if ch == '\x1b':
                seq = tty_file.read(2)
                if seq == '[A':
                    return 'UP'
                elif seq == '[B':
                    return 'DOWN'
                elif seq == '[C':
                    return 'RIGHT'
                elif seq == '[D':
                    return 'LEFT'
                return '\x1b' + seq
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def render():
    for i, choice in enumerate(choices):
        if i == selected:
            print(f"> {choice}")
        else:
            print(f"  {choice}")
def __exit__():
    print("\x1b[?25h", end="", flush=True)
if __name__ == "__main__":
    print("\x1b[?25l", end="", flush=True)
    clear()
    render()
    while True:
        key = getch()
        match key:
            case '\x03':
                __exit__()
                clear()
                break
            case "UP":
                if selected != selected_min:
                    selected -= 1
            case "DOWN":
                if selected != selected_max:
                    selected += 1
        clear()
        render()
