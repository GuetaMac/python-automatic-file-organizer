# Python Automatic File Organizer 

A simple Python automation tool that organizes files in your Windows Downloads folder based on their file extensions.

This project uses Python to automatically sort files into categorized folders, making file management easier and more organized. It can also be scheduled to run automatically using Windows Task Scheduler.

## Features

- Automatically organizes files by file type.
- Supports preview mode before moving files.
- Prevents overwriting existing files by generating unique filenames.
- Skips existing folders and the Windows `desktop.ini` file.
- Supports automatic execution through Windows Task Scheduler.
- Uses Python's built-in libraries, so no third-party packages are required.

## Technologies Used

- Python 3
- pathlib
- shutil
- Windows Task Scheduler

## Requirements

Before running the project, make sure you have:

- A Windows computer.
- Python 3 installed.
- A terminal such as Command Prompt or the VS Code terminal.
- Basic knowledge of running Python scripts.

## Installation and Setup

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation, check **Add Python to PATH** if that option is available.

After installation, open Command Prompt and verify Python:

```bash
py --version
```

You should see your installed Python version.

### Download the Project

On this GitHub repository page:

1. Click the green **Code** button.
2. Select **Download ZIP**.
3. Extract the downloaded ZIP file.
4. Open the extracted project folder.

Alternatively, if Git is installed, clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-automatic-file-organizer.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Open the Project Folder

Open Command Prompt or a terminal inside the folder containing `file_organizer.py`.

For example:

```bash
cd path\to\python-automatic-file-organizer
```

Replace the example path with the actual location of your project folder.

### 4. Configure the Downloads Folder

Open `file_organizer.py` in a code editor.

Find this line:

```python
DOWNLOADS_FOLDER = Path.home() / "Downloads"
```

This sets the target folder to the current Windows user's Downloads directory.

If your Downloads folder is located elsewhere, update the path accordingly.

### 5. Run in Preview Mode

The script uses preview mode by default:

```python
DRY_RUN = True
```

Run the script:

```bash
py file_organizer.py
```

The program displays where each file would be moved without actually moving anything.

**Review the preview carefully before proceeding.**

### 6. Move Files for Real

After reviewing the preview, change:

```python
DRY_RUN = True
```

to:

```python
DRY_RUN = False
```

Save the file and run:

```bash
py file_organizer.py
```

The script will now move files into their corresponding folders.

**Important:** Back up important files before using actual mode. Files are moved, not copied. Test with sample files first.

## Folder Categories

| Folder | File Types |
|---|---|
| Images | JPG, PNG, GIF, WEBP, SVG |
| Documents | PDF, DOCX, TXT, RTF |
| Presentations | PPT, PPTX, ODP |
| Spreadsheets | XLSX, CSV, ODS |
| Videos | MP4, MKV, MOV, AVI |
| Audio | MP3, WAV, M4A, FLAC |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Installers | EXE, MSI, MSIX |
| Code | HTML, CSS, JavaScript, Python, JSON, SQL |
| Ebooks | EPUB, MOBI, AZW, AZW3 |
| Others | File types not included in the categories |

## Automate with Windows Task Scheduler

You can configure Windows Task Scheduler to run the script automatically.

1. Open **Task Scheduler**.
2. Click **Create Basic Task**.
3. Enter a task name, such as `Automatic File Organizer`.
4. Choose a schedule, such as Daily.
5. Select **Start a Program**.
6. Configure the following fields:

**Program/script:**

```text
py
```

**Add arguments:**

```text
file_organizer.py
```

**Start in:**

```text
C:\path\to\python-automatic-file-organizer
```

Replace the example path with the actual folder containing your script.

7. Finish creating the task.
8. Test it with `DRY_RUN = True` before enabling actual file movement.

For a personal computer, **Run only when user is logged on** is a simple starting option. The computer must be on and the user logged in when the task is scheduled to run.

## Safety Notes

- Always test with `DRY_RUN = True` first.
- Back up important files before moving them.
- Do not run the script with administrator privileges unless necessary.
- Existing folders are skipped; the script does not organize files recursively inside them.
- Files with duplicate names are assigned a unique destination filename to avoid overwriting.
- Review installer files before keeping or executing them.

## What I Learned

- Python file handling and directory management.
- Working with file extensions and paths.
- Automating repetitive tasks.
- Basic error handling.
- Scheduling scripts with Windows Task Scheduler.

## Author

Created as a beginner Python automation project to practice file management and task scheduling.
