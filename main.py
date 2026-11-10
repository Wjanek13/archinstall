import shutil, sys
print("hello")
print("\033[2J\033[1;1H", end='')
x, y = shutil.get_terminal_size()
print(f"X: {x}, Y: {y}")
