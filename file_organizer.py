
from pathlib import Path
import shutil

# Folder na aayusin
DOWNLOADS_FOLDER = Path.home() / "Downloads"

# True = preview lang; False = aktuwal na paglilipat
DRY_RUN = False

# File extensions at katumbas na folders
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".ico", ".heic"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"
    ],
    "Presentations": [
        ".ppt", ".pptx", ".odp"
    ],
    "Spreadsheets": [
        ".xls", ".xlsx", ".csv", ".ods"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".wmv", ".webm"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Installers": [
        ".exe", ".msi", ".msix"
    ],
    "Code": [
        ".html", ".htm", ".css", ".js", ".jsx",
        ".ts", ".tsx", ".py", ".java", ".cpp", ".c",
        ".php", ".json", ".xml", ".sql", ".ipynb"
    ],
    "Ebooks": [
        ".epub", ".mobi", ".azw", ".azw3"
    ]
}


def get_destination(file):
    extension = file.suffix.lower()

    for folder_name, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder_name

    return "Others"


def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )
        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files():
    if not DOWNLOADS_FOLDER.is_dir():
        print("ERROR: Hindi makita ang Downloads folder.")
        print("Folder:", DOWNLOADS_FOLDER)
        return

    print("Automatic File Organizer")
    print("Folder:", DOWNLOADS_FOLDER)
    print("Preview mode:", DRY_RUN)
    print("-" * 40)

    processed_count = 0

    # Files lang sa mismong Downloads folder.
    # Hindi gagalawin ang existing subfolders.
    for file in DOWNLOADS_FOLDER.iterdir():
        if not file.is_file():
            continue

        
        if file.name.lower() == "desktop.ini":
            print("[SKIP] desktop.ini")
            continue

       
        if file.name.startswith("~$"):
            print(f"[SKIP] {file.name}")
            continue

        folder_name = get_destination(file)
        target_folder = DOWNLOADS_FOLDER / folder_name
        destination = get_unique_path(target_folder / file.name)

        if DRY_RUN:
            print(f"[PREVIEW] {file.name} -> {folder_name}/")
        else:
            try:
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(destination))
                print(f"[MOVED] {file.name} -> {folder_name}/")
                processed_count += 1
            except OSError as error:
                print(f"[ERROR] {file.name}: {error}")

    print("-" * 40)

    if DRY_RUN:
        print("Preview lang ito. Walang file na inilipat.")
        print("Suriin muna ang mga destination bago mag-move.")
    else:
        print("Done! Files moved:", processed_count)


if __name__ == "__main__":
    organize_files()
