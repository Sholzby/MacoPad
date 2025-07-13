from windows_tools import installed_software
from psutil import process_iter
from keyboard import is_pressed
from time import sleep

global word_running


def shutdown_pastel_hilite_server():
    print("shutdown server")


def launch_pastel_hilite_server():
    print("start server")


def check_if_word_launched():
    for process in process_iter(["name"]):
        if process.info["name"] and process.info["name"].lower() == "winword.exe":
            if not word_running:
                launch_pastel_hilite_server()
                word_running = True
        elif word_running:
            print("shutdown server")
            word_running = False


def main_loop():
    while True:
        check_if_word_launched()
        if is_pressed("ctrl"):
            print("do macro")
        sleep(1)


def check_installs():
    has_ai = False
    has_ms_word = False
    for software in installed_software.get_installed_software():
        match software["name"]:
            case "Copilot":
                has_ai = True
            case "msWord":
                has_ms_word = True
    if has_ai and has_ms_word:
        return True
    else:
        return False


if __name__ == "__main__":
    if check_installs():
        main_loop()
