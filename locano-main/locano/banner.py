#!/usr/bin/python
green = "\033[92m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"
cyan = "\033[36m"

def print_banner():
    banner = f"""
{white} +-------------------------------------------------------+
{white} |{green} _____      ____     ______      __      ____  _____   ____   {white} |
{white} |{green}|_   _|   .'    \. ./ ___  |    /  \    |_   \|_   _|.'    \. {white} |
{white} |{green}  | |    /  .--.  \ ./   \_|   / /\ \     |   \ | | /  .--.  \{white} |
{white} |{green}  | |   _| |    | | |         / ____ \    | |\ \| | | |    | |{white} |
{white} |{green}_ | |__/ |  \--'  / \.___.'\_/ /    \ \_ _| |_\   |_\  \--'  /{white} |
{white} |{green}|________|\.____.' \._____.'____|  |____|_____|\____|\.____.' {white} |

{white} +--------------{cyan}({red}Improved by Raj Yadav{cyan}){white}--------------------+{reset}
"""
    print(banner)
