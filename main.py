from windows_tools.installed_software import get_installed_software
from psutil import process_iter
from keyboard import is_pressed
from time import sleep
from pywinauto.application import Application, WindowSpecification
from pywinauto.keyboard import send_keys

word_running = False


def shutdown_pastel_hilite_server():
    print("shutdown server")


def launch_pastel_hilite_server():
    print("start server")


def send_keys_ai(app):
    print("temp")


def start_ai_chat():
    process_id = program_is_running("copilot")
    if process_id is None:
        cmd_prompt = Application().start("cmd.exe")
        cmd_prompt.CommandPrompt.type_keys(
            'Start-Process "shell:AppsFolder\Microsoft.Copilot_8wekyb3d8bbwe!App"{ENTER}'
        )
        sleep(1)
        cmd_prompt.kill(soft=True)

    else:
        app = Application.connect(process_id)
        return app


def check_macro_server():
    if program_is_running("winword.exe"):
        if not word_running:
            launch_pastel_hilite_server()
            word_running = True
    elif word_running:
        print("shutdown server")
        word_running = False


def program_is_running(process_name):
    process_id = None
    for process in process_iter(["name", "pid"]):
        if process.info["name"] and process.info["name"].lower() == process_name:
            return process.info["pid"]
    return process_id


def main_loop():
    while True:
        check_macro_server()
        if is_pressed("ctrl+1"):
            print("do macro")
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


def check_installs():
    has_ai = False
    has_ms_word = False
    for software in get_installed_software():
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
