from psutil import process_iter
from keyboard import is_pressed
from time import sleep
from subprocess import Popen
import pyautogui

word_running = False


def shutdown_pastel_hilite_server():
    print("shutdown server")


def launch_pastel_hilite_server():
    print("start server")


def send_keys_ai(keys):
    print("temp")


def start_ai_chat():
    Popen("start powershell", shell=True)
    sleep(1)
    # brings back chat dialog if minimized/closed
    pyautogui.write(
        'Start-Process "shell:AppsFolder\Microsoft.Copilot_8wekyb3d8bbwe!App"'
    )
    pyautogui.press("enter")
    sleep(1)
    pyautogui.hotkey("alt", "tab")
    sleep(1)
    pyautogui.write("exit")
    pyautogui.press("enter")
    sleep(1)
    copilot_input_loc = pyautogui.locateAllOnScreen("/locators/coilot_txtbx.png")


def check_macro_server():
    if program_is_running("winword.exe"):
        if not word_running:
            launch_pastel_hilite_server()
            word_running = True
    elif word_running:
        print("shutdown server")
        word_running = False


def program_is_running(process_name):
    for process in process_iter(["name"]):
        if process.info["name"] and process.info["name"].lower() == process_name:
            return True
    return False


def main_loop():
    while True:
        # check_macro_server()
        if is_pressed("ctrl+1"):
            start_ai_chat()
        elif is_pressed("ctrl+2"):
            print("do macro")
        elif is_pressed("ctrl+3"):
            print("do macro")
        elif is_pressed("ctrl+4"):
            print("do macro")
        elif is_pressed("ctrl+5"):
            print("do macro")
        elif is_pressed("ctrl+6"):
            print("do macro")
        elif is_pressed("ctrl+7"):
            print("do macro")
        elif is_pressed("ctrl+8"):
            print("do macro")
        elif is_pressed("ctrl+9"):
            print("do macro")
        elif is_pressed("ctrl+0"):
            print("do macro")
        elif is_pressed("ctrl+1+2"):
            print("do macro")
        elif is_pressed("ctrl+1+3"):
            print("do macro")
        elif is_pressed("ctrl+1+4"):
            print("do macro")
        elif is_pressed("ctrl+1+5"):
            print("do macro")
        elif is_pressed("ctrl+1+6"):
            print("do macro")
        elif is_pressed("ctrl+1+7"):
            print("do macro")
        sleep(0.1)


if __name__ == "__main__":
    # main_loop()
    # type_stuff = "test"
    start_ai_chat()
