import pyautogui
import time
import os
from ftplib import FTP
from datetime import datetime, timedelta
import psutil

# FTP credentials
ftp_host = "your_ftp_host"
ftp_user = "your_ftp_username"
ftp_pass = "your_ftp_password"
ftp_directory = "/path/to/upload"

# Track opened files/applications/tabs
previous_process = None

# Path where screenshots are saved
screenshot_directory = "/path/to/screenshot/directory"

# Function to check for new application/window
def check_for_new_application():
    global previous_process
    current_process = None

    # Get the current process (this will depend on the OS and libraries)
    if os.name == "nt":  # Windows
        current_process = psutil.Process(psutil.win32process.GetWindowThreadProcessId(psutil.Process().pid))
    
    if current_process != previous_process:
        previous_process = current_process
        return True
    return False

# Function to take and save screenshot
def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = pyautogui.screenshot()
    screenshot_path = os.path.join(screenshot_directory, f"screenshot_{timestamp}.png")
    screenshot.save(screenshot_path)
    print(f"Screenshot saved at {timestamp}.")
    return screenshot_path

# Function to upload screenshot to FTP
def upload_screenshot_to_ftp(file_path):
    try:
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)
        ftp.cwd(ftp_directory)
        
        with open(file_path, "rb") as f:
            ftp.storbinary(f"STOR {os.path.basename(file_path)}", f)
        
        print(f"File {file_path} uploaded to FTP.")
        ftp.quit()
    except Exception as e:
        print(f"Error uploading to FTP: {e}")

# Function to take periodic screenshots
def periodic_screenshot(interval=1200):
    while True:
        time.sleep(interval)
        file_path = take_screenshot()
        upload_screenshot_to_ftp(file_path)
        os.remove(file_path)  # Delete screenshot after upload to save space

# Function to delete screenshots older than 24 hours
def delete_old_screenshots():
    now = time.time()
    for file_name in os.listdir(screenshot_directory):
        file_path = os.path.join(screenshot_directory, file_name)
        # Check if file is older than 24 hours
        if os.path.isfile(file_path) and now - os.path.getctime(file_path) > 86400:  # 86400 seconds = 24 hours
            os.remove(file_path)
            print(f"Deleted old screenshot: {file_name}")

# Function to monitor and take screenshots
def monitor_and_take_screenshots():
    while True:
        if check_for_new_application():
            file_path = take_screenshot()
            upload_screenshot_to_ftp(file_path)
            os.remove(file_path)  # Delete screenshot after upload to save space

        # Periodic screenshot every 20 minutes
        periodic_screenshot(1200)

        # Delete old screenshots every day
        delete_old_screenshots()

# Run the monitoring function
monitor_and_take_screenshots()
