from psutil import process_iter
from keyboard import is_pressed
from time import sleep
from subprocess import Popen
from pyautogui import click, write, press, locateCenterOnScreen

word_running = False
copilot_id = "locators\copilot_txtbx.png"
power_shell_id = "locators\power_shell.png"
copilot_1 = "temp"


def shutdown_pastel_hilite_server():
    print("shutdown server")


def launch_pastel_hilite_server():
    print("start server")


def ask_copilot(keys):
    Popen("start powershell", shell=True)
    sleep(1)
    # brings back chat dialog if minimized/closed
    # works even if process is already running
    write('Start-Process "shell:AppsFolder\Microsoft.Copilot_8wekyb3d8bbwe!App"')
    press("enter")
    sleep(1)
    x, y = locateCenterOnScreen(image=power_shell_id, grayscale=False)
    click(x, y)
    write("exit")
    press("enter")
    x, y = locateCenterOnScreen(image=copilot_id, grayscale=False)
    click(x, y)
    write(keys)
    press("enter")


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
            start_ai_chat(copilot_1)
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
    type_stuff = "how do I make ice cream?"
    ask_copilot(type_stuff)
