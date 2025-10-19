from pathlib import Path
from colorama import Fore, Style, init

# Initialize Colorama with auto-reset after each print
init(autoreset=True)

def iterate_folder(path, level=1):

    for el in path.iterdir():
        # Create indentation based on the current level (4 spaces per level)
        indent = "    " * level  
        if el.is_dir():
            # Print directory name in blue with a trailing slash
            print(Fore.BLUE + indent + el.name + "/")
            # Recursively call the function for the subdirectory
            iterate_folder(el, level + 1)
        else:
            # Print file name in green
            print(Fore.GREEN + indent + el.name)


try:
    # Prompt the user to input the absolute path of the directory
    absolute_path = Path(input("👉 Input absolut path of the directory 👉"))

    # Check if the path exists
    if not absolute_path.exists():
        raise FileNotFoundError("Directory does not exist")
    
    # Check if the path is actually a directory
    if not absolute_path.is_dir():
        raise NotADirectoryError("This is not a directory")
    
    # Print the root directory name in blue
    print(Fore.BLUE + absolute_path.name + "/")

    # Start iterating through the directory
    iterate_folder(absolute_path)

# Catch common errors and display them in bright red
except (ValueError, FileNotFoundError, NotADirectoryError) as e:
    print(Fore.RED + Style.BRIGHT + f"Error: {e}")
