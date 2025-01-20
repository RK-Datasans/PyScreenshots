
# Screenshot Automation with FTP Upload

This Python script automates the process of capturing screenshots on your system, uploading them to an FTP server, and performing automatic cleanup of local screenshots older than 24 hours. It can take screenshots at regular intervals or whenever a new file, application, or browser tab is opened.

## Features

- **Automatic Screenshot Capture**: Takes screenshots every 20 minutes and whenever a new application or window is detected.
- **FTP Upload**: Uploads screenshots to a configured FTP server with timestamps.
- **Local Cleanup**: Deletes screenshots older than 24 hours from the local system to save space.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

You'll also need to install the following Python packages:

- `pyautogui`: For taking screenshots.
- `psutil`: For monitoring running processes and detecting application/window changes.
- `ftplib`: For uploading files to an FTP server.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/screenshot-ftp-upload.git
cd screenshot-ftp-upload
```

### 2. Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install pyautogui psutil
```

## Configuration

Before running the script, modify the following configuration options in the script:

### FTP Configuration:

Update the following variables in the script with your FTP credentials:

```python
ftp_host = "your_ftp_host"
ftp_user = "your_ftp_username"
ftp_pass = "your_ftp_password"
ftp_directory = "/path/to/upload"
```

### Screenshot Directory:

Set the directory path where you want the screenshots to be saved locally:

```python
screenshot_directory = "/path/to/screenshot/directory"
```

Make sure this directory exists and the script has the necessary permissions to write and delete files in this location.

## Usage

To run the script:

```bash
python screenshot_ftp_upload.py
```

The script will start:

- **Taking screenshots** at regular intervals (every 20 minutes).
- **Capturing screenshots** whenever a new application or window is opened.
- **Uploading screenshots** to the specified FTP server.
- **Deleting screenshots** older than 24 hours from the local system.

### Scheduled Execution

For continuous operation, you can schedule the script to run automatically:

- **Windows**: Use Task Scheduler to run the script at startup.
- **Linux/macOS**: Use `cron` jobs to run the script at startup or periodically.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- The script uses the **`pyautogui`** library for taking screenshots.
- **`psutil`** is used to detect active processes and windows.
- **`ftplib`** is used to upload screenshots to the FTP server.

## Troubleshooting

- Ensure that the script has the necessary file permissions, especially in directories used for saving and deleting screenshots.
- Double-check your FTP credentials and ensure the FTP server is accessible from your local machine.
- If you encounter any issues with `psutil` detecting running applications, ensure you are using a supported operating system.

Feel free to contribute or open an issue if you encounter any bugs or need additional features.
