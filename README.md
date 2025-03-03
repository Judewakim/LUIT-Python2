# 📂 LUIT-Python2

A Python script that generates a list of dictionaries containing details about files in a specified directory. It supports recursive traversal and displays file details in a Linux `ll` command-like format.

## 🚀 Features
- Retrieves file details such as name, size, last modified time, and permissions.
- Supports optional directory input (defaults to the current directory if none provided).
- Recursively scans nested directories.
- Displays output in a Linux CLI `ll` view.

## 🛠️ Installation & Usage
### Prerequisites
Ensure you have Python installed on your system.

### Running the Script
Clone the repository and navigate into the directory:
```bash
 git clone https://github.com/Judewakim/LUIT-Python2.git
 cd LUIT-Python2
```
Run the script:
```bash
python .\data_extraction.py
```
Or specify a directory:
```bash
python .\data_extraction.py /path/to/directory
```

## 📜 Example Output
```
Enter the directory path (press Enter to use current directory):

Linux CLI 'll' View:
644 1024 Tue Feb 20 10:30:45 2025 /home/user/file1.txt
755 4096 Tue Feb 19 14:15:30 2025 /home/user/scripts/script.sh
```

## 📌 Contributing
Feel free to fork this repository and submit pull requests for improvements!

## 📜 License
This project is open-source and available under the MIT License.

---
💡 *Happy Coding!*

