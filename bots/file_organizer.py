import os, shutil

def run():
    downloads = os.path.expanduser("~/Downloads")
    dest = {
        "Documents": [".pdf", ".docx", ".txt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mov"],
        "Archives": [".zip", ".rar"],
    }

    print("Organizing files in Downloads...")

    for filename in os.listdir(downloads):
        file_path = os.path.join(downloads, filename)
        if os.path.isfile(file_path):
            for folder, extensions in dest.items():
                if filename.lower().endswith(tuple(extensions)):
                    folder_path = os.path.join(downloads, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, folder_path)
                    print(f"Moved {filename} → {folder}")
                    break
    print("Done organizing!")
