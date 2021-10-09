from os import name, system

def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')