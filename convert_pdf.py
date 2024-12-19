from pdf2image import convert_from_path
from random import SystemRandom
from string import digits
import os
from shutil import rmtree
FILE_NAME_SIZE = 5
def generate_filename(used:set) -> str:
    helper = lambda: ''.join(SystemRandom().choice("ABC" + digits)
            for _ in range(FILE_NAME_SIZE))
    filename = helper()
    while filename in used:
        filename = helper()
    return filename

def convert_and_save(filename: str, upload_directory:os.path) -> str:
    images = convert_from_path(os.path.join(upload_directory, filename))
    
    existing_filenames = set(os.listdir(upload_directory))
    new_folder = generate_filename(existing_filenames)
        
    os.mkdir(os.path.join(upload_directory, new_folder))
    for i, image in enumerate(images):
        image.save(
            os.path.join(upload_directory, new_folder, f"{i}.jpg"))
    with open(os.path.join(upload_directory, new_folder, filename), 'w') as f:
        f.write("")
        
    return new_folder


def get_current_uploads(upload_directory:os.path, valid_extensions)-> list[str]:
    folders = os.listdir(upload_directory)
    presentations = []
    for folder in folders:
        files = os.listdir(os.path.join(upload_directory, folder))
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension in valid_extensions:
                presentations.append({"filename": file, "code": folder})
                break
    return presentations

def delete_folder(upload_directory:os.path, code:str) -> None:
    rmtree(os.path.join(upload_directory, code))

def main():
    images = convert_from_path("Project Proposal.pdf")
    for i, image in enumerate(images):
        image.save(f"slide_{i}.jpg", "JPEG")


if __name__ == '__main__':
    main()
