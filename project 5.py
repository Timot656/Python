import os
import platform

def shutdown():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("shutdown /s /t 1")
    elif current_os == "Linux" or current_os == "Darwin":  
        os.system("shutdown now")
    else:
        print("Unsupported OS")