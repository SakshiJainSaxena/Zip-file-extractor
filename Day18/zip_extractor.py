import zipfile

def extract_archive(archivepath, destination_folder):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destination_folder)


if __name__ == "__main__":
    print("Code is working.")
