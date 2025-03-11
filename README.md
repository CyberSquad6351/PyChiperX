# PyChiperX - Android Pass Cracker

**PyChiperX** is a powerful Python tool designed to break into Android devices by brute-forcing the lock screen password. It uses **ADB** (Android Debug Bridge) alongside Python libraries such as `subprocess`, `random`, `time`, and `colorama` to seamlessly interact with Android devices and help you crack those pesky numeric PINs.

> **Note:** This tool is strictly for educational purposes and works only on **numeric PIN locks** (numbers only, no patterns or complex passwords). Please use it responsibly!

## Features

- **Brute-Force Attack:** Automatically tries various PIN combinations from a wordlist.
- **ADB Integration:** Relies on ADB to interact with the Android device and input PINs.
- **Fully Customizable:** Allows you to adjust the maximum attempts, delay time, and wordlist path.

## How Does This Tool Work?

PyChiperX works by trying to brute-force the lock screen password on a locked Android device. When **USB Debugging** is enabled, the tool leverages ADB to input PIN combinations from a pre-configured wordlist. It continues until the correct PIN is found or the number of attempts is exhausted.

**The tool simulates real brute-force attacks to break numeric PIN codes.**

## How to Use the Tool

### Step 1: Install Dependencies
- Run the following command to install all required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Step 2: Open CMD
- First, open the **Command Prompt (CMD)** on your system.

### Step 3: Generate the Wordlist
- Before running the tool, you need to create a wordlist with possible PIN combinations. Run the `Wordlist.py` script to generate this wordlist.
 
Command: 
  - Linux/Mac: `python3 Wordlist.py`
  - Windows: `python Wordlist.py`

### Step 4: Run the `Main.py` File
- Run the main file by typing:
  - Linux/Mac: `python3 Main.py`
  - Windows: `python Main.py`

### Step 5: Provide The Wordlist File Path
- Provide the path to the generated wordlist.

### Step 6: Enter the Number of Attempts
- Enter the number of attempts you'd like to try at a time. Choose this based on how many attempts your device will allow before locking you out.

### Step 7: Enter the Time Delay Between Attempts
- Enter the number of seconds to wait after each attempt before the next one is made.

Now you're ready to crack! Run the main script to start the process.

### Requirements:
- Python 3.x
- Android device with **USB Debugging** enabled
- ADB (Android Debug Bridge) installed

### Required Python Modules:
- `subprocess`
- `random`
- `time`
- `colorama`

### Installation:
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/repo-name.git](https://github.com/CyberSquad6351/PyChiperX.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Tool:
1. Connect your Android device and ensure **USB Debugging** is enabled.
2. Start the unlocking process by running the main tool script:
    ```bash
    python pass_cracker.py
    ```

3. **Input Configuration**:
   - Provide the path to your wordlist.
   - Set the maximum number of attempts and the delay time between each try.

### **Important Note for Windows 10 Users:**
If you're using **Windows 10**, make sure to add the ADB path to your **Environment Variables** for smooth operation. Here's how:

1. Search for **Environment Variables** in the Windows search bar and select **Edit the system environment variables**.
2. Under the **System Properties** window, click on **Environment Variables**.
3. In the **System Variables** section, scroll down and find the **Path** variable, then click **Edit**.
4. Add the ADB path to the list (e.g., `C:\Program Files (x86)\Android\android-sdk\platform-tools`).
5. Click **OK** to save and exit.

This will ensure that ADB commands can be run from anywhere in CMD.

---

## License

This tool is for educational use only. Use it responsibly, and always respect the privacy and security of others.

## Contact

- Website: [Cyber_Squad6351](https://cybersquad6351.netlify.app/)
- YouTube: [Cyber_Squad6351 Channel](https://youtube.com/@cyber_squad6351?si=8Lm-a76txyExM5F_)
- Instagram: [@cyber__squad6351](https://www.instagram.com/cyber__squad6351/)
- Email: [mishraaditya.skm14@gmail.com](mailto:mishraaditya.skm14@gmail.com)
