import colorama
from colorama import Fore

# Initialize colorama
colorama.init()

def generate_numbers_series(digits):
    if digits <= 0:
        print(Fore.RED + "Please enter a positive integer.")
        return
    
    lower_bound = 10**(digits-1) if digits > 1 else 0
    upper_bound = (10**digits) - 1
    
    with open("Wordlist.txt", "w") as file:
        for num in range(lower_bound, upper_bound + 1):
            file.write(str(num) + "\n")

    print(Fore.GREEN + f"All {digits}-digit numbers saved to Wordlist.txt")

# Get user input
digits = int(input("Enter the number of digits: "))
generate_numbers_series(digits)
