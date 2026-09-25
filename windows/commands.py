import subprocess
import os
import webbrowser
import pyautogui
import time
import AppOpener
from urllib.parse import quote_plus
from config import ai_name
# -----------------------
# CHANGE THIS IF NEEDED 
# -----------------------
pyautogui.FAILSAFE = False

# -----------------------
# File Paths (CHANGE THESE TO YOUR DESIRED PATH)
# -----------------------

LIBREWOLF_PATH = r"" # CHANGE THIS TO YOUR LIBRE WOLF PATH
OSU_PATH = r"" # CHANGE THIS TO OSU PATH
CMD_PATH = r"" # CHANGE THIS TO CMD PATH
memory_path = "memory.txt"

# -----------------------
# Memory Storing/Forgetting
# -----------------------

# Storing The Memory
def store_memory(memory_text):
    try:
        with open(memory_path, "a", encoding="utf-8") as file:
            file.write(memory_text + "\n")
        print(f"{ai_name}: Memory saved.")

    except Exception as e:
        print(f"{ai_name}: Error saving memory: {e}")

# Forgetting The Memory
def forget_memory(forget_memory_text):
    try:
        with open(memory_path, "r+") as f:
            lines = f.readlines()

            new_lines = [
                line for line in lines
                if line.strip() != forget_memory_text
            ]

            if len(new_lines) == len(lines):
                print(f"{ai_name}: Memory is already forgotten.")
                return False

            f.seek(0)
            f.writelines(new_lines)
            f.truncate()

        print(f"{ai_name}: Removed")
        return True
    except Exception as e:
        print(f"{ai_name}: Failed as: {e}")
        return False
# -----------------------
# HELP COMMANDS
# -----------------------
def commands_help():
    try:
        print(f"""
        {ai_name}: heres a list of commands you can use:

        # Basic Features
        "/commands"

        # Open Commands
        "open librewolf"
        "open notepad"
        "open calculator"
        "open browser"
        "write in the notepad"
        "open osu"
        "run this in terminal"

        # Close Commands
        "close librewolf"
        "close notepad"
        "close calculator"
        "close browser"
        "close ollama"
        "close osu"

        # Automated Commands
        "open shanzos github"
        "open shanzos website"
        "open google maps"
        "open amazon"
        "open JPLT"
        """)
    except Exception as e:
        print(f"{ai_name}: Load Failed: {e}")

# -----------------------
# OPEN APPS COMMANDS
# -----------------------

# Loads Ollama in its own isolated terminal
def load_ollama_in_terminal():
    try:
        AppOpener.open("terminal")
        time.sleep(1)
        pyautogui.write(r'py -3.14 "{BLANK}"',interval=0.01) # CHANGE BLANK TO YOUR MAIN.PY PATH
        pyautogui.press("enter")
        print(f"{ai_name}: Ollama client started in terminal.")
        time.sleep(2)
        os.system("taskkill /F /IM Code.exe >nul 2>&1")

    except Exception as e:
        print(f"{ai_name}: Load Failed: {e}")


# Opens the OSU game
def open_osu():
    try:
        subprocess.Popen([OSU_PATH])
        print(f"{ai_name}: OSU has been opened.")

    except Exception as e:
        print(f"{ai_name}: Load Failed: {e}")

# Opens LibreWolf
def open_librewolf():
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        print(f"{ai_name}: LibreWolf launched successfully.")

    except Exception as e:
        print(f"{ai_name}: Load Failed: {e}")

# Opens Notepad

def open_notepad():
    try:
        subprocess.Popen(["notepad.exe"])
        print(f"{ai_name}: Notepad launched successfully.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Opens Calculator
def open_calculator():
    try:
        subprocess.Popen(["calc.exe"])
        print(f"{ai_name}: Calculator launched successfully.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Opens Notepad and writes whatever the user inputs
def write_notepad():
    try:
        notepad_message = input(f"{ai_name}: Enter your message for the notepad: ")

        if notepad_message:
            subprocess.Popen(["notepad.exe"])
            time.sleep(0.5)
            pyautogui.write(notepad_message)
            print(f"{ai_name}: Wrote {notepad_message} in notepad.")
        else:
            print(f"{ai_name}: Your message needs to be filled in mate.")
    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Opens your browser

def open_browser():
    try:
        webbrowser.open("https://www.duckduckgo.com")
        print(f"{ai_name}: Browser opened.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# -----------------------
# CLOSE APPS COMMANDS
# -----------------------
# Closes Ollama
def close_ollama():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "python.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: Ollama has been closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")


# Closes OSU
def close_osu():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "osu!.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: OSU has been closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")


# Closes LibreWolf
def close_librewolf():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "librewolf.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: LibreWolf has been closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")


# Closes Notepad
def close_notepad():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "notepad.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: Notepad has been closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")


# Closes Calculator
def close_calculator():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "CalculatorApp.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: Calculator has been closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")


# Closes the browser
def close_browser():
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "librewolf.exe"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"{ai_name}: Browser closed.")
    except Exception as e:
        print(f"{ai_name}: Close Failed: {e}")

# -----------------------
# Automated Tasks
# -----------------------

# DuckDuckGo Search in librewolf browser 
def duckduckgo(search_query=""):
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')

        url = "https://duckduckgo.com/"

        if search_query:
            url += "?q=" + quote_plus(search_query)

        pyautogui.write(url)
        pyautogui.press('enter')

        print(f"{ai_name}: Opened browser searching for for '{search_query}'.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")
        

# YouTube Search
def youtube(search_query=""):
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')

        url = "https://youtube.com/"

        if search_query:
            url += "results?search_query=" + quote_plus(search_query)

        pyautogui.write(url)
        pyautogui.press('enter')

        print(f"{ai_name}: Opened YouTube searching for for '{search_query}'.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Google Maps
def google_map(search_query=""):
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')

        url = "https://www.google.com/maps"

        if search_query:
            url += "/search/" + quote_plus(search_query)

        pyautogui.write(url)
        pyautogui.press('enter')

        print(f"{ai_name}: Opened Google Maps for '{search_query}'.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Search for github repositorys or profiles
def github(search_query=""):
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')
        url = "https://github.com/"

        if search_query:
            url += "" + quote_plus(search_query)

        pyautogui.write(url)
        pyautogui.press('enter')

        print(f"{ai_name}: Opened Github searching for '{search_query}'.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")


# Amazon UK
# Searches Amazon UK for the user's requested product
def amazon(product=""):
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')

        if product:
            url = "https://www.amazon.co.uk/s?k=" + quote_plus(product)
        else:
            url = "https://www.amazon.co.uk/"

        pyautogui.write(url)
        pyautogui.press('enter')
        print(f"{ai_name}: Opened Amazon UK for '{product}'.")

    except Exception as e:
        print(f"{ai_name}: Failed: {e}")



# Japanese Hiragana/Katakana Practice
def practice_hirigana_and_katakana():
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')

        url = "https://kana-quiz.tofugu.com/"

        pyautogui.write(url)
        pyautogui.press('enter')#
        print(f"{ai_name}: Opened The JPLT")
    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Shanzo Github
def shanzo_github():
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write("https://github.com/shanzofr")
        pyautogui.press('enter')
        print(f"{ai_name}: Opened Shanzo's GitHub.")
    except Exception as e:
        print(f"{ai_name}: Failed: {e}")

# Shanzo Website
def shanzo_web():
    try:
        subprocess.Popen([LIBREWOLF_PATH])
        time.sleep(1)
        pyautogui.press('f11')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write("https://shanzofr.github.io/")
        pyautogui.press('enter')
        print(f"{ai_name}: Opened Shanzo's GitHub.")
    except Exception as e:
        print(f"{ai_name}: Failed: {e}")



# -----------------------
# Commands List
# -----------------------

COMMANDS = {

    # Basic Commands
    "/commands": commands_help,
    
    # Open Commands
    "open librewolf": open_librewolf,
    "open notepad": open_notepad,
    "open calculator": open_calculator,
    "open browser": open_browser,
    "write in the notepad": write_notepad,
    "open osu": open_osu,
    "run this in terminal": load_ollama_in_terminal,

    # Close Commands
    "close librewolf": close_librewolf,
    "close notepad": close_notepad,
    "close calculator": close_calculator,
    "close browser": close_browser,
    "close ollama": close_ollama,
    "close osu": close_osu,

    # Automated Commands
    "open shanzos github": shanzo_github,
    "open shanzos website": shanzo_web,
    "open google maps": google_map,
    "open amazon": amazon,
    "open JPLT": practice_hirigana_and_katakana,
    "open duckduckgo": duckduckgo,
    "open youtube": youtube,
    "open github": github,
}
