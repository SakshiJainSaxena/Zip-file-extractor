import zipfile
import pathlib


def make_archive(filepaths, destination_directory):
    destination_path = pathlib.Path(destination_directory, 'Compressed.zip')
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":
    print("Code is running fine")