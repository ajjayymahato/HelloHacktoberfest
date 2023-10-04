import pyfiglet
import termcolor

def print_hacktober_anniversary():
    text = "Happy 10th Anniversary Hacktober"
    ascii_art = pyfiglet.figlet_format(text, font="starwars")

    colored_ascii_art = termcolor.colored(ascii_art, color="yellow")

    print(colored_ascii_art)

if __name__ == "__main__":
    print_hacktober_anniversary()
