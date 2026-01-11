import os
import shutil

# Path of the folder to organize
SOURCE_FOLDER = "sample_folder"

# Folder categories and extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}

def create_folders(base_path):
    """Create category folders if they don't exist."""
    for folder in FILE_TYPES.keys():
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    os.makedirs(os.path.join(base_path, "Others"), exist_ok=True)

def organize_files(base_path):
    """Move files into categorized folders."""
    for file in os.listdir(base_path):
        file_path = os.path.join(base_path, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(
                        file_path,
                        os.path.join(base_path, folder, file)
                    )
                    moved = True
                    break

            if not moved:
                shutil.move(
                    file_path,
                    os.path.join(base_path, "Others", file)
                )

def main():
    create_folders(SOURCE_FOLDER)
    organize_files(SOURCE_FOLDER)
    print("Files organized successfully!")

if __name__ == "__main__":
    main()
