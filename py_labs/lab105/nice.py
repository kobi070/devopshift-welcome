from pyfiglet import Figlet


def print_title(text: str):
    f = Figlet("3d-ascii", justify="center", width=100)
    print(f.renderText(text))