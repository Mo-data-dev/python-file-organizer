from pathlib import Path
import shutil

folder = Path.home() / "Desktop" / "file_organizer"

file_types = {
    ".txt": "Documents",
    ".md": "Documents",
    ".pdf": "Documents",
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".py": "Code",
    ".json": "Data"
}


def organize_files():
    for file in folder.iterdir():

        if file.is_file() and file.name != "organizer.py":

            extension = file.suffix.lower()
            destination = file_types.get(extension, "Others")

            destination_folder = folder / destination
            destination_folder.mkdir(exist_ok=True)

            new_location = destination_folder / file.name

            if new_location.exists():
                print(f"Skipped: {file.name}")
            else:
                shutil.move(str(file), str(new_location))
                print(f"Moved: {file.name} -> {destination}")

    print("File organization complete!")


organize_files()
