from colorama import init, Fore

# Initialize Colorama for colored terminal output
init(autoreset=True)

# Function to print colored header
def print_colored_header(text, color):
    color_code = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    print(f"{color_code.get(color, Fore.RESET)}{text}")
