from pdf2image import convert_from_path
from random import SystemRandom
from string import digits
import os

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
        
    return new_folder


def main():
    images = convert_from_path("Project Proposal.pdf")
    for i, image in enumerate(images):
        image.save(f"slide_{i}.jpg", "JPEG")


if __name__ == '__main__':
    main()
